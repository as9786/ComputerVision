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
- 
- SASA는 attention을 합성곱 신경망의 보조 수단이 아니라, 합성곱을 완전히 대체하는 독립적인 기본 블록(stnad-alone primitive)으로 사용
- 
