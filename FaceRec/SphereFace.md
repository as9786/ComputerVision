# SphereFace: Deep Hypershpere Embedding for Face Recognition

## 초록
- 얼굴 인식에서는 같은 사람의 최대 거리가 다른 사람의 최소 거리보다 작아야 하는 강한 구별력이 요구됨
- 합성곱 신경망이 각도 구별력을 학습할 수 있도록 A-Softmax(Angular Softmax) loss 제안
- 가중치 정규화를 통해 특징들이 초구면 다양체 위에 분포하도록 기하학적 제약 부여
- Angle margin parameter m을 통해 결정 경계의 크기를 정량적으로 조절

## 1. 서론
- 폐쇄형(Closed-Set) 분류 문제와 달리 얼굴 인식은 학습 때 보지 못한 새로운 인물의 얼굴을 구분해야 하는 open-set 문제
- 기존 손실 함수의 한계점
    - Softmax : 결정 경계가 가중치의 크기와 각도에 영향을 받아 class 간 여백이 없고 각도 공간에서의 구별력이 부족
    - 삼중항/대조 : Training set pair 구성이 어렵고 기존 softmax와 결합할 때 기하학적 공간 불일치 발생(Euclidean vs inner dot)
- 본 논문은 마지막 완전 연결 계층의 내적 연산을 각도 공간으로 재해석. 각도에 직접 곱셈 마진을 부여하는 A-Softmax loss를 통해 문제 해결

## 2. 방법
- 잔차 연결을 활용한 64개 층의 합성곱 신경망
- 가중치 정규화와 편향 제거를 통해 분류 기준을 순수한 각도로 바꿈. Ground truth class angle에 정수 m을 곱해 더 엄격한 angle margin 형성

### 2-1. Modified softmax
- x가 주어졌을 때, softmax 이진 분류에서 class 1과 class 2로 분류될 확률을 $p1,  p2$라고 하자
- $p_1 = \frac{e^{W_1^T x+b_1}}{e^{W_1^T x+b_1}+e^{W_2^T x+b_2}}, \ p_2 = \frac{e^{W_2^T x+b_2}}{e^{W_1^T x+b_1}+e^{W_2^T x+b_2}}$
- $p_1 > p_2$ => Class 1, $p_1 < p_2$ => Class 2
- 결정 경계 : $p_1 = p_2$. 분모가 같으므로 분자가 같으면 됨
- $e^{W_1^T x+b_1} = e^{W_2^T x+b_2}$
- $W_1^T x + b_1 = W_2^T x + b_2$ (자연로그)
- 이진 분류 기준 기존 softmax decision boundary : $(W_1 - W_2)x + b_1 - b_2=0$
- 내적 공식($‖W‖‖x‖cos \theta = W_i^Tx$)으로 풀면 가중치 크기와 편향이 개입. ‖W₁‖‖x‖cos θ₁ + b₁ = ‖W₂‖‖x‖cos θ₂ + b₂
- Weight vector를 L2 normalization(‖Wᵢ‖ = 1)하고, 편향 제거(bᵢ = 0)
- 결정 경계가 $cos \theta_1 = cos \theta_2$로 단순화되어 오직 weight vector와 feature vector 사이의 각도만으로 분류 수행
- 여전히 결정 경계가 하나뿐이어서 class 간 margin이 존재하지 않음

### 2-2. A-Softmax(Angular Softmax) Loss
- Class 간 angle margin을 강제하기 위해 정답 class의 각도 $\theta_1$에 정수 m(m ≥ 1)을 곱함
- Class 1로 분류되기 위한 조건  : $cos(m \theta_1) > cos(\theta_2)$ (즉, $\theta_1 < \frac{\theta_2}{m}$이 되어야 하므로 다른 class보다 m배 더 가까워야 정답으로 인정

#### 비단조성 문제
- 비단조 함수는 최적화에 사용할 수 없음
- 전 구간에서 단조 감소하는 조각별 함수(piecewise funtion) ψ(θ)로 대체

<img width="531" height="60" alt="image" src="https://github.com/user-attachments/assets/8c452581-102d-498a-8b2b-f384563da9ee" />

- 학습 안정화 기법 : 기존 Softmax 수식과 가중합 형태로 구성하고, 가중치 매개변수 $\lambda$를 점진적으로 줄여나가는 방식으로 안정적인 수렴 유도

### 2-3. 기하학적 해석
- 가중치를 정규화하고 각도 마진을 주면, 학습된 feature vector들이 원점에서 뻗어나오는 원뿔 형태로 군집화됨
- 이를 구의 표면으로 투영하면 초구면 위에서 같은 인물의 특징점들은 좁은 영역에 모임

## 3. 평가
### 3-1. m 효과
- m이 커질수록 class 내 응집력이 강해짐
- m=4일 떄, 최고 성능
