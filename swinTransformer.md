# Swin Transformer: Hierarchical Vision Transformer using Shifted Windows
- ViT는 모든 patch가 self attention을 함으로 계산 비용이 크게 발생

-> 각 patch를 window로 나누어 해당 window 안에서만 self attention을 수행하고 그 window를 한 번 shift한 후에 다시 self attention을 하는 구조 제시
- 일반적인 Transformer와 달리 계층적 구조를 제시하면서 분류뿐만 아니라 object detection, object segmentation에서도 좋은 성능을 낼 수 있게 됨

## Introduction

![다운로드](https://user-images.githubusercontent.com/80622859/186898639-0febd622-c41e-486e-adb9-8bee1e7b3baf.png)

- Input size = (224,224)
- ViT는 각 patch size를 16x16 pixcel로 만든다면 $(224/16)^2=196$ 개의 patch를 가진 상태를 유지하고 각 patch와 나머지 전체 patch에 대한 self attention 수행(Quadratic computational complexity to image size)
- Swin Transformer는 마치 feature pyramid network처럼 작은 patch 4x4에서 시작해서 점점 patch들을 합쳐나가는 방식
