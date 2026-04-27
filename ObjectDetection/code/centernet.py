# Library
import torch
from torch import nn 
from torch.nn import functional as F
from torchvision import models

Norm = nn.BatchNorm2d

def map2coords(h, w, stride):
    # x축 좌표 생성
    shifts_x = torch.arange(0, w * stride, step=stride, dtype=torch.float32)
    # y축 좌표 생성
    shifts_y = torch.arange(0, h * stride, step=stride, dtype=torch.float32)
    # 모든 좌표를 격자점 형태로 생성
    shift_y, shift_x = torch.meshgrid(shifts_y, shifts_x)
    # 2D -> 1D
    shift_x = shift_x.reshape(-1)
    shift_y = shift_y.reshape(-1)
    # (x,y) 좌표를 쌍으로 묶고, 각 셀의 중심으로 이동
    locations = torch.stack((shift_x, shift_y), dim=1) + stride // 2
    return locations 

def gather_feature(fmap, index, mask=None, use_transform=False):
    # (B, C, H, W) -> (B, H X W, C)
    if use_transform:
        batch, channel = fmap.shape[:2]
        fmap = fmap.view(batch, channel, -1).permute((0,2,1)).contiguous()

    # 마지막 차원 크기
    dim = fmap.size(-1)
    # (B, K) -> (B, K, C)
    index = index.unsqueeze(len(index.shape)).expand(*index.shape, dim)
    fmap = fmap.gather(dim=1, index=index)
    if mask is not None:
        mask = mask.unsqueeze(2).expand_as(fmap)
        fmap = fmap[mask]
        fmap = fmap.reshape(-1, dim)

    return fmap

# Backbone
class ResNet(nn.Module):

    def __init__(self, pretrained=True):
        super().__init__()
        self.resnet = models.resnet50(pretrained=pretrained)
        self.outplanes = 2048

    def forward(self, x):
        size = x.size()
        assert size[-1] % 32 == 0 and size[-2] % 32 == 0, '사진 해상도는 32로 나누어져야 합니다.'

        x = self.resnet.conv1(x)
        x = self.resnet.bn1(x)
        x = self.resnet.relu(x)
        x = self.resnet.maxpool(x)

        feature1 = self.resnet.layer1(x)
        feature2 = self.resnet.layer2(feature1)
        feature3 = self.resnet.layer3(feature2)
        feature4 = self.resnet.layer4(feature3)

        return feature1, feature2, feature3, feature4

    def freeze_bn(self):
        for layer in self.modules():
            if isinstance(layer, nn.BatchNorm2d):
                layer.eval()

    def freeze_stages(self, stage):
        if stage >= 0:
            self.resnet.bn1.eval()
            for m in [self.resnet.conv1, self.resnet.bn1]:
                for param in m.parameters():
                    param.requires_grad = False

        for i in range(1, stage + 1):
            layer = getattr(self.resnet, 'layer{}'.format(i))
            layer.eval()
            for param in layer.parameters():
                param.requires_grad = False

# Decoder
class Decoder(nn.Module):

    def __init__(self, inplanes, bn_momentum=0.1):
        super().__init__()
        self.bn_momentum = bn_momentum
        # Backbone output : [b, 2048, h, w]
        self.inplanes = inplanes
        self.deconv_with_bias = False
        self.deconv_layer = self.make_deconv_layer(3, [256,256,256], [4,4,4])

    def make_deconv_layer(self, num_layers, num_filters, num_kernels):
        layers = []
        for i in range(num_layers):
            kernel = num_kernels[i]
            # 출력 크기를 맞추기 위한 경험적 설정
            padding = 0 if kernel == 2 else 1
            output_padding = 1 if kernel == 3 else 0
            planes = num_filters[i]
            deconv = nn.ConvTranspose2d(in_channels=self.inplanes, 
                                        out_channels=planes, 
                                        kernel_size=kernel, 
                                        stride=2, 
                                        padding=padding, 
                                        output_padding=output_padding,
                                        bias=self.deconv_with_bias)
            layers.append(deconv)
            layers.append(nn.BatchNorm2d(planes, momentum=self.bn_momentum))
            layers.append(nn.ReLU(inplace=True))
            self.inplanes = planes
        return nn.Sequential(*layers)

    def forward(self, x):
        return self.deconv_layer(x)

 # 1 x 1 합성곱
