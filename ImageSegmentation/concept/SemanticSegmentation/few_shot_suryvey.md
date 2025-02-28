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

