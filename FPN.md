# Feature Pyramid Networks for Object Detection
- Computing resource를 적게 차지하면서 다양한 크기의 객체를 인식하는 방식
- Faster R-CNN과 결합하여 학습

## Preview

![다운로드 (1)](https://user-images.githubusercontent.com/80622859/186900246-dc1813eb-9435-4035-8dae-e7c453dda4a1.png)

- 원본 image를 합성곱 신경망에 입력하여 forward pass를 수행하고, 각 stage마다 서로 다른 scale을 가지는 4개의 feature map을 추출(Bottom-up pathway)
- 이후 Top-down pathway를 통해 각 feature map에 1x1 합성곱 연산을 적용하여 모두 256 channel을 가지도록 조정하고 upsampling을 수행
- 마지막으로 Lateral connection 과정을 통해 pyramid level 바로 아래 있는 feature map과 element-wise addition(요소별 덧셈) 연산 수행
- 이를 통해 얻은 4개의 서로 다른 feature map에 3x3 합성곱 연산을 적용

### forward pass
- 각 filter를 입력 volume의 가로/세로 차원으로 합성곱시키며 2차원의 activation map을 생성하는 것
### upsampling
- 축소된 feature map을 원본 image 크기로 되돌리기 위해 사용되는 방식
- Downsampling : Conv 층과 pooling 층을 통과시키면서 원본 image를 압축해나가는 과정
- Upsampling : Downsampling과 반대로 크기를 늘려나가는 

## Main Ideas

### Pyramids란?

![다운로드 (2)](https://user-images.githubusercontent.com/80622859/186902214-f6fde689-12ab-4ea1-b9ca-46b91c872361.png)

- 합성곱 신경망에서 얻을 수 있는 서로 다른 해상도의 feature map을 쌓아올린 형태
- Level : 피라미드의 각 층에 해당하는 feature map
- 합성곱 신경망에서 입력층에 가까울 수록 높은 해상도(high resolution)의 feature map을 가짐 => 가장자리, 곡선 등과 같은 저수준 특징(low-level feature)을 보유
- 반대의 경우에는 질감과 물체의 일부분 등 class를 추론할 수 있는 고수준 특징(high-level feature)을 가지고 있음
- Object detection 시 각 level의 feature map을 일부 혹은 전부 사용하요 예측 수행

## Feature Pyramid Network

![다운로드 (3)](https://user-images.githubusercontent.com/80622859/186902783-efc9d3da-956d-4f46-9316-0667c64e0dce.png)

- 임의의 크기의 single-scale image를 합성곱 신경망에 입력하여 다양한 scale의 feature map을 출력하는 신경망(논문에서는 ResNet 사용)
- 
