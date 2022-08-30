# Swin Transformer: Hierarchical Vision Transformer using Shifted Windows
- ViT는 모든 patch가 self attention을 함으로 계산 비용이 크게 발생

-> 각 patch를 window로 나누어 해당 window 안에서만 self attention을 수행하고 그 window를 한 번 shift한 후에 다시 self attention을 하는 구조 제시
- 일반적인 Transformer와 달리 계층적 구조를 제시하면서 분류뿐만 아니라 object detection, object segmentation에서도 좋은 성능을 낼 수 있게 됨

## Introduction

![다운로드](https://user-images.githubusercontent.com/80622859/186898639-0febd622-c41e-486e-adb9-8bee1e7b3baf.png)

- Input size = (224,224)
- ViT는 각 patch size를 16x16 pixcel로 만든다면 $(224/16)^2=196$ 개의 patch를 가진 상태를 유지하고 각 patch와 나머지 전체 patch에 대한 self attention 수행(Quadratic computational complexity to image size)
- Swin Transformer는 마치 feature pyramid network처럼 작은 patch 4x4에서 시작해서 점점 patch들을 합쳐나가는 방식
- 그림에서 빨간선으로 나누어진 patch들을 window라고 부름
- Swin Transformer는 window내의 patch들끼리만 self attention을 수행(Linear computation complexity to image size)
- 논문에서는 window size(M) = 7x7, 4x4 size의 각 patch가 56x56개 있고 이것을 7x7 size window로 나누어 8x8 window 생성

## Method
- 전체적인 구조

![다운로드 (4)](https://user-images.githubusercontent.com/80622859/186910798-cb2dfb42-88ba-485e-98d6-16d85cb18e65.png)

- 단계
1. Patch Partition
2. Linear Embedding
3. Swin Transformer
4. Path Merging

- 핵심 idea : 오른쪽 그림 (b), swin transformer block, 두 개의 encoder로 구성, MSA(Multi head sef-attention)이 아니라 W-MSA, SW-MAS로 구성
- 1개의 block 당 2개의 encoder가 붙어 있음

### Patch Partition/Patch Merging
- Input image에 patch partition을 할 경우

![다운로드](https://user-images.githubusercontent.com/80622859/187357450-89c38a44-99c4-475a-aac2-a837d98c9e88.png)

- Image에서 한 점은 pixel이지만 patch partition을 하게 되면 한 점은 patch가 됨.
- 각 patch의 pixcel 정보들이 channel이 됨

### Linear Embedding
- Linear layer을 거쳐서 C의 차원으로 만들어줌

### Swin Transformer Block(Shifted Window based Self-Attention)

![다운로드 (1)](https://user-images.githubusercontent.com/80622859/187357762-a7435c43-0253-4ca0-b886-95a0a7a9423b.png)

- MSA가 아니라 Windows-MSA, Shifted Windows-MSA를 사용
- W-MSA는 현재 window에 있는 patch들끼리만 self-attention 연산을 수행. Image는 주변 pixels끼리 서로 연관성이 높기 때문에 window 내에서만 self-attention을 써서 효율적으로 연산량을 줄임
- 하지만 window가 고정되어 있기 때문에 고정된 부분에서만 self-attention을 수행하는 단점이 있어서 저자들은 이 window를 shift해서 self-attention을 한 번더 수행 = SW-MSA

![다운로드 (2)](https://user-images.githubusercontent.com/80622859/187358248-685ea5df-c7da-4146-b546-110a4f2f58c7.png)

- Cycle shift : 먼저 window를 shift(window size//2만큼 우측 하단으로 shift하고 A,B,C 구역을 mask 씌워서 self-attention을 하지 못하도록 함. 그 이유는 원래 A, B, C 구역은 좌상단에 있었기 때문에 반대편에 와서 연산을 하는 것이 의미가 없음
- mask 연산을 한 후 다시 원래 값으로 되돌림(reverse cyclic shift)
- Windows 사이의 연결성을 나타낼 수 있음
- Cycle shift 대신에 padding을 사용할 수 있었지만 이러한 방법은 계산 비용을 증가시키기 때문에 비효율적

### Relative position bias
- ViT와 다르게 처음에 position embedding을 더해주지 않음
- 대신에 self-attention 과정에서 relative position bias를 추가

![render](https://user-images.githubusercontent.com/80622859/187358968-6b98aa8d-526e-4ac1-a778-77e32a802f50.png)

- 기존에 position embedding은 절대좌표를 더함
- Swin-Transformer의 경우에는 상대좌표를 더함.
