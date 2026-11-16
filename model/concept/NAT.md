# Neighborhood Attention Transformer(NAT)

## 초록
- 각 pixel이 자기 주변 가장 가까운 k x k neighbor pixel에만 attnetion을 수행하는 방법
- Self-Attention 시간 복잡도 $O(N^2)$ -> O(N)
- Swin transformer처럼 영상을 격자로 강제 분할하거나 pixel shift를 하지 않아도 수용 영역이 넓어짐.
- Winodw attention보다 최대 40% 빠르고 memory를 25% 덜 사용

## 1. 서론

<img width="942" height="236" alt="image" src="https://github.com/user-attachments/assets/35b198c4-4ca3-40d2-ab98-0fed6c6c5ce2" />

- Stand-Alone Self-Attention(SASA)의 한계 : 합성곱 신경망처럼 sliding winodw 방식으로 local attention을 수행하려고 했으나, GPU에서 병렬화하기 까다로움. 속도가 느리고 영상 가장자리 pixel에서 상호작용 개수가 줄어드는 대칭점 깨짐 문제.
- Swin transformer 한계 : Window 간 정보 교환을 위해 인위적인 shifted window 연산이 추가로 필요. 격자 분할로 인해 합성곱 신경망의 장점인 평행 이동 등가성이 깨짐

## 2. 방법

### 2-1. Neighborhood attention의 정의
- 자신을 중심으로 한 가장 가까운 k x k개의 이웃 pixel로만 제한하는 명시적인 sliding window mechanism

$$NA_k (i) = softmax(\frac{Q_i K^T_{p(i)} + B_{i, p(i)}}{\sqrt d})V_{p(i)}$$

- Q : Query vector
- K, V : 가장 가까운 이웃 픽셀들의 key, value matrix
- B : 상재거 위치 편향
- SASA는 영상 테두리 픽셀에서 window가 영상 밖으로 나가면 padding을 넣어 attention 대상이 줄어듬
- NA는 가장자리 pixel에서도 무조건 k x k개의 가장 가까운 이웃을 참조하도록 안쪽으로 고정
- 모든 픽셀이 동일한 연산량. k를 사진 전체 크기로 키우면 자연스럽게 self-attention과 정확히 같아짐

### 2-2. NATTEN(Neighborhood Attention Extension)
- Sliding window attention이 널리 쓰이지 못한 이유는 기본 연산으로 구현 시 메모리 복사와 overhead가 극심했기 때문
- Tiled Neighborhood Attention algorithm을 고안하여 GPU의 공유 메모리 활용을 극대화한 패키지 NATTEN 구현
- 연산 속도는 최대 40% 향상, 메모리 사용량은 최대 25% 절감

### 2-3. NAT
- 4단계의 계층 구조
- Overlapping convolutional tokenizer : 3 x 3 convolution(stride=2)을 연속으로 2번 적용해 초기 해상도를 1/4f로 줄이며 지역적 연속성 보존
- Overlapping downsampler : 각 단계 사이에서도 단순 patch merging 대신 3 x 3 합성곱을 사용하여 해상도를 줄이고 channel을 두 배로 늘림
- NAT block : 층 정규화 -> NA -> 층 정규화 -> MLP (Swin과 유사)

## 3. 결과
- 전역 맥락 부족

