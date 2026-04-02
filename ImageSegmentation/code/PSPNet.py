# Library
from torch import nn
import torch
import torch.nn.functional as F

# PSP block
class PSPModule(nn.Module):

    def __init__(self, in_channel, mid_reduce=4, out_channel=512, sizes=(1,2,3,6)):
        super().__init__()
        self.mid_channel = int(in_channel / mid_reduce)
        self.stages = nn.ModuleList([nn.Sequential(nn.AdaptiveAvgPool2d(output_size=(size, size)), nn.Conv2d(in_channel, self.mid_channel, kernel_size=1, bias=False)) for size in sizes])
        self.bottleneck = nn.Conv2d((in_channel + self.mid_channel * 4), out_channel, kernel_size=3)
        self.bn = nn.BatchNorm2d(out_channel)
        self.prelu = nn.PReLU()

    def forward(self, x):
        h, w = x.size(2), x.size(3)
        muls = [F.upsample(input=stage(x), size=(h,w), mode='bilinear') for stage in self.stages]
        out = self.bottleneck(torch.cat((muls[0], muls[1], muls[2], muls[3], x), 1))
        out = self.bn(out)
        out = self.prelu(out)
        return out

# 예시
model = PSPModule(64)
sample = torch.randn((1,64,224,224))
output = model(sample)
print(output.shape) 
