# Stand-Alone Self-Attention in Vision Models(SASA)

## 초록
- ResNet의 모든 공간 합성곱을 local self attention으로 대체하여 순수 attention based model 구축
- Relative positional embedding을 도입하여 attetion mechanism에서도 합성곱 신경망의 핵심 성질인 평행 이동 등가성(translation equivariance) 달성
### 평행 이동 등가성
- 입력이 평행 이동하면, feature map도 똑같이 평행 이동하는 성질
- 사진 속 고양이가 왼쪽에 있을 때, 고양이 얼굴에 점을 찍음 -> 고양이가 오른쪽으로 100 pixel 이동하면 점의 위치도 똑같이 오른쪽으로 100 pixel 이동
- 평행 이동 불변성(Translation invariance)
  - 고양이가 왼쪽에서 오른쪽으로 움직여도 최종 판단 결과가 변하지 않고 똑같은 성질
- DNN은 위치 정보를 보존하는 등가성을 유지하며 정보를 처리하다가, 마지막 분류 단계에서는 위치와 상관없이 class를 맞추는 불변성을 획득
- Kernel size가 커져도 가중치 수가 늘어나지 않은 attention의 특성 덕분에, ResNet-50 대비 가중치와 연산량은 줄이고 더 높은 분류 정확도 기록

## 1. 서론
- 합성곱 신경망 한계 : 수용 영역을 넓혀 장거리 상호작용(long-range dependencies)를 파악하려 하면 가중치 수와 연산량이 kernel size의 제곱으로 폭증
- SASA는 attention을 합성곱 신경망의 보조 수단이 아니라, 합성곱을 완전히 대체하는 독립적인 기본 블록(stnad-alone primitive)으로 사용
- 모든 위치를 참조하는 global attention 대신, 주변 영역만 참조하는 local self-attention을 사용하면 연산 비용을 제어 가능
- Relative positional embedding을 통해 합성곱과 유사한 공간적 위치 정보 학습 기대

## 2. 방법
- ResNet architecture 기반으로 spatial convolution을 local sef-attention으로 교체
- ResNet bottleneck block의 3 x 3 convolution을 attention layer로 대체
- Spatial downsampling이 필요한 경우 attention 이후 average pooling 사용

### 2-1. Local self-attention
- 각 pixel 그리고 feature 위치를 query로 사용
- Query 주변의 k x k 영역을 memory block으로 정의
- Memory block 내의 feature들을 key와 value로 변환
- 주변 영역에서만 attention 수행

$$ y_{i,j} = \sum_{a,b \in N_k (i,j)} softmax_{ab} (q^T_{i,j}k_{ab})v_{ab}$$

### 2-2. Relative positional embedding
- 기본 self-attention은 content similarity를 기반으로 작동하므로 feature 간 상대적인 위치 정보를 직접 반영 X
- 위치 정보를 사용하지 않으면 pixel의 공간적 배치 관계를 효과적으로 구분하기 어려움
- 이를 해결하기 위해 2D relative positional embedding 도입
- Query와 주변 key 사이의 행 및 열 방향 상대 거리 계산
- Row offset과 columns offset의 embedding을 결합하여 relative positional representation 생성

### 2-3. Attention stem
- 초기 층에서는 가장자리, 질감 등 저차원 공간 특징 추출이 중요
- RGB pixel 개별적으로 의미 있는 정보를 충분히 포함하지 않기 때문에 content-based attention만으로 초기 특징을 학습하기 어려움
- 이를 위해 spatially-aware value transformation 제안
- 주변 위치에 따라 서로 다른 값 변환을 적용하여 공간적 특징 학습 강화

$$\tilde{v}_{ab} = (\sum_m p(a,b,m)W^v_m)x_{ab}$$

- p(a,b,m) : 위치에 따른 가중치
- $W^v_m$ : 학습 가능한 값 변환 행렬 
