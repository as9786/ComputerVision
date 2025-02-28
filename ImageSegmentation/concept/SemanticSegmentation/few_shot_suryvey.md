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
- 목적 함수 : $\hat{M_q}=f_{\theta}(I_q,S(l))
- Traditional algorithm X
- Episodic training(meta-learning), 전이 학습 등 활용

### 2.1 Episodic training 
