# CosFace: Large Margin Cosine Loss for Deep Face Recognition

## 초록
- 깊은 합성곱 신경망 기반 얼굴 인식에서 손실 함수 개선을 통해 특징 구별 능력 극대화
- Softmax loss -> Cosine loss. L2 normalization
- LMCL(Large Margin Cosine Loss) : Cosine space에서 decision margin을 최대화하기 위해 cosine margin 항 m을 도입
- Minimize intra-Class variance, Maximize inter-class variance

## 1. 서론
- 얼굴 인식은 크게 검증(1:1)과 식별(1:N)으로 나뉨
- 기존 방법론 한계
    - Softmax loss : Open-set 얼굴 인식을 위한 특징 구별력이 부족
    - Triplet loss : 가능한 삼중항의 조합이 기하급수적으로 증가해 수렴이 느림
    - SphereFace(A-Softmax) : Cosine function의 비단조성으로 인해 최적화가 불안정하고 초매개변수 조정이 어려움
- 본 논문은 특징과 가중치를 정규화하고 cosine space에서 직접 margin을 빼주는 방식을 통해 학습이 안정적이고 구별력이 뛰어남

## 2. 방법
- 64개의 층으로 이뤄진 합성곱 신경망(SphereFace와 동일한 잔차 신경망 기반 backbone) 
- 구면 공간에 특징을 투영한 뒤, cosine similarity 기반으로 class margin을 강제하여 결정 경계를 더욱 엄격하게
### 2-1. LMCL(Large Margin Cosine Loss)

- Softmax : 크기와 각도가 모두 결정 경계에 영향을 주어 각도 공간에서의 순수한 분리력이 떨어짐
- Normalized Softmax Loss(NSL)
    - Weight vector를 L2 정규화. Feature vector를 특정 크기로 고정
    - 크기 변동을 제거하여 오직 각도에 의존. 여전히 class 간 여백이 없어 충분히 밀집 X
- LMCL
    - Cosine space에서 직접 고정된 여백 m($m \geq 0$)을 빼주어 정답 클래스에 대해 더 엄격한 기준 적용
    - 정답 클래스 $y_i$에 대한 조건 : $cos(\theta_{y_i}) - m > cos(\theta_j)$ (다른 클래스 j보다 m만큼 더 커야 정답으로 인정)
    - $L_{lmc} = \frac{1}{N} \sum_i -\log \frac{e^{s(\cos(\theta_{y_i, i}) - m)}}{e^{s(\cos(\theta_{y_i, i}) - m)} + \sum_{j \neq y_i} e^{s\cos(\theta_{j, i})}}$
    - 초매개변수 s (구의 반지름)는 주어진 m에 따라 하한선 이상으로 충분히 크게 설정해야 학습이 원할
 
### 2-2. 다른 손실 함수와 비교 
- Softmax : ‖W₁‖cos θ₁ = ‖W₂‖cos θ₂ (가중치 크기에 따라 경계가 왜곡됨)
- NSL : $cos_{\theta_1} = cos_{\theta_2}$ (결정 경계가 하나여서 경계 부근의 모호한 표본 구분에 취약)
- A-Softmax : $cos(m\theta_1)=cos\theta_2$ (각도에 m을 곱하므로 $\theta$가 작아질수록 여백이 0에 수렴하여 여백 효과가 일관되지 않음)
- LMCL : $cos\theta_1 - m = cos \theta_2$ (Cosine space에서 모든 각도에 대해 일정한 여백을 보장하며, 미분이 간단해 최적화가 쉬움)

### 2-3. 특징 정규화의 중요성
- 가중치만 정규화하고 feature vector를 정규화하지 않으면, 신경망이 각도를 줄이는 대신 단순히 쉬운 표본의 특징 크기를 키우는 방식으로 손실을 줄이게 됨
- Softmax는 두 벡터의 내적인 $W^T x = ‖W‖ ‖x‖ cos θ$ 값을 최대화하도록 학습
- ‖x‖을 정규화하지 않을 시 손실을 줄이기 위해 각도를 좁혀서 $cos\theta$를 키우는 것보다, 구분하기 쉬운 사진의 특징 길이를 엄청나게 키워버리는 것이 쉬움
- 따라서 x와 W를 모두 정규화하고 고정 크기 s를 곱해주어야 모든 특징이 초구면 위에 분포하며 오직 cosine similarity만으로 군집화됨
- 기하학적으로 원점에서 출발하는 모든 vector length를 똑같이 s로 맞추면 2차원에서는 원, 3차원에서는 구가 됨
- 4차원 이상의 고차원 공간에서 반지름이 s인 구의 표면을 초구면이라고 부름
- s를 곱해주지 않으면 $cos\theta$는 -1에서 1 사이의 아주 작은 값만 갖게 됨
- 공간이 너무 좁아서 data들이 들어갈 자리가 없고 확률값이 1에 가까워지지 않음
    - 클래스가 10개이고 정답 클래스와 완벽히 일치해 $cos\theta=1$이 되고 나머지 클래스가 $cos\theta=0$이라고 가정
    - s = 1 => $\frac{e^1}{e^1+9 \times e^0}=0.23$. 완벽하게 맞춰도 정답 확률이 23%밖에 안

## 3. 평가
- m을 0에서부터 점진적으로 키우면 class 내 밀집도가 높아져 성능이 향상됨(m=0.35에서 최고 성능)
- m > 0.45 => 제약 조건이 지나치게 엄격해져 모형이 수렴하지 못하거나 과적합 발생 

