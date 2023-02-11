# Semantic Image Segmentation with Deep Convolutional Nets and Fully connected CRFs

## 1. Introduction

- Deep Convolutional Nerual Networks(DCNNs)는 분류, 객체 탐지 등의 전반적인 CV 분야에서 좋은 영향
- 하지만 segmentation에서는 성능이 좋지 않았음
- DCNN을 

- Semantic segmentation에서 높은 성능을 내기 위해서는 합성곱 신경망의 마지막에 존재하는 한 pixel이 입력값에서 어느 크기의 영역을 cover할 수 있는지에 대한 receptive field 크기가 중요하게 작용
- Pooling을 dilated convolution으로 parameter의 수를 유지하며 해상도가 줄어드는 것을 막음
- 기존 합성곱과 동일한 양의 parameter와 계산량을 유지하면서도, field of view(한 pixel이 볼 수 있는 영역)를 크게 가져감
- DCNN을 semantic segmentation에 적용할 때 문제점
1. Reduced feature resolution
2. Existence of objects at multiple scales
3. Reduced localization accuracy due to DCNN invariance

- Deeplab에서 제안한 3가지 해결 방안

1. Max pooling 및 downsampling 시 spatial resoltion의 feature map 출력. Atrous convolution 사용
2. Atrous Spatial Pyramid Pooling(ASPP)
3. CRF

- 속도, 정확도, 간결성이라는 3가지 장점 

## 2. Related Work

- Semantic segmentation에서 사용된 DCNN의 3가지 기법

1. Bottom up segmentation 및 DCNN 기반의 region classification

- 하나의 객체 안에 여러 segmentation을 만들어 그것들을 합침
- 오류가 발생하면 해결할 수 없음

![image](https://user-images.githubusercontent.com/80622859/218249292-c071ac57-503f-4ea6-99f0-1000d72ed970.png)

2. Image labeling에 사용된 DCNN feature들과 독립적으로 얻은 segmentation을 결합
3. DCNN을 사용하여 category-label pixel label을 추출 -> 이 방식 채택

## 3. Method
 
