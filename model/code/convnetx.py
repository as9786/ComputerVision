# Library
import torch
from torch import nn
import torch.nn.functional as F
from timm.models.layers import trunc_normal_, DropPath

# 층 정규화
class LayerNorm(nn.Module):
    
    def __init__(self, normalized_shape, eps=1e-6, data_format='channels_last'):
        super().__init__()
        # 크기
        self.weight = nn.Parameter(torch.ones(normalized_shape))
        # Shift
        self.bias = nn.Parameter(torch.ones(normalized_shape))
        # Prevent zero-division 
        self.eps = eps
        self.data_format = data_format
        if self.data_format not in ['channels_last', 'channels_first']:
            raise NotImplementedError
        self.normalized_shape = (normalized_shape, )

    def forward(self, x):
        if self.data_format == 'channels_last':
            return F.layer_norm(x, self.normalized_shape, self.weight, self.bias, self.eps)
        elif self.data_format == 'channels_first':
            # 채널 방향에 대한 평균 계싼
            u = x.mean(1, keepdim=True)
            # 분산 계산
            s = (x-u).pow(2).mean(1, keepdim=True)
            # 정규화
            x = (x-u) / torch.sqrt(s + self.eps)
            # Scale + Shift 
            x = self.weight[:, None, None] * x + self.bias[:, None, None]
            return x

# Block
class Block(nn.Module):

    def __init__(self, dim, drop_path=0, layer_scale_init_value=1e-6):
        super().__init__()
        # Depth-Wise convolution 
        self.dwconv = nn.Conv2d(dim, dim, kernel_size=7, padding=3, groups=dim)
        self.norm = LayerNorm(dim, eps=1e-6)
        self.pwconv1 = nn.Linear(dim, 4 * dim)
        self.act = nn.GELU()
        self.pwconv2 = nn.Linear(dim * 4, dim)
        self.gamma = nn.Parameter(layer_scale_init_value * torch.ones((dim)), 
                                  requires_grad=True) if layer_scale_init_value > 0 else None 
        self.drop_path = DropPath(drop_path) if drop_path > 0 else nn.Identity() 

    def forward(self, x):
        inp = x
        x = self.dwconv(x)
        x = x.permute(0,2,3,1) #(N, C, H, W) -> (N, H, W, C)
        x = self.norm(x)
        x = self.pwconv1(x)
        x = self.act(x)
        x = self.pwconv2(x)
        if self.gamma is not None:
            x = self.gamma * x
        x = x.permute(0,3,1,2) # (N, H, W, C) -> (N, C, H, W)
        x = inp + self.drop_path(x)
        return x
    
# 모형
class ConvNeXt(nn.Module):

    def __init__(
        self,
        in_chans=3,                     # # of input image channle
        num_classes=1000,              # # of classes
        depths=[3, 3, 9, 3],           # # of blocks in each stage
        dims=[96, 192, 384, 768],      # # of channels in each stage
        drop_path_rate=0,              
        layer_scale_init_value=1e-6,   
        head_init_scale=1              
    ):
        super().__init__()


        # Downsampling layer
        self.downsample_layers = nn.ModuleList()

        # stem: 입력 이미지를 처음 받아서 patchify + channel 확장
        stem = nn.Sequential(
            nn.Conv2d(in_chans, dims[0], kernel_size=4, stride=4),
            LayerNorm(dims[0], eps=1e-6, data_format='channels_first')
        )
        self.downsample_layers.append(stem)

        # 각 단계 사이에서 해상도를 절반으로 줄이고 채널 수를 증가시킴
        for i in range(3):
            downsample_layer = nn.Sequential(
                LayerNorm(dims[i], eps=1e-6, data_format='channels_first'),
                nn.Conv2d(dims[i], dims[i+1], kernel_size=2, stride=2)
            )
            self.downsample_layers.append(downsample_layer)

        # 각 단계 정의
        self.stages = nn.ModuleList()

        # 전체 Block 개수(sum(depths))만큼. DropPath 비율을 0 ~ drop_path_rate까지 선형 증가하도록 생성
        dp_rates = [x.item() for x in torch.linspace(0, drop_path_rate, sum(depths))]

        cur = 0
        for i in range(4):
            stage = nn.Sequential(
                *[
                    Block(
                        dim=dims[i],
                        drop_path=dp_rates[cur + j],
                        layer_scale_init_value=layer_scale_init_value
                    )
                    for j in range(depths[i])
                ]
            )
            self.stages.append(stage)
            cur += depths[i]

        # Global Average Pooling 이후 feature에 LayerNorm 적용
        self.norm = nn.LayerNorm(dims[-1], eps=1e-6)

        # 최종 classification layer
        self.head = nn.Linear(dims[-1], num_classes)

        # 가중치 초기화
        self.apply(self._init_weights)

        # classification head의 weight, bias를 추가 스케일링
        self.head.weight.data.mul_(head_init_scale)
        self.head.bias.data.mul_(head_init_scale)

    def _init_weights(self, m):
        # Conv2d와 Linear에 대해 weight 초기화
        if isinstance(m, (nn.Conv2d, nn.Linear)):
            trunc_normal_(m.weight, std=0.02)   # truncated normal 초기화
            nn.init.constant_(m.bias, 0)        # bias는 0으로 초기화

    def forward_features(self, x):
        for i in range(4):
            x = self.downsample_layers[i](x) 
            x = self.stages[i](x)           
            
        return self.norm(x.mean([-2, -1]))

    def forward(self, x):
        x = self.forward_features(x)
        x = self.head(x)
        return x
    
if __name__ == '__main__':
    model = ConvNeXt(depths=[3, 3, 27, 3], dims=[192, 384, 768, 1536])
    sample = torch.rand((1,3,64,64))
    o = model(sample)
    print(o.shape)
