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
