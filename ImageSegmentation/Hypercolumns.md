# Hypercolumns for Object Segmentation and Fine-grained Localization

## Abstract

- 합성곱 신경망의 마지막 층은 너무 coarse해서 정확한 영역을 잡기 힘듦
- 한편에, 앞 쪽 신경망은 지역은 잘 잡지만 의미적인 부분을 잘 잡지 못함
- 두 개의 특징을 모두 포착하기 위해, 한 pixel의 hypercolumn을 그 pixel 위에 있는 모든 합성곱 신경망 단위의 activation vector로 정의
- Hypercolumn을 pixel descriptor로 사용. 세 가지의 fine-grained localization 작업
- Simultaneous detection, segmentation, part labeling

## 1. 서론
- 합성곱 신경망의 마지막 층은 우리가 알고자 하는 객체의 가장 많은 정보를 지니고 있다고 알려져 있음
- 하지만 항상 그 층이 최적의 표현이 아닐 수도 있음
- 다양한 추상화와 크기가 필요
- Multiscale strategy is neccessary
- 우리가 관심 있는 정보는 합성곱 신경망 전역에 퍼져 있음
- 주어진 입력 위치의 hypercolumn을 합성곱 신경망의 모든 계층에서 해당 위치 위에 있는 모든 단위의 출력으로 정의 후 하나의 vector로 쌓음
- 하지만 가까이 위치한 층은 서로 높은 상관 관계를 지니기 때문에 표본 추출을 통해서 측정

![image](https://github.com/as9786/ComputerVision/assets/80622859/ef94f179-9886-44f7-89f5-7b31f812ff2e)

- 하지만 두 가지 문제가 존재
1. 사진에서 객체 범주의 모든 instance를 감지하고 분할하는 것을 목표로 하는 동시 탐지 및 분할
2. 객체를 탐지하고 해당 부분을 localization

- 1 번 문제는 keypoint를 찾고, 2번 문제는 각 부분을 분할하여서 해결
- Pixel classification으로 framing하고 hypercolumn을 pixel descriptor로 사용하여 이러한 작업과 다른 세분화된 지역 작업을 처리하기 위한 일반적인 framework 제시
- 해당 방법은 신경망을 사용하여 종단 학습 가능


## 2. 관련 연구

### Combining featurea across multiple levels

-  Laplacian pyramid
-  Edge orientation, 곡률 등을 추정하기위해 특정 차수까지의 부분 도함수인 jet 사용
-  Texture 구분을 위해 a bank of filters의 출력 사용
-  A bank of filter는 여러 크기를 포함하지만 여전히 단순한 선형 필터인 반면, hypercolumn representation의 많은 기능은 비선형적 함수
-  합성곱 신경망도 multiple levels의 추상적 표현과 크기를 결합
-  해당 논문에서는 하위 층의 해상도를 유지하고 높은 층을 표본 추출하여 결합

## 3. Pixel classification using hypercolumns

### Problem setting
- Object detection system은 여러 집합의 탐지들을 제공한다고 가정
- 각 탐지들은 category label과 점수가 있는 경계 상자로 제공
- 이러한 탐지들은 이미 비 최대 억제를 수행한 것으로 가정
- 모든 탐지에 대해 객체를 분할하거나, keypoints를 예측
- 각 작업에 대해 탐지의 경계 상자를 약간 확장하고 확장된 상자에서 heatmap을 예측
- Heatmap이 encoding하는 정보의 유형은 특정 작업에 따라 다름
- 분할의 경우, heatmap은 특정 위치가 객체 내부에 있을 확률
- Part labeling의 경우 각 part에 대해 별도의 heatpmap을 예측하며, 각 heatmap은 해당 위차가 해당 부분에 속할 확률을 나타냄
- Keypoint prediction의 경우에도 각 keypoint에 대해 별도의 heatmap을 출력하여, 각 heatmap은 keypoint가 특정 위치에 있을 확률
- 각각의 경우 50 x 50 heatmap을 예측하여 확장된 경계 상자의 크기에 맞게 크기를 조정하고 사진에 표시

 ### Computing the hypercolumn representation
 - 경계 상자를 잘라서 고정된 크기로 조정하고 합성곱 신경망에 입력
 - 합성곱 신경망의 모든 중간 출력들은 feature map
