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

### VFL의 한계
- Low-Quality matches : IoU 값이 낮은 경우에는 손실이 매우 낮아, 성능 개선에 한계

### MAL
- 
