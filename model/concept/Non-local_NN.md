# Non-local Neural Networks

## 초록
- 합성곱 신경망과 순환 신경망이 한 번에 국소적인 이웃만 처리하는 한계를 넘기 위해, 특정 위치의 응답을 모든 위치의 특징들의 가중합으로 계산하는 non-local 연산 제안 
- Self-Attention은 고전 영상 처리 기법인 non-local means를 확장한 특수한 형태

## 1. 서론
- 여러 층을 거쳐 신호를 전달하면 계산 비용이 비효율적. 최적화가 어려워짐. 멀리 떨어진 위치 간의 즉각적인 정보 교환이 힘듦
- 본 논문은 단 한 번의 연산으로 전체 영상 내 모든 위치의 특징을 직접 비교하고 합산하는 module 고안

## 2. 방법

### 2-1. Generic Non-local Operation
- DL에서 일반적인 non-local은 다음과 같이 정의

$$y_i=\frac{1}{C(x)}\sum_{\forall j} f(x_i, x_j)g(x_j)$$

- i : 출력을 계산하고자 하는 기준 위치 식별자
- j : 가능한 모든 위치를 순회하는 식별자
- x, y : Input feature map and output feature map(크기가 동일)
- $f(x_i, x_j)$ : 위치 i와 j 사이의 유사도를 계산하는 scalar function. Scalar function : 여러 입력값을 받아, 단 하나의 숫자를 내뱉는 함수
- $g(x_i)$ : 위치 j의 입력 특징을 선형 변환하는 함수. $g(x_i)=W_g x_j$, 1 x 1 또는 1 x 1 x 1 합성곱으로 구현
- C(x) : 가중치 합을 맞춰주기 위한 정규화 계수

#### 완전 연결 계층과 차이
- 완전 연결 층도 모든 위치를 연결하지만, 학습된 고정된 가중치를 사용하며 입력 크기가 고정되어야 하고 위치 정보가 사라짐
- Non-Local은 두 입력 특징 간의 유사도에 따라 가중치가 동적으로 결정. 가변적인 입력 크기를 그대로 유지

### 2-2. 유사도 함수의 4가지 구현 방식
- 유사도를 어떻게 정의하냐에 따라 변형이 존재. 어떤 형태를 쓰든 non-local 연산 자체의 유무가 성능에 훨씬 더 중요|ㅊ
- $\theta(x_i)=W_{\theta} x_i$, $\phi(x_j)=W_{\phi} x_j$

|구현 방식|유사도 수식|정규화 계수|특징|
|-----|------|-----|--|
|Gaussian|$e^{x^T_i x_j}$|$\sum_{\forall j} f(x_i, x_j)$|별도 embedding 없이 원본 특징 내적에 지수 함수 적용|
|Embedded Gaussian|$e^{\theta(x_i)^T \phi(x_j)}$|$\sum_{\forall j} f(x_i, x_j)$|Transformer의 self-attention과 정확히 동일)|
|Dot product|$\theta(x_i)^T \phi(x_j)$|N(전체 위치 개수)|Softmax 없이 단순 내적 후 위치 개수 N으로 나눔|
|Concatenation|$ReLU(w^T_f[\theta(x_i),\phi(x_j)])$|N|두 특징을 이어 붙인 뒤 선형 층과 ReLU 통과(Relation network)|




