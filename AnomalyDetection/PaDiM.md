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
