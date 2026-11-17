# SCRFD: Sample and Computation Redistribution for Efficient Face Detection

## 1. 서론
- RetinaFace는 매우 뛰어난 정확도를 보이지만, 거대한 backbone을 쓸 경우 연산량이 너무 커서 edge device에서는 돌리기 힘듦
- 그렇다고 기존 모형을 단순 downscale 할 경우, 성능이 무너짐
- 해당 문제의 원인을 2가지로 정리
1. 잘못 설계된 연산량 분배
  - 기존 얼굴 검출기는 FPN 구조를 그대로 씀
  - 얼굴 검출은 일반 객체 검출에 비해 해상도가 작고 오밀조밀한 특성이 있는데, 이 차이를 무시한 채 불필요한 층에 연산 자원을 낭비 
2. 비효율적인 데이터 학습 불균형
  - 작은 얼굴 표본이 부족

## 2. 방법
- 최적의 모형 구조를 찾기 위해 두 가지 재분배 전략 제안

### 2-1. 연산 재분배(Computation Redistribution, CR)
- Backbone, neck, head 사이의 최적의 연산 비율을 수학적 탐색을 통해 재설계
- Backbone에서 초반 층보다 중간 층에 연산량을 대거 집중하는 것이 성능 향상에 가장 효율적
- Head 비중을 대폭 낮추고 단순화. 절약한 연산량을 backbone과 neck에 재투자

### 2-2. Sample Redistribution(SR)
- 아주 작은 얼굴들을 깊이 있게 학습시키기 위해, data augmentation 단계 재설계
- 기존 방식
  - 단순히 영상을 random cropping.
  - 큰 얼굴만 자주 노출되어 작은 얼굴을 학습하는 효율지 저하
- SR 적용 결과
  - 의도적으로 large cropping strategy
  - 얼굴 양성 표본이 대거 공급. 저해상도 영상 속 극도로 작은 얼굴들의 검출 성능이 비약적으로 향상

### 2-3. 모형 구조
- 사용자가 가진 하드웨어 성능에 맞춰 골라 쓸 수 있는 최적의 구조 제공
