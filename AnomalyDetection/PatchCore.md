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

