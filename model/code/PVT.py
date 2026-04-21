# Library
import torch
from torch import nn
from torch.nn import functional as F
from functools import partial

from timm.models.layers import DropPath, trunc_normal_

# MLP
class MLP(nn.Module):

    def __init__(self, in_features: int, hidden_features: int, out_features: int=None, act_layer=nn.GELU, drop: float=0.):
        super().__init__()
        out_features = out_features or in_features
        hidden_features = hidden_features or in_features
        self.linear1 = nn.Linear(in_features, hidden_features)
        self.act = act_layer()
        self.linear2 = nn.Linear(hidden_features, out_features)
        self.drop = nn.Dropout(drop)

    def forward(self, x):
        x = self.linear1(x)
        x = self.act(x)
        x = self.drop(x)
        x = self.linear2(x)
        x = self.drop(x)
        return x

class Attention(nn.Module):
    
    def __init__(self, dim: int, num_heads: int=8, qkv_bias: bool=False, qk_scale: bool=None, attn_drop: float=0., proj_drop: float=0., sr_ratio: float=1):
        super().__init__()
        assert dim % num_heads == 0, f'dim {dim} should be devided by num_heads {num_heads}'

        self.dim = dim
        self.num_heads = num_heads
        head_dim = dim // num_heads
        self.scale = qk_scale or head_dim ** -0.5

        self.q = nn.Linear(dim ,dim, bias=qkv_bias)
        self.kv = nn.Linear(dim, dim*2, bias=qkv_bias)
        self.attn_drop = nn.Dropout(attn_drop)
        self.proj = nn.Linear(dim, dim)
        self.proj_drop = nn.Dropout(proj_drop)

        self.sr_ratio = sr_ratio
        if sr_ratio > 1:
            self.sr = nn.Conv2d(dim, dim, kernel_size=sr_ratio, stride=sr_ratio)
            self.norm = nn.LayerNorm(dim)

    def forward(self, x, H, W):
        B, N, C = x.shape
        q = self.q(x).reshape(B, N, self.num_heads, C // self.num_heads).permute(0,2,1,3)

        if self.sr_ratio > 1:
            x_ = x.permute(0, 2, 1).reshape(B, C, H, W)
            # Spatial reduction
            x_ = self.sr(x_).reshape(B, C, -1).permute(0, 2, 1)
            x_ = self.norm(x_)
            # Key, value 한 번에 생성
            kv = self.kv(x_).reshape(B, -1, 2, self.num_heads, C // self.num_heads).permute(2, 0, 3, 1, 4)
        else:
            kv = self.kv(x).reshape(B, -1, 2, self.num_heads, C // self.num_heads).permute(2,0,3,1,4)
        
        k,v = kv[0], kv[1]

        attn = (q @ k.transpose(-2,-1)) * self.scale
        attn = attn.softmax(dim=-1)
        attn = self.attn_drop(attn)

        x = (attn @ v).transpose(1,2).reshape(B,N,C)
        x = self.proj(x)
        x = self.proj_drop(x)

        return x

class Block(nn.Module):
  def __init__(self, dim: int, num_heads: int, mlp_ratio: float=4., qkv_bias: bool=False, qk_scale: bool=False, drop: float=0., attn_drop: float=0., 
              drop_path: float=0., act_layer=nn.GELU, norm_layer=nn.LayerNorm, sr_ratio: float=1):

      super().__init__()
      self.norm1 = norm_layer(dim)
      self.attn = Attention(dim, num_heads=num_heads, qkv_bias=qkv_bias, qk_scale=qk_scale, attn_drop=attn_drop, proj_drop=drop, sr_ratio=sr_ratio)
      self.drop_path = DropPath(drop_path) if drop_path > 0 else nn.Identity()
      self.norm2 = norm_layer(dim)
      mlp_hidden_dim = int(dim * mlp_ratio)
      self.mlp = MLP(in_features=dim, hidden_features=mlp_hidden_dim, act_layer=act_layer, drop=drop)

  def forward(self, x, H, W):
      x = x + self.drop_path(self.attn(self.norm1(x), H, W))
      x = x + self.drop_path(self.mlp(self.norm2(x)))
      return x

# Patch embedding
class PatchEmbedding(nn.Module):

    def __init__(self, img_size: int=224, patch_size: int=16, in_chans: int=3, embed_dim: int=768):
        super().__init__()
        img_size = (img_size, img_size)
        patch_size = (patch_size, patch_size)

        self.img_size = img_size
        self.patch_size = patch_size
        self.H, self.W = img_size[0] // patch_size[0], img_size[1] // patch_size[1]
        self.num_patches = self.H * self.W
        self.proj = nn.Conv2d(in_chans, embed_dim, kernel_size=patch_size, stride=patch_size)
        self.norm = nn.LayerNorm(embed_dim)

    def forward(self, x):
        B, C, H, W = x.shape
        x = self.proj(x).flatten(2).transpose(1,2)
        x = self.norm(x)
        H, W = H // self.patch_size[0], W // self.patch_size[1]

        return x, (H, W)

# PVT
class PVT(nn.Module):
    def __init__(self, img_size: int=224, patch_size: int=16, in_chans: int=3, num_classes: int=1000, embed_dims: list=[64,128,256,512], num_heads: list=[1,2,4,8], 
                mlp_ratios: list=[4,4,4,4], qkv_bias: bool=False, qk_scale: bool=False, drop_rate: float=0., attn_drop_rate: float=0., drop_path_rate: float=0., norm_layer=nn.LayerNorm,
                depths: list=[3,4,6,3], sr_ratios: list=[8,4,2,1], num_stages: int=4):

        super().__init__()
        self.num_classes = num_classes
        self.depths = depths
        self.num_stages = num_stages

        dpr = [x.item() for x in torch.linspace(0, drop_path_rate, sum(depths))]
        cur = 0

        for i in range(num_stages):
            # Patch embedding
            patch_embed = PatchEmbedding(
                img_size=img_size if i == 0 else img_size // (2 ** (i + 1)),  # 단계가 깊어질수록 해상도 감소
                patch_size=patch_size if i == 0 else 2,                       # 첫 stage만 큰 patch, 이후는 downsampling 역할
                in_chans=in_chans if i == 0 else embed_dims[i - 1],           # 이전 stage의 output 채널 사용
                embed_dim=embed_dims[i]                                       # 현재 stage embedding dimension
            )
            # Positional embedding 길이 설정 (마지막은 cls token 추가)
            num_patches = patch_embed.num_patches if i != num_stages - 1 else patch_embed.num_patches + 1
            pos_embed = nn.Parameter(torch.zeros(1, num_patches, embed_dims[i]))            
            pos_drop = nn.Dropout(p=drop_rate)

            block = nn.ModuleList([Block(dim=embed_dims[i], num_heads=num_heads[i], mlp_ratio=mlp_ratios[i], qkv_bias=qkv_bias, qk_scale=qk_scale, drop=drop_rate, 
                                        attn_drop=attn_drop_rate, drop_path=dpr[cur+j], norm_layer=norm_layer, sr_ratio=sr_ratios[i]) for j in range(depths[i])])
            cur += depths[i]

            setattr(self, f"patch_embed{i + 1}", patch_embed)
            setattr(self, f"pos_embed{i + 1}", pos_embed)
            setattr(self, f"pos_drop{i + 1}", pos_drop)
            setattr(self, f"block{i + 1}", block)

        self.norm = norm_layer(embed_dims[3])

        # cls token
        self.cls_token = nn.Parameter(torch.zeros(1,1,embed_dims[3]))

        # Classification head
        self.head = nn.Linear(embed_dims[3], num_classes) if num_classes > 0 else nn.Identity()

        # 가중치 초기화
        for i in range(num_stages):
            pos_embed = getattr(self, f'pos_embed{i+1}')
            trunc_normal_(pos_embed, std=0.02)
        trunc_normal_(self.cls_token, std=0.02)
        self.apply(self._init_weights)

    def _init_weights(self, m):
        if isinstance(m, nn.Linear):
            trunc_normal_(m.weight, std=0.02)
            if isinstance(m, nn.Linear) and m.bias is not None:
                nn.init.constant_(m.bias, 0)
        elif isinstance(m, nn.LayerNorm):
            nn.init.constant_(m.bias, 0)
            nn.init.constant_(m.weight, 1)

    def _get_pos_embed(self, pos_embed, patch_embed, H, W):
        if H * W == self.patch_embed1.num_patches:
            return pos_embed
        else:
            return F.interpolate(
                pos_embed.reshape(1, patch_embed.H, patch_embed.W, -1).permute(0, 3, 1, 2),
                size=(H, W), mode="bilinear").reshape(1, -1, H * W).permute(0, 2, 1)

    def forward_features(self, x):
        B = x.shape[0]

        for i in range(self.num_stages):
            patch_embed = getattr(self, f"patch_embed{i + 1}")
            pos_embed = getattr(self, f"pos_embed{i + 1}")
            pos_drop = getattr(self, f"pos_drop{i + 1}")
            block = getattr(self, f"block{i + 1}")
            x, (H, W) = patch_embed(x)

            if i == self.num_stages - 1:
                cls_tokens = self.cls_token.expand(B, -1, -1)
                x = torch.cat((cls_tokens, x), dim=1)
                pos_embed_ = self._get_pos_embed(pos_embed[:, 1:], patch_embed, H, W)
                pos_embed = torch.cat((pos_embed[:,0:1], pos_embed_), dim=1)

            else:
                pos_embed = self._get_pos_embed(pos_embed, patch_embed, H, W)

            x = pos_drop(x + pos_embed)
            for blk in block:
                x = blk(x, H, W)
            if i != self.num_stages - 1:
                x = x.reshape(B, H, W, -1).permute(0,3,1,2).contiguous()

        x = self.norm(x)

        return x[:, 0]

    def forward(self, x):
        x = self.forward_features(x)
        x = self.head(x)

        return x

model = PVT(
        patch_size=4, embed_dims=[64, 128, 320, 512], num_heads=[1, 2, 5, 8], mlp_ratios=[8, 8, 4, 4], qkv_bias=True,
        norm_layer=partial(nn.LayerNorm, eps=1e-6), depths=[2, 2, 2, 2], sr_ratios=[8, 4, 2, 1])
