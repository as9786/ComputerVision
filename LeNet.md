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
- 손실함수를 최소화하기 위해 현재 매개변수의 경사를 이용

![다운로드 (4)](https://user-images.githubusercontent.com/80622859/192319209-055273e0-1f22-4c66-aa82-ef29ae8fa6b7.png)

- W : 실수의 매개변수 집합, E(W)는 연속적이고 미분 가능, $\epsilon$ : scalar
- 대중적인 최적화 과정은 online update라고 불리기도 하는 stochastic gradient

![다운로드 (5)](https://user-images.githubusercontent.com/80622859/192319970-a4095da8-ce8e-4148-8227-04bb54896d3f.png)

#### 확률적 경사하강법
- 추출된 data 한 개에 대해서 경사를 계산하고, 경사하강법을 적용하는 방법
- 전체 data를 사용하는 것이 아니라, 무작위로 추출한 일부 data를 사용하는 것
- 학습 중간 과정에서 결과의 진폭이 크고 불안정하며, 속도가 매우 빠름

### C. Gradient Back-Propagation
- 경사를 활용한 학습 1950년대부터 소개되었지만 선형 모형에 한정되어 사용
- 아래의 3가지 이유로 기계학습에서도 사용
1. 손실함수의 local minima문제는 실제로 큰 문제가 아니라는 점. 
2. 오차 역전파가 비선형 모형에서도 대중화
3. 오차 역전파 과정이 sigmoid 함수를 통해서 MLP에 적용되면 복잡한 기계학습 과업을 해결 가능

### D. Learning in Real Handwriting Recognition Systems
- 합성곱 활용
- Heuristic한 방법을 통해서 글자를 분리
- 그리고 학습기에 의해 후보들 중 가장 높은 점수를 낸 조합 채택
- 하지만 이럴 경우 비용이 많이 들고 어려움
- 논문에서는 Section V와 같은 GTN 방법 사용

### E. Globally Trainable Systems
- 손실함수의 미분 가능함을 보장하기 위해 feed-forward network로 전반적인 system 구성

![다운로드 (6)](https://user-images.githubusercontent.com/80622859/192321494-4993b81c-b64c-4cc8-b920-00441d4966f6.png)

- $X_n$ : 출력값, $W_n$ : 매개변수
- $X_0$는 model의 첫 입력이며 $Z^p$와 같음
- System 전체의 손실함수를 각각 편미분한 것은 아래와 같음

![다운로드 (7)](https://user-images.githubusercontent.com/80622859/192321774-9e1813e0-f389-4339-b383-5bfd41cc5422.png)

## 2. Convoultional Neural Networks for Isolated Character Recognition
- Image는 크기가 크기 때문에 많은 매개변수들이 필요로 하고, 많은 매개변수를 학습시키기 위해 더 많은 data를 요구
- 가장 큰 결점은 input data에 약간의 왜곡만 취해도 아주 다른 data라고 인식

### A. Convolutional Networks
- LeNet-5 구조

![다운로드 (8)](https://user-images.githubusercontent.com/80622859/192322204-3aa0df0b-913e-43f0-af5b-a91995537120.png)

- Input은 정규화되고, centered된 image를 받음
- 층의 각각의 unit은 이전 층의 근처에 위치한 unit들에서 입력을 받아옴(local receptive fields) => 가장자리, 모서리와 같은 저차원의 시각적 특징을 추출할 수 있게 됨
- 위와 같은 특징들을 하위의 층들에서 조합하여 고차원의 시각적 특징을 감지할 수 있게 됨
- 저차원의 시각적 특징도 전체적으로 유의미한 특징이기 때문에 image에 왜곡이 주어져도 같은 가중치를 갖게 됨
- 이러한 출력들을 feature map이라고 부름
- Feature map의 unit들은 image의 다른 부분에서도 같은 연산을 하도록 제한
- C1 : 6개의 feature map, feature map의 unit은 5x5 filter => 26개 parameters
- 각각의 feature map은 서로 다른 가중치를 가지면 서로 다른 local feature를 추출
- 입력에 변환을 줘도 출력이 똑같이 변환되기 때문에 기존의 출력과 같은 값을 얻게 된다는 장점이 있음
- Sub-sampling-layer(Pooling) : 2x2 filter, 인접한 unit들 간의 중복을 허용하지 않음. feature map의 크기를 줄임
- Sub-sampling-layer에서 줄어든 만큼 합성곱층에서 feature map의 수가 늘어나는 것을 반복

### B. LeNet-5
- 7개의 층, 입력 크기 : 32 x 32
- Output layer는 euclidean radial basis function(RBF)로 구성

![다운로드 (9)](https://user-images.githubusercontent.com/80622859/192323768-41cf9f2a-5fa5-49bf-8707-7a174c8e4a8e.png)

### C. Loss Function
- MLE

![다운로드 (10)](https://user-images.githubusercontent.com/80622859/192323889-014460d7-a480-4766-a45b-0b1b8e9928db.png)

- $y_(D_p)$ : $D_p$번째 RBF unit의 출력
- 두 가지 결점
1. RBF의 매개변수들을 학습시키면 E(W)가 매우 작아지나, RBF의 모든 매개변수 vector는 동일하기 때문에 결국 신경망의 입력은 무시한 채 모든 RBF의 출력이 0이 됨
2. Class 간의 경쟁이 없음

