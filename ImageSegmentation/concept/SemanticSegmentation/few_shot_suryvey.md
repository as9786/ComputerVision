# Few Shot Semantic Segmentation: a review of methodologies, benchmarks, and open challenges

## 초록
- 의미적 분할은 dataset 수집에 어려움을 겪고 있음
- Few-Shot semantic segmentation : 오직 적은 예시로 semantic classes를 구별해낼 수 있는 것

## 1. 서론
- 의미적 분할 : Pixel-Level
- 영상 분류, 객체 탐지와 연관이 있음

![image](https://github.com/user-attachments/assets/36ebad98-22f5-4a3b-84e4-de020ada3339)

- CNN을 활용한 영상 처리 기술은 성능 향상에 큰 영향을 미침
- Semantic segmentation dataset 공수 : MS COCO 기준 55,000명이 한 시간 일해야 제작할 수 있음
- Specific domain은 수집이 더 어려움
- 그래서 FSL(Few Shot Learning)이 필요
- FSL을 의미적 분할에 적용한 것이 Few Shot Semantic Segmentation(FSS)
- 적은 labelled example로 새로운 label을 학습해야 함

## 2. 배경 및 문제 정의
- FSS : (image, mask)로 구성된 training set에서 k개를 뽑아 구성된 support set S를 통해, query image($I_q$)에서 class l과 mask($\hat{M_q}$)를 예측하는 문제
- Class l이 주어졌을 때, k개의 쌍으로 구성된 support set을 구성
- $S(l)={(I^i, M_l^i)}_{i=1}^k$
- $I^i$ : RGB image of shape [H,W,3], $M_l^i$  : Binary mask of shape [H,W]
- 목적 함수 : $\hat{M_q}=f_{\theta}(I_q,S(l))$
- Traditional algorithm X
- Episodic training(meta-learning), 전이 학습 등 활용

### 2.1 Episodic training 
- Meta-leraning
- Episode : a support set of labeled images S, a query image $I_q$ 그리고 이에 대응되는 GT mask $M_q$
- 모형은 각 episode마다 예측값과 정답값의 손실을 최소화하기 위해 학습
- 모형은 나중에 unseen classes에 대해 시험
- Trainset($D_{train}$)으로부터 class set(C)를 받은 후, 훈련($C_{train}$)과 시험($C_{test}$)을 나눔($C_{train}\capC_{test}=0)
- $C_{train}$에서 임의의 class c를 하나 뽑아 training episode 구성
- c를 고정하고, 해당 c에 해당하는 k개의 사진과 정답으로 support set S를 구성. c에 대한 query image($I_q$)와 정답($M_q$)도 같이 구성
- 목적 함수

![image](https://github.com/user-attachments/assets/3f5c25eb-214b-45df-9c08-a65591e95618)

- 각 episode에서 최적화 값을 찾으며 제한된 support set에 대해서도 일반화 가능

### 2-2. 전이 학습
- Pretrained feature extractors or backbones

## 3. Methodology spectrum

![image](https://github.com/user-attachments/assets/e2eff7b8-41e7-4aeb-9857-843a00e346bb)

### 3.1 Conditional Networks

![image](https://github.com/user-attachments/assets/5275adb1-1e74-4cda-890c-a0e4030cacfa)

- Two parallel branch : Conditioning branch and segmentation branch
- Conditioning branch(g)는 Support set(S)을 입력으로 받고, parameter $\theta$를 생성
- Segmentation branch(h)는 query image($I_q$)와 $\theta$를 받고, 예측값($\hat{M_q}$) 출력
- 시험 동안에는 h의 사전 학습된 특징 추출기를 사용하여 $I_q$로부터 dense map을 추출
- 그 후, h가 최종적인 예측값 출력

 #### Few-shot segmentation propagation with guided networks.
 - 첫 번째 실험에서는 S에서 뽑은 $\theta$를 h의 query feature와 결합
 - 최종 feature map은 작은 합성곱 신경망을 통해 binary mask로 변환
 - 두 번째 실험에서는 선형 분류기 가중치로
 - 첫 번째 접근법의 성능이 더 좋음

#### Simpler is better: Few-shot semantic segmentation with classifier weight transformer
- 최적값을 찾기 위해 transformer 사용
- 이전 실험과 비슷하게 $\theta$는 final mask를 생성하기 위해 사용. Feature extractor는 g와 h 사이에서 사전 학습
- 핵심은 g를 선형 분류기 가중치를 Q, feature vector를 K, V로 사용

#### Rich Embedding Features for One-Shot Semantic Segmentation

- 서로 다른 parameter를 사용 시 도움이 됨 
- 해당 parameter들을 사용하여 서로 다른 3개의 similarity maps를 제안. 해당 maps는 최종 예측을 생성하기 위해 순서대로 결합됨
- 첫 번째 parameter set(Termed Peak Embedding) query image에서 구별되는 특징들을 확인하고 강조
- 이는 embedding에 대해서 상대적으로 높은 값을 강조하여 중요한 사진 영역으로 attention을 유도함
- 두 번째 parameter set(Global Embedding)은 support image 내에 물체에서 중요한 정보를 포착하는데 집중
- 객체 지역 내에 features의 평균 값을 계산하고, 정확한 분할을 위한 전역 정보를 압축
- 마지막으로 adaptive embedding은 attention을 사용하여 객체 관련 pixel의 상대적 중요도를 식별
- 이는 입력의 문맥과 정보를 기반으로한 집중을 동적으로 조정할 수 있게 하여 복잡한 상황에서도 좋은 성능을 이끌어 냄

### 3.2 Prototypical Networks

- 사진들을 embedding space에 점들로 표현. 비슷한 사진이면 가깝고, 그렇지 않으면 멀어짐
- Support set에서 같은 클래스로 구성된 사진들의 중심을 계산하는 것은 해당 클래스의 원형을 표현
- 추론 시에는 새로운 사진이 가까운 중심점의 클래스로 예측

![image](https://github.com/user-attachments/assets/de7e4de4-b39b-43c5-ab03-fe3924b30277)

- 분할 모형을 pixel-wise classification으로 모형화할 수 있다는 점을 감안하여, 학습된 특징 공간에서 query image의 각 pixel을 투영한 후, 가장 가까운 prototype의 동일한 class로 labeling

![image](https://github.com/user-attachments/assets/570de570-0ee9-4e87-8635-31b1d18f35af)

- The computation of prototypes & 적합한 거리 지표를 선택하는 것이 중요

 #### The computation of prototypes
 
- Masked Average Pooling를 주로 사용
- MAP는 support image가 투영한 feature volumne으로부터 ResNet, VGG와 같은 특징 추출기를 통해 유용한 정보 표현을 추출 
- 해당 과정은 feature volume과 GT mask 간의 요소별 곱 과정을 포함
- Hadamard product의 평균값은 class prototype을 상징하는 single feature vector를 산출
- MAP는 GT mask가 주체를 묘사하는 feature volume의 공간적 위치에서 vector를 처리

#### 거리 지표
- The similarity between prototypes and query features
- Bregman distance divergence
- 경험적으로 Euclidean distance보다 cosine distance의 성능이 더 좋음

#### Prototype mixture model
- 하나의 class를 1개를 초과한 prototype으로 표현. Class의 작은 특징들도 더 잘 포착
- 이를 graph-based로 확장
- Fully connected graph. 각 node는 feature vector. 간선은 유사도. 해당 간선은 pixel-level classification에 사용
- Class 수 < Prototype 수
- 모형이 사진의 배경에 존재하는 유사 class로 인해 혼란을 겪음
- 해당 문제를 해결하기 위해, 활성화되지만 label이 없는 영역에 대해 pseudo-class를 도입
- 해당 접근 방식을 통해 새로운 class를 추론함으로써 limited support set을 더 잘 활용 


