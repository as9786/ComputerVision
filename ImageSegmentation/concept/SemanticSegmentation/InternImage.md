# InternImage: Exploring Large-Scale Vision Foundation Models with Deformable Convolutions

## Abstract 

- 최근 몇 년간 large ViT가 크게 발전한 것과 비교하면 CNN을 기반으로 한 large scale model은 거의 연구가 안 됨
- InternImage는 기존 CNN의 엄격한 inductive bias를 줄이고, ViT와 같은 large scale data에서 대규모 parameter로 더 강하고 강력한 pattern을 학습할 수 있음
- ViT를 능가하는 CNN

- ## Introduction

- Transformer model은 NLP, CV 분야를 휩쓸어서 모든 연구의 기초
- CNN이 ViT보다 부족하다는 의미
- 하지만 CNN에 scaling-up parameter, architecture level design, massive data를 추가하면 ViT보다 비슷하거나 더 좋은 성능에 달성할 수 있다고 주장

![image](https://github.com/as9786/ComputerVision/assets/80622859/38583a2d-b7b7-4230-9cb0-c3c122980ae8)

- Operator level에서 보면 ViT는 long-range dependence를 가지고 적응적으로 공간영역 집계할 수 있음. MHSA의 이점을 활용하여 ViT는 large-scale data에서 CNN보다 더 강력하고 강력한 표현을 학습할 수 있음
- 구조 관점에서도 MHSA 이외에 층 정규화, 전결합계층, GELU 등과 같이 기존 합성곱 신경망에서 쓰이지 않은 요소들이 사용 됨
- (c)에서처럼 매우 큰 kernel을 가진 dense convolution을 사용하여 합성곱 신경망에 long-range dependency를 도입하려는 시도를 하였지만, 성능 및 모형 크기 측명에서 ViT와 격차 존재
- 저자들은 이와 같은 문제점을 해결하기 위해 flexible convolution인 DCN에서 시작
- Transformer와 유사한 구조의 맞춤형 block level 및 architecture level design을 채택하여 InternImage라는 새로운 backbone 생성
- Core operator로 window size가 3인 dynamic space convolution 사용
- 주어진 data에 대해서 적절한 수용 영역을 동적으로 학습할 수 있는 sampling offset
- Sampling offset은 modulation scalars에 대해 적응적으로 조정되어 ViT와 같은 adative spatial aggregation 달성 => 기존 합성곱 신경망의 과도한 inductive bias 감소
- Convolution window는 일반적으로 3 x 3이며, large dense kernel로 인한 optimization problem과 비싼 비용을 방지

![image](https://github.com/as9786/ComputerVision/assets/80622859/cc3621ed-1c28-44e5-b9db-3c0edb43b0a7)

- InternImage는 큰 parameter size로 효율적으로 확장하고 large scale dataset에서 더 강력한 표현을 학습하여 ViT와 비슷하거나 더 나은 성능으 얻음
- 개선된 3 x 3 DCN operator를 사용하여 장기 의존성과 adative spatial aggregation을 도입하여 CNN을 large scale setting에서 성공적으로 확장
- Operator를 중심으로 basic block 구축
- Stack rule 및 scaling 전략 탐구

## Related Work

### Vision Foundation Models

- Large scale dataset과 computation resource를 사용할 수 있게 된 후에 CNN은 visual recoginition에 주목
- 깊은 합성곱 신경망 등장
- DCN, Depthwise separable conv 등 다양한 방법 등장
- Transformer based model
- ViT는 global receptive, dynamic spatial aggregation을 가짐
- 하지만 ViT는 downstream task에서 computation/memory complexity로 인해 어려움을 겪음
- HaloNet, Swin Transformer는 local attention과 shfited window를 통해 정보 전송

### Large-Scale Models
- 모형을 확장하는 것은 자연어 처리 영역에서 잘 연구된 특징 표현을 향상시키는 중요한 전략
- ViT와 CNN의 장점을 결합하여 Hybrid-ViT를 만들기도 함

## Deformable Convolution v3

### Convolution vs MHSA

(1) Long-Range Dependencies

- Effective receptive field가 큰 모형은 대게 downstream vision task에서 더 잘 수행됨
- 3 x 3 convolution에 의해 stacked CNN은 실질적인 effective field는 상대적으로 작음
- 매우 깊은 모형에서도 합성곱 신경망 기반의 모형은 long-range dependencies를 얻을 수 없음

(2) Adaptive Spatial Aggregation

- 가중치가 입력에 의해 동적으로 조정되는 MHSA와 다르게 convolution은 정적인 가중치를 가지고, 2D locality, neighborhood structure, translation equivalence 특성을 가진 operation
- 편향이 높은 트성을 이용하여 ViT에 비해 빨리 수렴되고 training data가 덜 필요할 수 있지만 합성곱 신경망이 large-scale data에 정보를 학습하는 것을 제한

### DCN v2

- $\Delta p_k$를 이용하여 long-ragne dependencies를 포착할 수 있고, short-range까지 cover가 가능하다고 주장
- Adaptive spatial aggregation의 경우 samlping offset $\Delta p_k$와 modulation $\Delta m_k$ 모두 학습할 수 있어 MHSA와 유사한 특성을 제안한다고 주장
- 정적인 가중치가 아니라 합성곱을 취할 때마다 가중치를 변경시킴.

![image](https://github.com/as9786/ComputerVision/assets/80622859/8455a5fc-99e5-42b8-bd80-74c85ea7148f)

### Extending DCN v2 for VIsion Foundation Models

#### (1) Sharing weights among convolutional neurons

- 일반 합성곱과 유사하게 DCN v2는 각 convolution neuron마다 독립적인 가중치를 가짐
- 그러므로 parameter와 memory complexity가 sampling point 숫자에 대해 선형적으로 늘어남
- Depthwise Separable Convolution처럼 가중치 $W_k$를 depthwise, pointwise로 분리
- Depthwise part는 location-aware modulation scalar $m_k$가 담당
- Pointwise part는 shared projection weights w among sampling points로 진행

#### (2) Multi-group mechanism

- Adaptive spatial aggregation과 함께 작동하며 서로 다른 위치의 다른 representation sub-space의 풍부한 정보를 효과적으로 학습
- Spatial aggregation을 G group으로 분할, 각 group은 $\Delta p_{gk}$라는 sampling offset, $\Delta m_{gk}$라는 modulation scale -> 서로 다른 group에서는 MHSA처럼 서로 다른 spatial aggregation pattern을 가질 수 있음 => Downstream task에서 장점

#### (3) Normalizing modulation scalars along sampling points

- 기존의 DCN v2에서는 modulation을 계산할 때 sigmoid 활용
- Modulation scalars의 범위는 [0,1]. Sample points의 modulation scalar 합은 0 이상으로 다양하여 값이 안정적이지 않음
- Sigmoid 대신 softmax 사용
- Modulation value 안정. Large-scale model 학습 시 안정적인 결과 생성

![image](https://github.com/as9786/ComputerVision/assets/80622859/71f3350c-173b-4c79-a97b-7a40fe20b6ae)

- G : Group convolution 개수, K : Sampling point의 개수

- 장점
1. Long-range dependencies 및 adaptive spatial aggregation 측면에서 합성곱보다 장점이 있음
2. 적은 학습과 시간으로 모형을 더 효율적으로 만듦
3. 최적화하기 쉬움

![image](https://github.com/as9786/ComputerVision/assets/80622859/798417b4-19e3-43af-932b-5f7df83ae145)

