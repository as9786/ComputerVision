# Real-Time Scene Text Detection with Differentiable Binarization

## 서론
- 분할 기반 모형은 pixel 단위 data를 다루므로 글자 탐지에서 많이 다뤄짐
- 해당 방법은 회전되거나 기울어진 영상에서도 좋은 성능을 보이나 후처리가 복잡해 연산량이 많음
- 정확도 향상을 위해 progressive scale expansion을 숭핸 PSENet, 분할 결과에 pixel embedding을 하는 방법으로 pixel 간 거리를 군집화하는 방법이 SOTA
- 기존 방식은 분할 신경망을 이진화된 영상으로 만들기 위해 고정된 임계값을 사용
- 해당 논문은 이진화 과정을 분할 신경망에 직접 삽입하여, 분할과 이진화를 함께 최적화 => 각 위치마다 적응형 임계값(adaptive threshold)을 자동으로 예측 
- Joint optimization = Binarization operation + Segmentation network

![image](https://github.com/user-attachments/assets/356ea1c8-44bf-412d-9536-22b97de317ff)

- 하지만 이진화 함수는 특정 값 이상이면 1, 아니면 0이기 때문에 미분 불가능 => Differentiable Binarization(DB, 이진화 근사 함수) 사용

## 방법

![image](https://github.com/user-attachments/assets/4f1f9da5-1938-448f-8e78-b480302ce849)

- 입력 영상은 Feature-Pyramid Backbone으로 넣음
- Pyramid features는 같은 크기로 up-sampled된 후 위로부터 정보 전달이 되어 F라는 feature 생성 
- Feature pyramid 구조를 통해서 크기 변화에 강건하게 만듦
- F를 사용해서 probability map(P)과 threshold map(T) 생성
- Binary map($\^{B}$)은 P와 F에 의해서 계산
- 학습 기간 동안, P, T, $\^{B}$가 최신화됨. P와 $\^{B}$는 같은 손실 함수를 공유
- 추론 과정에서는 box formulation module을 통한 $\^{B}$ 또는 P로부터 경계 상자를 얻음

### 이진화

#### 표준 이진화(Standard binarization)

- 분할 신경망으로부터 생성된 $P \in R^{HXW}$가 주어졌을 때, 이것을 binary map ($P \in R^{HXW}$)으로 전환
- 글자가 있는 영역은 1
- 보통 binarization map은 아래와 같이 표현

![image](https://github.com/user-attachments/assets/14e05db0-c7a2-4ebd-8a2d-9263f2ec555f)

- t : 사전 정의된 임계값

#### Differentiable binarization

- 표준 이진화는 학습 동안 분할 신경망과 함께 최적화될 수 없음
- 이 문제를 해결하기 위해 근사 계단 함수를 통해서 이진화를 수행

![image](https://github.com/user-attachments/assets/96519264-ca2d-499b-aae9-35692a87a749)

- k : Amplifying factor(기본값 = 50)
- 표준 이진화와 유사하지만 분할 신경망 학습 도중에 같이 최적화되는 부분이 차이
- 이는 배경과 글자를 분리하는데 도움을 줄 뿐만 아니라 서로 다른 text instances를 분리하는데도 도움을 줌

#### Adaptive threshold
- 글자와 배경을 효과적으로 구분하기 위해 pixel마다 다르게 설정되는 임계값

#### Deformable convolution
- 보다 유연한 수용 영역을 제공. 이는 극단적인 종횡비를 가진 text instance에서 장점을 가짐

#### Label generation

![image](https://github.com/user-attachments/assets/8c69bde5-f698-439e-b7dc-9df22985d515)

- 글자 영상이 주어졌을 때, 글자 영역의 각 다각형은 부분 집합으로 표현됨

![image](https://github.com/user-attachments/assets/34c29663-29e8-4218-81cf-951fadb213a8)

- n : 꼭짓점 수
- 글자 감지 영역을 설정하기 위해 원래의 글자 다각형 영역(G)을 축소하여 positive area 생성(Vatti clipping algorithm)

![image](https://github.com/user-attachments/assets/679054a9-0af6-42d6-872f-0616a6df2519)

- D : offset of shrinking, L : 둘레, A : 넓이, r : shrink ratio(default=0.4)
- 비슷한 과정으로 threshold map으로부터 labels를 생성할 수 있음
- 기존 축소된 text polygon $G_{s}$과 유사하게 G를 D만큼 확장하여 $G_d$ 생성. $G_d$는 글자 경계 너머의 외곽 영역을 포함
- $G_s$와 $G_d$ 사이의 공간을 경계 영역으로 간주
- 경계 영역 내의 각 pixel에 대해 이 pixel이 글자 경계에 얼마나 가까운지 가장 가까운 G의 선분까지의 거리를 계산
- 이 거리가 threshold map 각 pixel label이 됨
- 경계에 가까운 pixel은 낮은 값, 멀리 떨어진 pixel은 높은 값으로 설정

#### 최적화

- $ L = L_s + \alpha \times L_b + \beta \times L_t$
- $L_s$ : Probability map loss, $L_b$ : Binary map loss, $L_t$ : Threshold map loss, $\alpha$ : default=1, $\beta$ : default=10
- $L_s$, $L_b$는 BCE loss 사용
- Hard negative mining 적용

![image](https://github.com/user-attachments/assets/ec1ce869-d52c-4284-bc93-9aef27156145)

- $S_l$ : 표본 집합. Positive sample : Negatvie sample = 1 : 3
- $L_t$는 L1 loss 사용

![image](https://github.com/user-attachments/assets/d3a91ad5-198b-4dfc-8a2c-76303b052b89)

- $R_d$ : $G_d$ 내부 pixel, $y^*$ : threshold label
- 




