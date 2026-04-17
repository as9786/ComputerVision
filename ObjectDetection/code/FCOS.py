# Library
import math
import numpy as np
from torch import nn
import torch.nn.functional as F
import torch
import torchvision
from torchvision import transforms as T
from torchvision.models import resnet50

# class
CLASSES = ['BACKGROUND', 'PLATE']

# Backbone
class Backbone(nn.Module):

    def __init__(self):
        super().__init__()
        self.resnet = resnet50(pretrained=False)

    def forward(self, x):
        x = self.resnet.conv1(x)
        x = self.resnet.bn1(x)
        x = self.resnet.relu(x)
        x = self.resnet.maxpool(x)
        p1 = self.resnet.layer1(x)
        p2 = self.resnet.layer2(p1)
        p3 = self.resnet.layer3(p2)
        p4 = self.resnet.layer4(p3)

        return p2, p3, p4

# FCOS
class FCOS(nn.Module):

    def __init__(self):
        super().__init__()

        self.backbone = Backbone()
        self.scales = nn.Parameter(torch.tensor([8.,12.,32.,64.,128.]))
        self.strides = [8, 16, 32, 64, 128]

        self.conv1 = self.conv_gn(512,256)
        self.conv2 = self.conv_gn(1024,256)
        self.conv3 = self.conv_gn(2048,256)
        self.conv4 = self.conv_gn(256,256,stride=2)
        self.conv5 = self.conv_gn(256,256,stride=2)

        self.cls_head = nn.Sequential(
            self.conv_gn(256,256),
            nn.ReLU(inplace=True),
            self.conv_gn(256,256),
            nn.ReLU(inplace=True),
            self.conv_gn(256,256),
            nn.ReLU(inplace=True),
            self.conv_gn(256,256),
            nn.ReLU(inplace=True)
        )
        self.cls_final = self.conv_gn(256, len(CLASSES))
        self.cls_centerness = self.conv_gn(256,1)

        self.reg_head = nn.Sequential(
            self.conv_gn(256,256),
            nn.ReLU(inplace=True),
            self.conv_gn(256,256),
            nn.ReLU(inplace=True),
            self.conv_gn(256,256),
            nn.ReLU(inplace=True),
            self.conv_gn(256,256),
            nn.ReLU(inplace=True),
            self.conv_gn(256,4)
        )
        
        self._init_weights()

    def _init_weights(self):
        # 모든 합성곱 가중치를 정규분포로 초기화
        for layer in [self.conv1, self.conv2, self.conv3, self.conv4, self.conv5, self.cls_final, self.cls_centerness, self.cls_head, self.reg_head]:
            for l in layer.modules():
                if isinstance(l, nn.Conv2d):
                    nn.init.normal_(l.weight, std=0.01)
                    if l.bias is not None:
                        nn.init.constant_(l.bias, 0)

    def conv_gn(self, in_channels, out_channels, kernel_size=3, padding=1, stride=1):
        layer = nn.Sequential(
            nn.GroupNorm(32, in_channels),
            nn.Conv2d(in_channels, out_channels, kernel_size=kernel_size, padding=padding, stride=stride)
        )
        return layer

    def forward(self, x):
        layer1, layer2, layer3 = self.backbone(x)
        p5 = self.conv3(layer3)
        p4 = self.conv2(layer2) + F.interpolate(p5, size=layer2.shape[2:4], mode='bilinear', align_corners=True)
        p3 = self.conv1(layer1) + F.interpolate(p4, size=layer1.shape[2:4], mode='bilinear', align_corners=True)
        p6 = self.conv4(p5)
        p7 = self.conv5(p6)

        feature_pyramid = [p3, p4, p5, p6, p7]

        classes_by_feature = []
        centerness_by_feature = []
        reg_by_feature = []

        for scale, stride, feature in zip(self.scales, self.strides, feature_pyramid):
            c = self.cls_head(feature)
            classes = self.cls_final(c).sigmoid()
            centerness = self.cls_centerness(c).sigmoid()
            reg = torch.exp(self.reg_head(feature)) * scale

            classes = classes.permute(0,2,3,1).contiguous()
            centerness = centerness.permute(0,2,3,1).contiguous().squeeze(3)
            reg = reg.permute(0,2,3,1).contiguous()

            reg_by_feature.append(reg)
            centerness_by_feature.append(centerness)
            classes_by_feature.append(classes)

        return classes_by_feature, centerness_by_feature, reg_by_feature
      
# 모형
model = FCOS()
model.eval()

sample = torch.randn(1,3,32,32)
o = model(sample)
