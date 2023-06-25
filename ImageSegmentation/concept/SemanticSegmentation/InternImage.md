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
- ViT와 CNN의 장점을 결합하여 hybrid-ViT를 만들기도 함
- 