class Conv1x1(nn.Module):
    def __init__(self, num_in, num_out):
        super().__init__()
        self.conv = nn.Conv2d(num_in, num_out, kernel_size=1, bias=False)
        self.norm = Norm(num_out)
        self.act = nn.ReLU(inplace=True)
        self.block = nn.Sequential(self.conv, self.norm, self.act)

    def forward(self, x):
        return self.block(x)

# 3 x 3 합성곱
class Conv3x3(nn.Module):
    def __init__(self, num_in, num_out):
        super().__init__()
        self.conv = nn.Conv2d(num_in, num_out, kernel_size=3, padding=1, bias=False)
        self.norm = Norm(num_out)
        self.act = nn.ReLU(inplace=True)
        self.block = nn.Sequential(self.conv, self.norm, self.act)

    def forward(self, x):
        return self.block(x)

class FPN(nn.Module):
    def __init__(self, in_channels=[256, 512, 1024, 2048], outplanes=512):
        super().__init__()

        # 각 backbone feature의 channel을 outplanes로 통일
        self.laterals = nn.ModuleList([
            Conv1x1(in_ch, outplanes) for in_ch in in_channels
        ])

        # bottom-up path에서 concat 후 channel 수가 증가하므로 그에 맞게 설정
        self.smooths = nn.ModuleList([
            Conv3x3(outplanes * c, outplanes * c) for c in range(1, 5)
        ])

        self.pooling = nn.MaxPool2d(2)

    def forward(self, features):
        # features: [C1, C2, C3, C4]
        # channel:  [256, 512, 1024, 2048]

        laterals = [
            lateral(feature) for lateral, feature in zip(self.laterals, features)
        ]

        map4 = laterals[3]
        map3 = laterals[2] + F.interpolate(map4, size=laterals[2].shape[-2:], mode='nearest')
        map2 = laterals[1] + F.interpolate(map3, size=laterals[1].shape[-2:], mode='nearest')
        map1 = laterals[0] + F.interpolate(map2, size=laterals[0].shape[-2:], mode='nearest')

        map1 = self.smooths[0](map1)
        map2 = self.smooths[1](torch.cat([map2, self.pooling(map1)], dim=1))
        map3 = self.smooths[2](torch.cat([map3, self.pooling(map2)], dim=1))
        map4 = self.smooths[3](torch.cat([map4, self.pooling(map3)], dim=1))

        return map4
class Head(nn.Module):
    def __init__(self, channel, num_classes):
        super().__init__()

        self.hm = nn.Sequential(
            nn.Conv2d(channel, channel, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(channel, num_classes, kernel_size=1)
        )

        self.wh = nn.Sequential(
            nn.Conv2d(channel, channel, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(channel, 2, kernel_size=1)
        )

        self.reg = nn.Sequential(
            nn.Conv2d(channel, channel, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(channel, 2, kernel_size=1)
        )

    def forward(self, x):
        return {
            "hm": self.hm(x),
            "wh": self.wh(x),
            "reg": self.reg(x)
        }

class CenterNet(nn.Module):
    def __init__(self, num_classes, class_name):
        super().__init__()

        self.backbone = ResNet()

        # ResNet feature channel 순서가 [layer1, layer2, layer3, layer4] 라고 가정
        self.fpn = FPN(
            in_channels=[256, 512, 1024, 2048],
            outplanes=512
        )

        # FPN이 최종적으로 outplanes * 4 채널을 반환하므로 2048 입력
        self.upsample = Decoder(inplanes=512 * 4)

        # Decoder 최종 출력 채널이 64라면 Head channel=64
        self.head = Head(channel=256, num_classes=num_classes)

        self.down_stride = 4
        self.score_th = 0.1
        self.class_name = class_name

    def forward(self, x):
        feats = self.backbone(x)
        feat = self.fpn(feats)
        feat = self.upsample(feat)
        out = self.head(feat)

        return out

model = CenterNet(1, ['car'])
