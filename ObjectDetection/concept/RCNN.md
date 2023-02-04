# Rich featue hierarchies for accurate object detection and semantic segmentation

## Abstract

- mAP(mean Average Precision) : 객체 탐지의 성능을 측정하는 지표
1. 객체 탐지를 위한 영역 제안(region proposal)에 합성곱 신경망 적용
2. 사전 훈련과 미세 조정을 적용해서 train data가 적은 상황에서도 성능을 올림
- 영역 제안과 합성곱 신경망을 결합 => R-CNN(Regions with CNN)
- 영역 제안 : Image 안에서 객체가 있을 만한 후보 영역을 먼저 찾아주는 방법. ex) 선택적 탐색(Selective Search)

## 1. Introduction

- 두 단계(2-stage) 절차를 갖는 구조화된 모형(2-stage detector)
1. 객체 분류(classification)
2. 경계 박스 추정(Bounding-box regression)
- 경계 박스(Bouding-box,bbox) : 객체 위를 표시하는 사각형 box  
- 분류 + 회귀
- 두 가지 문제
1. 합성곱 신경망으로 object localization(객체 위치를 찾는 일)
2. Annotation된 data가 부족한 상태에서 모형을 학습해야 하는 문제

### 1. CNN으로 object localization하는 문제

- 객체 탐지는 객체를 분류하는 일뿐만 아니라 객체의 위치 좌표까지를 찾아야 함
- Object localization을 위한 세 가지 접근
1. Localization은 일종의 회귀 문제 => 실효성이 떨어짐
2. Sliding-Window Detector 사용 => 합성곱 신경망을 사용하기 때문에 window와 strdie의 크기가 커지게 되는데 이는 localization을 오히려 어렵게 함
3. 영역 제안(Region proposals) => 객체 탐지와 분할에서 모두 효과
- 영역 제안 절차

![image](https://user-images.githubusercontent.com/80622859/216748762-8cc4b053-6a39-4660-8ca4-bdf269c7d42d.png)

1. Input image
2. 2,000개의 후보 영역 제안
3. 합성곱 신경망을 이용해 각 후보 영역에서 feature 연산. 이에 앞서 후보 영역을 일정한 크기로 조정(warped region). 합성곱 신경망 특성 상 input data shape이 고정되어야 함
4. 합성곱 신경망 마지막 단계인 전결합 계층을 feature라고 간주하고, SVM을 이용해 각 영역에 대한 분류 작업 수행

### 2. Annotation된 data가 부족한 상태에서 모형을 학습해야 하는 문제

- 사전 훈련 및 미세 조정
- mAP가 8% 개선

## 2. Object detection with R-CNN

- Three module
1. Class별로 영역을 제안 -> 이렇게 제안한 후보 영역을 바탕으로 객체 찾음
2. 합성곱 신경망 -> 후보 영역에서 크기가 고정된 feature 추출
3. SVM

### 2.1 Module design

- 영역 제안 : 선택적 탐색(비슷한 영역을 합쳐나가면서 후보 영역을 제안)

![image](https://user-images.githubusercontent.com/80622859/216748941-7e7455a6-ed82-469c-a9ae-c2f9f3da7380.png)

- Feature extration : AlexNet을 활용해 제안된 각 후보 영역별로 feature, 4096개를 추출. 이렇게 추출한 feature를 기반으로 SVM이 최종 분류 작업 수행
- AlexNet 구조

![image](https://user-images.githubusercontent.com/80622859/216748976-17a25982-0653-4461-b606-994cc1cfff1f.png)

- 제안된 후보 영역에서 feature extraction을 위해서 후보 영역의 크기를 고정시켜야 함(warping)
- 227 x 227
- Warping 하기 전에, 후보 영역 주변 배경을 조금 살림.
- 16 pixel만큼 주변 배경을 살리면 성능이 가장 좋음(Warping with context padding 16 pixels)

- R-CNN architecture

![image](https://user-images.githubusercontent.com/80622859/216749038-6d39b90e-1334-4c3f-a66c-baba9f8286d1.png)

### 2.2 Test-time detection

- SVM을 통해 각 class 별로 점수를 계산
- 점수에 따라 비 최대 억제(Non-Maximum Suppression, NMS)를 수행
- 비 최대 억제 : bbox 
- 점수가 높은 후보 영역 경계 박스를 기준으로 IoU가 특정 임계값을 넘는 다른 경계 박스는 모두 제거
