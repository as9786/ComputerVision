# Towards Total Recall in Industrial Anomaly Detection

## 초록
- Cold-start problem을 해결
- 재현율을 최대화하는게 목표
- Nomial patch feature를 대표하는 memory bank 사용

## 1. 서론
- 적은 양의 nominal data만 보고서도 이상 팀지 및 localization을 잘 수행해내는 것
- 보통 out-of-distribution detection 문제로 이상 탐지 문제를 해결하는데 결함이 매우 미세한 차이일 수 있음

![image](https://github.com/user-attachments/assets/c14d84c8-5eff-4ee7-8e31-d190de6ec00d)

- 주황샌 선 : Anomaly contour
- 정상 분포를 학습함으로써 이상 탐지를 하는 방법 : AutoEncoder, GAN etc\
- 정상 분포에 적응하지 않고 ImageNet classification에서의 feature를 활용하는 방법 => 성능이 좋게 나옴
-  여러 크기의 특징 표현을 활용한 시험 표본과 정상 표본 간의 feature matching
-  미세한 결함 분할은 고해상도 상에서 이뤄지는 반면, 전체적인 이상 탐지는 추상적인 단계에서 이뤄짐
-  PatchCore는 ImageNet class bias를 줄임
-  특정 patch만 이상으로 구분될 경우, 바로 비정상으로 구분.
-  중간 단계의 network patch feature를 사용함으로써, 고해상도에서의 ImageNet bias를 최소화
-  지역적으로 이웃한 특징을 함께 고려함으로써 충분한 spatial context를 보유
-  실용성을 위해 nominal feature bank를 위한 greedy coreset subsampling 제안 -> 추출된 patch level memory bank의 중복성을 줄여주고, storage memory와 추론 시간을 줄여줌

![image](https://github.com/user-attachments/assets/54390ab4-d83b-44a4-909f-aa9192b8d9ec)

- 정상 표본들은 neighbourhood-aware patch level feature로서 memory bank 안에 포함
- 추론 시간을 줄이기 위해 greedy coreset subsampling을 통해 memory bank downsampling

## 2. 관련 연구 

- PatchCore에 사용된 요소들은 SPADE와 PaDiM과 유사

### SPADE
- Pretrained backhone으로부터 추출된 nominal feature의 memory bank 사용
- Image-level and pixel-level 각각에 대해 분리된 접근 방식 사용
- 다양한 특징 계층으로 구성된 memory bank를 활용해 KNN 기반의 이상 분할과 image level anomaly detection 수행

## 3. 방법

### 3.1. Locally aware patch features
- Memory bank M 사용
- 학습 과정에서 생성된 mid level feature representation으로 구성된 patch level feature들로 이뤄짐. ImageNet에 대한 편향 줄임
- 주변의 patch 정보를 포함할 수 있도록 아래와 같이 식 계산
- Neighbor patch

![image](https://github.com/user-attachments/assets/0eca3d45-d1c5-4dbb-802b-86361cfe620f)

- (h,w)에서의 locally aware feature 계산식

![image](https://github.com/user-attachments/assets/a31c4e38-34b9-4877-bc44-682464135e8d)

- $f_{agg}$는 주변의 feature vector 정보를 합쳐주는 함수
- PatchCore에서는 adaptive average pooling 사용
- 각 feature map에 대한 local smoothing의 효과
- (h, w) 쌍 각각에 대해 해당 위치에 대응되는 하나의 d 차원의 single representation이 결과로 나옴
- 여러 계층의 특징들을 사용하는 것이 성능이 좋음
- 사용된 특징의 공간적 해상도와 일반성을 유지하기 위해 중간의 두 특징 계층만을 사용

![image](https://github.com/user-attachments/assets/1b7f69ff-264e-4598-8d48-4caaf3a07636)

- 보간법을 통해 j+1 feature map을 j번째와 합쳐줌

### 3.2. Coreset-reduced patch-feature memory bank
- Training data가 커짐에 따라 memory bank M도 매우 커짐
- M이 large image size와 count를 찾을 수 있도록 함
- 논문에서는 coreset subsampling mechanism 제안
- Coreset selection time을 줄이기 위해 iterative greedy approximation 사용

### 3.3. Anomaly Detection with PatchCore
- image level anomaly score 예측
- Distance score 중 최댓값ㅇ르 anomaly score로 가짐
- 



