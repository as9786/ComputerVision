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

