# Library
import torch 
from torch import nn
import torch.nn.functional as F
from torchvision.models import resnet50
from torchvision.ops import nms 
import numpy as np
import math

# Denormalize
def cxcy_to_xy(cxcy):
    x1y1 = cxcy[..., :2] - cxcy[..., 2:] / 2
    x2y2 = cxcy[..., :2] + cxcy[..., 2:] / 2
    return torch.cat([x1y1,x2y2],dim=1)

def decode(tcxcy, center_anchor):
    cxcy = tcxcy[:, :2] * center_anchor[:, 2:] + center_anchor[:, :2]
    wh = torch.exp(tcxcy[:, 2:]) * center_anchor[:, 2:]
    cxywh = torch.cat([cxcy, wh], dim=1)
    return cxywh

# Anchor
def create_anchors(img_size):
    pyramid_levels = np.array([3,4,5,6,7])
    # 올림 나눗셈
    feature_maps = [(img_size + 2 ** x - 1) // (2**x) for x in pyramid_levels]

    # 종횡비
    aspect_ratios = np.array([1,2,0.5])
    scales = np.array([2**0, 2**(1/3), 2**(2/3)])

    strides = [img_size // f for f in feature_maps]
    areas = [32, 64, 128, 256, 512]

    center_anchors = []
    # 각 pyramid level에 따른 anchor 생성
    for feature_map, area, stride in zip(feature_maps, areas, strides):
        for i in range(feature_map):
            for j in range(feature_map):
                c_x = (j + 0.5) / feature_map
                c_y = (i + 0.5) / feature_map

                for aspect_ratio in aspect_ratios:
                    for scale in scales:
                        w = (area / img_size) * scale * np.sqrt(aspect_ratio)
                        h = (area / img_size) * scale / np.sqrt(aspect_ratio)
                        anchor = [c_x, c_y, w, h]
                        center_anchors.append(anchor)

    center_anchors = np.array(center_anchors).astype(np.float32)
    center_anchors = torch.FloatTensor(center_anchors)

    return center_anchors

# Classification head
class ClassificationHead(nn.Module):

    def __init__(self, num_classes, prior_prob=0.01):
        super().__init__()
        self.num_classes = num_classes
        self.conv1 = nn.Conv2d(256,256,3,padding=1)
        self.conv2 = nn.Conv2d(256,256,3,padding=1)
        self.conv3 = nn.Conv2d(256,256,3,padding=1)
        self.conv4 = nn.Conv2d(256,256,3,padding=1)
        self.conv5 = nn.Conv2d(256, 9 * self.num_classes, 3, padding=1)
        self.relu = nn.ReLU()
        self.sigmoid = nn.Sigmoid()

        self._init_weights(prior_prob)

    def _init_weights(self, prior_prob):
        # 모든 합성곱 가중치를 정규분포로 초기화
        for layer in [self.conv1, self.conv2, self.conv3, self.conv4, self.conv5]:
            nn.init.normal_(layer.weight, std=0.01)
            if layer.bias is not None:
                nn.init.constant_(layer.bias, 0)
        # 마지막 분류 합성곱의 편향을 사전 분포 확률에 맞게 설정
        bias_value = -math.log((1 - prior_prob) / prior_prob) # Logit function
        nn.init.constant_(self.conv5.bias, bias_value)

    def forward(self, x):
        batch_size = x.size(0)
        x = self.conv1(x)
        x = self.relu(x)
        x = self.conv2(x)
        x = self.relu(x)
        x = self.conv3(x)
        x = self.relu(x)
        x = self.conv4(x)
        x = self.relu(x)
        x = self.conv5(x)
        x = self.sigmoid(x)
        x = x.permute(0,2,3,1).contiguous() # 
        x = x.view(batch_size, -1, self.num_classes)
        return x
      
# Regression head
class RegressionHead(nn.Module):

    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(256,256,3,padding=1)
        self.conv2 = nn.Conv2d(256,256,3,padding=1)
        self.conv3 = nn.Conv2d(256,256,3,padding=1)
        self.conv4 = nn.Conv2d(256,256,3,padding=1)
        self.conv5 = nn.Conv2d(256, 4*9, 3, padding=1)
        self.relu = nn.ReLU()

    def forward(self, x):
        batch_size = x.size(0)
        x = self.conv1(x)
        x = self.relu(x)
        x = self.conv2(x)
        x = self.relu(x)
        x = self.conv3(x)
        x = self.relu(x)
        x = self.conv4(x)
        x = self.relu(x)
        x = self.conv5(x)
        x = x.permute(0,2,3,1).contiguous()
        x = x.view(batch_size, -1, 4)
        return x
# Backbone
class ResNet50(nn.Module):

    def __init__(self, pretrained=True):
        super().__init__()
        self.resnet50_list = nn.ModuleList(list(resnet50(pretrained=pretrained).children())[:-1])

    def forward(self, x):
        x = self.resnet50_list[0](x) # Conv
        x = self.resnet50_list[1](x) # BN
        x = self.resnet50_list[2](x) # ReLU
        x = self.resnet50_list[3](x) # Max pooling

        x = self.resnet50_list[4](x)
        c3 = self.resnet50_list[5](x)
        c4 = self.resnet50_list[6](c3)
        c5 = self.resnet50_list[7](c4)

        return [c3, c4, c5]
# FPN
class FPN(nn.Module):

    def __init__(self):
        super().__init__()
        self.stride = 128
        channels = [512, 1024, 2048]
        self.conv1 = nn.Conv2d(channels[0], 256, 1)
        self.conv2 = nn.Conv2d(channels[1], 256, 1)
        self.conv3 = nn.Conv2d(channels[2], 256, 1)
        # Pyramid feature
        self.conv4 = nn.Conv2d(channels[2], 256, 3, stride=2, padding=1)
        self.conv5 = nn.Conv2d(256, 256, 3, stride=2, padding=1)
        # Smoothing
        self.conv6 = nn.Conv2d(256,256,3,1)
        self.conv7 = nn.Conv2d(256,256,3,1)
        self.conv8 = nn.Conv2d(256,256,3,1)

        self._init_weights()

    def _init_weights(self):
        for conv in [self.conv1,self.conv2,self.conv3,self.conv4,self.conv5,self.conv6,self.conv7,self.conv8]:
            nn.init.xavier_uniform_(conv.weight)
            if conv.bias is not None:
                nn.init.constant_(conv.bias, 0)
    
    def forward(self, c3, c4, c5):
        p5 = self.conv3(c5)
        p4 = self.conv2(c4)
        p4 = F.interpolate(p5, size=p4.size()[2:]) + p4 
        p3 = self.conv1(c3)
        p3 = F.interpolate(p4, size=p3.size()[2:]) + p3 

        p6 = self.conv4(c5)
        p7 = self.conv5(F.relu(p6))

        p3 = self.conv6(p3)
        p4 = self.conv7(p4)
        p5 = self.conv8(p5)

        return [p3,p4,p5,p6,p7]

class RetinaNet(nn.Module):

    def __init__(self, num_classes, img_size):
        super().__init__()

        self.anchors = create_anchors(img_size)

        # Module
        self.backbone = ResNet50(True)
        self.fpn = FPN()
        self.cls_module = ClassificationHead(num_classes)
        self.reg_module = RegressionHead()
        self.initialize_sub_modules()

    def initialize_sub_modules(self):
        for c in self.reg_module.children():
            if isinstance(c, nn.Conv2d):
                nn.init.normal_(c.weight, std=0.01)
                nn.init.constant_(c.bias, 0)

    def freeze_bn(self):
        for layer in self.modules:
            if isinstance(layer, nn.BatchNorm2d):
                layer.eval()

    def forward(self, x):
        c3, c4, c5 = self.backbone(x)
        features = self.fpn(c3,c4,c5)
        c = torch.cat([self.cls_module(feature) for feature in features], dim=1)
        reg= torch.cat([self.reg_module(feature) for feature in features], dim=1)
        return c, reg 
    
    def predict(self, cls, reg, center_anchor, opts):
        pred_cls = cls
        pred_reg = reg 

        pred_cls = pred_cls.squeeze()
        pred_bbox = cxcy_to_xy(decode(pred_reg.squeeze(), center_anchor)).clamp(0,1)
        
        bbox, label, score = self._suppress(pred_bbox, pred_cls, opts)
        return bbox, label, score 
    
    def _suppress(self, raw_cls_bbox, raw_prob, opts):
        bboxes = []
        labels = []
        scores = []

        for l in range(1, opts.num_classes):  # 0은 background
            prob_l = raw_prob[:, l]
            mask = prob_l > opts.thres

            if mask.sum() == 0:
                continue

            cls_bbox_l = raw_cls_bbox[mask]
            prob_l = prob_l[mask]

            keep = nms(cls_bbox_l, prob_l, iou_threshold=0.3)

            if len(keep) == 0:
                continue

            bboxes.append(cls_bbox_l[keep])
            labels.append(torch.full((len(keep),), l - 1, dtype=torch.int64, device=cls_bbox_l.device))
            scores.append(prob_l[keep])

        if len(bboxes) == 0:
            return (
                np.zeros((0, 4), dtype=np.float32),
                np.zeros((0,), dtype=np.int32),
                np.zeros((0,), dtype=np.float32),
            )

        bboxes = torch.cat(bboxes, dim=0).cpu().numpy().astype(np.float32)
        labels = torch.cat(labels, dim=0).cpu().numpy().astype(np.int32)
        scores = torch.cat(scores, dim=0).cpu().numpy().astype(np.float32)

        return bboxes, labels, scores

if __name__ == '__main__':
  img = torch.randn([2, 3, 600, 600]).cuda()
  model = RetinaNet(num_classes=81, img_size=600).cuda()
  output = model(img)
  print(output[0].size())
  print(output[1].size())

