# Gradient-Based Learning Applied to Document Recognition

## 1. Introduction
- 사람이 일일이 설계한 특징들보다 자동화된 학습에 의존하는 것이 pattern recognition에 더욱 효과적
- 두 가지 인식 방법
1. Character recognition : 독립된 하나의 글자를 인식. ex) CNN
2. Document understanding : 여러 개의 글자가 모인 문장, 여러 문장이 모인 문서를 이해하는 과정 ex) Graph Transformer Networks
- Existing pattern recognition system

![캡처](https://user-images.githubusercontent.com/80622859/192315428-85fc105a-b92e-44c8-b153-771060688eee.PNG)

- Feature extractor : 입력값을 저차원의 vector로 변환. 이러한 형태는 쉽게 matching되고, class가 바뀌지 않는 선에서 변형이 강함
- Feature extractor는 사전 지식이 어느 정도 필요하며 수작업을 설계되기 때문에 시간 소요가 높음
- Trainable classifier : 보편적이고 학습 가능
- 다른 문제마다 새로운 feature extractor를 설계해야 하기 때문에 비효율적

- 아래의 3가지 요인으로 학습기의 성능 개선이 가능
1. 컴퓨터 성능의 향상으로 brute-force 계산 방법이 가능
2. Data의 크기 증가
3. 고차원의 입력을 다룰 수 있고 복잡한 결정을 내릴 수 있는 기계학습 등장. ex) 역전 오차파로 학습된 multi-layered neural networks

### A. Learning from Data
- Gradient-based learning
- 기계는 다음과 함수를 계산

![다운로드](https://user-images.githubusercontent.com/80622859/192316747-9ba83ad6-cdba-4c62-9c14-51d0ce8cea43.png)

- $Z^p$ : 입력값, W : 조절가능한 매개변수, $Y^p$ : $Z^p$에 대해 예측한 class의 label이거나 각각의 class에 관련된 확률
- 손실함수

![다운로드 (1)](https://user-images.githubusercontent.com/80622859/192317019-bb11b204-3027-4eee-810d-75623e87159d.png)

- $D^p$ : p번째 입력값의 실제 label
- 실제 label과 기계가 출력하는 값의 불일치를 측정
- 평균 손실함수 : $E_{train}(W)$
- 학습 과정에서 평균 손실함수를 가장 작게 만드는 W를 찾아야 함
- 하지만 중요한 것은 train data가 아니라 test data에 대해서 오차를 줄여야 함
- $E_{test}$와 $E_{train}$의 관계는 다음 식에 근접

![다운로드 (2)](https://user-images.githubusercontent.com/80622859/192317870-f66411af-417a-4bb3-9853-7f1f38bf1649.png)

- P : data size, h : 기계의 복잡도, $\alpha$ : 0.5 ~ 1 사이의 수
- Train data의 크기가 커지고 기계가 단순해진다면 train data에서의 오차와 test data에서의 오차의 차이가 줄어듬
- h가 증가하면 $E_{train}$이 감소 -> $E_{train}$와 $E_{test}$ 사이의 차이는 증가
- Structural risk minimization : $E_{train}$을 최소화시키는 방법

![다운로드 (3)](https://user-images.githubusercontent.com/80622859/192318426-f94a5eb3-0042-4751-b3cc-0c4da57765a3.png)

- H(W) : 규제화, $\beta$ : 상수

### B. Gradient-Based Learning






