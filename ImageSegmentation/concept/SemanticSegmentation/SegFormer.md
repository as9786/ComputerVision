# SegFormer: Simple and Efficient Design for Semantic Segmentation with Transformers(2021)

- Hongkong University & NVIDIA
- Transformer를 semantic segmentation task에 적용한 모형

![image](https://user-images.githubusercontent.com/80622859/224026237-7e8550d5-2c21-4e04-8646-ec163ab3a43b.png)

- Parameter 대비 모형의 정확도(IoU)가 효율적이라는 것을 강조

## Abstract

1. Multi scale feature를 출력값으로 뽑는 계층적 구조의 transformer encoder
- Transformer 구조에서 각 patch의 위치 정보를 위해 사용하는 positional encoding이 필요 없도록 함
- 학습에 사용되지 않은 image size를 추론 시에 보간법 사용으로 인한 성능 하락 회피

2. 복잡한 deocoder를 사용하지 않고 MLP로만 이루어진 MLP decoder 사용
- Encoder에서 얻은 multi-scale feature를 결합하여 각 feature map에서의 local attention과 합쳐진 feature map에서의 global attention을 통해 강력한 representation을 얻음

## Method

- ViT에서는 HxWx3 일 때, patch size를 16 x 16 으로 설정
- SegFormer에서는 4 x 4 patch size 사용 => Desne prediction task에서 더 높은 성능
- Patch들은 multi-level feature map을 뽑아내는 transformer encoder로 들어가게 됨
- 각 feature map은 원본에 비해 {1/4,1/8,1/16,1/32}로 들어감
- MLP decoder에서는 multi-level feature map을 여러 층에 거쳐 최종적으로 H/4 x W/4 x N(cls) 해상도를 갖는 segmentation mask를 예측

![image](https://user-images.githubusercontent.com/80622859/224030064-817c904a-b702-48cf-b5f8-317813ed9b0b.png)

### 1. Hierarchical Transformer Encoder
- SegFormer의 encoder를 Mix Transformer Encoder(MiT)라고 부름
- ViT 기반

#### Hierarchical Feature Representation

- Single-resolution feature map을 생성하는 ViT와 다르게 high-resolution coarse feature와 low-resolution fine-grained feature를 가지는 mulit-level feature map을 통해 성능 향상
- Fine grained : 하나의 작업을 작은 단위의 process로 나눈 뒤 다수의 호출을 통해 작업 결과를 생성해내는 방식
- 각 단계별로 feature map은 아래와 같은 방식으로 해상도와 channel을 갖음

![image](https://user-images.githubusercontent.com/80622859/224031279-be449008-3e57-4ca6-8ed1-75284049137f.png)

### Overlapped Patch Merging

- ViT에서는 N x N x 3 patch들을 1 x 1 x C vector로 표현
- 각 patch들은 서로 겹치지 않기 때문에 patch들 간에 지역적 연속성이 보존되기 어려움
- 이를 해결하기 위해 swin transformer는 shifted window를 통해 patch들 간의 지역적 연속성을 보존
- SegFormer는 overlapping patch merging으로 접근
- 단순히 4 x 4 patch로 나누어 vector embedding을 진행하는 것이 아니라 마치 CNN이 sliding window로 조금씩 겹쳐가면서 연산을 진행하는 것과 같이 K(patch size or kernel size), S(stride), P(padding)을 사전에 정의하여 B(batch) x C(channel x stride^2) x N(num of patch)의 차원으로 patch를 분할하고 B(batch) x C(embedding dim) x W(width) x H(height)의 차원으로 병합을 수행

### Efficient Self-Attention

- Encoder의 self-attention layer는 많은 연산량을 차지
- SegFormersms patch size가 16 x 16이 아닌 4 x 4이기 때문에 더 많은 parameter 존재
- 기존 multi-head attention은 Q, K, V를 모두 N(HxW)xC 차원을 가지는 행렬로 만들어 아래 식으로 계산

![image](https://user-images.githubusercontent.com/80622859/224035293-8ee753c5-410c-4e65-873e-4a223381037d.png)

- 위의 수식은 $O(N^2)$ 계산복잡도를 가짐(N은 입력 길이)
- Large image가 입력으로 들어올 시 모형이 급격히 무거워짐
- Reduction ratio를 사전에 정의
- K와 V의 N(HxW) channel을 줄이는 sequence reduction process 적용

![image](https://user-images.githubusercontent.com/80622859/224036554-e8257cee-a505-48c2-8da5-cb6ddbca9c05.png)

- N을 R로 나누고 C에 R을 곱하여 reshape
- C x R 선형 변환을 통해서 다시 C로 줄임
- N/R x C 차원으로 key와 value 만들 수 있음
- R = [64,16,4,1]

### Mix-FFN
- ViT는 지역 정보를 추가하기 위해 positional encoding을 적용
- 이러한 방식은 입력 해상도가 고정되어야 한다는 문제가 있음.
- 입력 해상도가 달라지게 되면 보간법을 통해 크기를 맞춰주어야 하여 성능이 하락
- Positional encoding을 대신하여 3 x 3 convolution(stride:1/padding:1)을 FFN에 적용

![image](https://user-images.githubusercontent.com/80622859/224037381-b0d855b2-e807-49e9-9c49-86f43f3debd5.png)

- 기존의 ViT에서 Conv 3 x 3 layer만 추가
- 3 x 3 convolution은 가중치를 줄이기 위해 depth-wise convolution 사용

### 2. Lightweight All-MLP Decoder





