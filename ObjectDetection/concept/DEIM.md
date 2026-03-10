# DEIM: DETR with Improved Matching for Fast Convergence

## 초록
- DETR의 One-to-One matching에서 발생하는 희소 문제를 완화하기 위해, Dense O2O matching 제안
- Standard data augmentation method를 통해 추가 목표를 도입함으로써 영상 당 양성 표본의 수를 늘림
- Desne O2O의 역효과를 방지하기 위해 MAL(Matchability-Aware Loss) 제안

## 1. 서론
- DETR은 수렴이 느림
  1. Sparse supervision
     - 양성 표본 수가 적음
  2. Low-qaulity matches
     - 전통적인 탐지기는 8,000개 이상의 anchor 사용. DETR은 100~300개의 query 사용
     - Query는 공간적으로 정렬되어 있지 않기 때문에, IoU는 낮지만 신뢰도는 높은 문제 발생
- 이를 해결하기 위해, Group DETR(여러 query group을 둠), Co-DETR(O2M 방식 결합) 등 제안되었지만 decoder가 추가로 필요해 계산량이 증가
- DEIM은 훈련 사진 내 target 수를 늘려 학습 과정에서 자연스럽게 더 많은 양성 표본을 얻음
- Mosaic + Mixup
- 기존 DETR에서 사용되는 손실 함수(VariFocal Loss)는 상대적으로 적은 dense anchor 환경에 맞추어 설계
- VFL은 IoU는 높지만 신뢰도가 낮은 경우 강하게 규제하고, low quality matching은 거의 무시
- Low quality matching을 해결하고 dense O2O를 더욱 향상시키기 위해 MAL 제안
- MAL은 matched query와 target 간의 IoU와 분류 신뢰도를 함께 반영해 matchability에 따라 penalty 조정
- High quality matching에 대해서는 VFL과 유사하게 동작. Low quality matching에는 더 큰 가중치 부여 -> Positive sample의 효용을 높임. 수식도 더 간결
- DEIM은 dense O2O와 MAL을 결합해 효과적인 training framework 구성

## 2. 방법

### 2-1. Dense O2O
- Matching 구조는 그대로(O2O)를 유지하면서, 사진 당 정답 수 N을 늘려 지도 학습을 조밀하게 수행
- 원본을 네 구역으로 복제해 하나의 합성 영상으로 만듦(해상도는 유지)
- 정답 수가 1에서 4로 늘어남
- Desne O2O는 O2M 수준의 지도 학습 효과를 보이면서 복잡도 증가가 거의 없음

### 2-2. Matchability-Aware loss
### The limitation of VFL 
- VariFocal Loss는 focal loss를 기반으로 DETR model에서 객체 탐지 성능을 개선

<img width="527" height="92" alt="image" src="https://github.com/user-attachments/assets/abe4335a-c42f-473d-a11c-d61da5e4a355" />

- q : The IoU between the predicted bbox and GT bbox, p : The predicted probabaility for the foreground class, $\alpha, \gamma$ : The tuning parameter of rhe focal loss
- 한계점
    - Low-Quality matches : High IoU 값에 집중하여, low IoU에서는 손실 값이 매우 작아 모형이 해당 상자를 충분히 개선하지 못함
    - Processing negative sample : VFL에서는 정답이 IoU. 겹침이 전혀 없는 match를 negative sample로 간주해 positive sample 수를 줄이므로, 효과적인 학습이 제한(타 모형들은 IoU threshold 기준으로 나눔)

### Matchability-Aware Loss(MAL)
- Matchability is directly incorporated into the loss function, enabling the model to respond more sensitively to low-quality matches

<img width="506" height="78" alt="image" src="https://github.com/user-attachments/assets/dfdbb121-a6a8-45dc-9cd9-1a58a7fbf8fd" />

1. Target label을 q에서 $q^{\gamma}$로 바꾸어 negative/positive smaple의 가중치를 단순화
2. 양성-음성 균형을 위해 사용되던 초매개변수 $\alpha$ 제거
- 이는 고품질 경계 상자에 과도하게 집중되는 현상을 방지하고 전반적인 학습 개선

<img width="617" height="561" alt="image" src="https://github.com/user-attachments/assets/e14afdc6-87cc-48bf-af20-daf3a01814dd" />

## 3. 실험

### 3-1. 학습 세부사항
- Mosaic and mixup => Additional positive sample
