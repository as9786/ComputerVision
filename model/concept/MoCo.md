# Momentum Contrast for unsupervised visual representation learning

## 1. 기존 문제
- 영상 : 연속적, 고차원 => 사전 구축 힘듦

## 2. 방법

### 2-1. 대조 학습
- 기존 대조 학습과 다르게 동적 사전 구축
- 사전은 data에서 추출된 key로 구성
- Encoder는 사전 탐색을 수행
- 사전 탐색 : Query와 유사한 key를 찾음

### 2-2. 사전 구성
- Queue(FIFO)로 구성
- Queue로 설정 시 사전 크기가 mini batch보다 커질 수 있음(기존 방법들은 보통 일치함)

### 2-3. 손실 함수(InfoNCE)
- $L_q = -log \frac{exp(q \cdot k_{+}/\tau)}{\sum_{i=0}^K exp(q \cdot k_i / \tau)}$
- q : Encoded query, k : Key(Encoded sample)

### 2-4. Momentum 
- Queue dictionary 사용 시, 구성이 계속 바뀌어 역전파 불가
- $\theta_k \leftarrow m\theta_k + (1-m)\theta_q$
- m : Momentum coefficient
- Query encoder만 학습
- Key encoder는 학습 불가 -> Momentum으로 최신화

