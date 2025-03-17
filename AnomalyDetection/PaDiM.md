# PaDiM : a Patch Distribution Modeling Framework for Anomaly Detection and Localization

## 초록

- 영상 내에서 이상을 검출하면서 동시에 위치를 찾아냄
- patch embedding을 위해서 사전 학습된 합성곱 신경망을 사용하고, normal class의 확률적 표현을 얻고자 multivariate Gaussian distribution 활용

## 1. 서론
- 영상 집합에서 이질적이거나 예상하지 못한 pattern을 검출하는 것을 이상 탐지 또는 novelty detection이라고 함
- 제조 공정에서 이상은 매우 드물게 발생. 이를 수동으로 검출하는 것도 힘듦
- Anomaly localization은 각 pixel이나 혹은 pixel들의 각 patch에 이상 점수(anomaly score)를 배정해서 anomaly map을 산출하는 더 복잡한 작업
- 하지만 더 정확하고 해석 할 수 있도록 도와줌
- 이상 탐지는 정상과 비정상 사이의 이진 분류
- 하지만 비정상 예시는 부족하고, 예기치 못한 pattern을 가질 수 있기 때문에 지도 학습 방법은 어려움을 가짐
- 그래서 이상 탐지 모형들은 one-class learning setting을 가짐
- 학습하는 동안  비정상 예시들은 사용할 수 없음. 오직 정상 사진들에 대해서 학습
- 시험 때, normal dataset과 다른 예시들이 비정상으로 분류
- PaDiM의 patch position은 multivariate Gaussian distribution으로 표현
- 사전 학습된 합성곱 신경망의 다른 의미적 계층 간의 상관 관계를 고려

## 2. 관련 연구 
- 크게 재구성 기반이나 embedding similarity-based methods로 분류

### 2.1 재구성 기반 방법(Reconstruction-based methods)
- AE, VAE, GAN은 오직 정상 사진만 복원하도록 학습
- 그래서 비정상은 잘 복원되지 않기 때문에 검출될 수 없음

### 2.2 Embedding similarity-based methods
- 이상 탐지를 위한 전체 사진이나 anomaly localization을 위한 image patch를 묘사하는 meaningful vector를 추출하는 DNN 사용
- 해당 방법은 이상 사진의 어떤 부분이 높은 이상 점수에 대해 기여하는 알 수 없음. 해석이 어려움
- 이상 점수는 reference vector와 시험 사진 간의 embedding vector distance

## 3. Patch Distribution Modeling

### 3.1 Embedding extraction

![image](https://github.com/user-attachments/assets/5346941b-2442-41e0-95bf-967afc9d984a)

- 학습 중에, 정상 사진의 각 patch는 pretrained CNN activation map에서 공간적으로 대응되는 activation vector와 연관
- Fine-grained and global context를 encoding 하기 위해서, 다른 semnatic level과 해상도로부터 정보를 가지고 있는 embedding vector를 얻고자 다른 층들로부터의 activation vector를 이어 붙임
- Activation maps가 입력 사진보다 낮은 해상도를 가지기 때문에 많은 pixel들은 동일한 embedding을 가지게 됨. 또한, 원본 사진 해상도에서 겹치는 부분이 없는 pixel patch를 형성

### 3.2 Learning of the normality
- (i,j)에서 정상 사진 특성을 학습하기 위해, 첫 번째로 N개의 normal training image로부터 (i,j)에서의 patch embedding vector의 집합을 계산
- 이 집합으로부터 얻어지는 정보를 요약하기 위해, $X_{ij}$가 multivariate Gaussian distribution에 의해서 생성되었다는 가정을 만듦.

### 3.3 Inference : computation of the anomaly map
- Test image의 (i,j)에 있는 patch에 대해서 anomaly score를 만들어내고자 Mahalanobis distance를 사용
- Test patch embedding과 학습된 분포 간 거리
- 점수가 높을 수록, anomalous area가 많음

## 4. 실험
- 객체들은 항상 중앙에 있음
- Random rotation(-10, 10) + random crop(224 x 224)
