# FCOS: Fully Convolutional One-Stage Object Deteection

## 초록
- 하나의 단계로 이루어진 완전 합성곱 탐지기
- Anchor-Free

## 1. 서론

### Weakness of anchor box
- Detection performance is highly sensitive to the size, aspect ratio and number of anchor boxes
- 위 초매개변수들을 잘 조정해야 됨
- 정해진 매개변수들로 인해 작은 물체의 모양이 크게 변하게 된다면 성능 하락 => 일반화 성능 하락
- So many negative samples
- 복잡한 계산 필요

- Predict 4d vector (l, t, r, b) and class

<img width="442" height="256" alt="image" src="https://github.com/user-attachments/assets/34738308-7b3c-464f-9d2a-792b1655f7a7" />

- The 4D vector represents the offsets from the object's location to the four sides of the bbox
- The concept of center-ness is introduced to predict the deviation of a pixel from the center of the bbox

### Strength of FCOS
- 분할에도 사용 가능
- 단순
- Less memory, faster training

## 2. 관련 연구
### 2-1. Anchor-Free Detectors
- YOLO v2

## 3. 방법
- The object detection problem is reformulated as a per-pixel prediction task and multi-level prediction is employed to improve recall and resolve the ambiguity of overlapping bounding boxes

### 3-1. Fully Convolutional One-stage Object Detector
- Directly regress the bounding box from training samples
- 좌표가 정답 경계 상자에 속하고, 같은 class => Positive sample
- More positive samples (Not IoU based)

### 3-2. 신경망 출력
- C binary classifier

### 3-3. 손실 함수
- Cls : Focal loss
- Reg : IoU loss

### 3-4. Multi-level prediction with FPN for FCOS
- Because of large stride last feature map may cause low Best Possible Recall(BPR)
- BPR : 모형의 구조적 한계로 인해 이론적으로 탐지할 수 있는 객체의 최대 비율
- 하지만 실험 결과 더 나은 성능
- 경계 상자가 겹쳐질 경우, 어떤 경계 상자로 추정해야하는지 모호함을 가지게 됨 
- Multi-Level prediction => 해결

<img width="817" height="362" alt="image" src="https://github.com/user-attachments/assets/fe1bc702-39c8-4c23-abc8-048a73cbe332" />

- 5 levels of feature maps are used
- 각 단계에 대한 경계 상자의 회귀 범위를 직접 제한
- $max(l,t,r,b) > m_i\,\ max(l,t,r,b_ < m_{i-1}$ => Negative sample
- $m_i$ : The maximum distance that feature levvel i is responsible for regressing(0,64,128,256,512,inf)
- 상자가 겹칠 경우, 더 작은 상자 선택
- Share head

### 3-5. Center-ness for FCOS
- 위치에서 해당 위치에 속한 객체의 중심까지의 거리를 정규화된 값으로 표현
- $centerness^* = \sqrt{\frac{min(l^*,r^*)}{max(l^*,r^*)} \times \frac{min(t^*, b^*)}{max(t^*, b^*)}}$
- 0~1, BCE loss
- Score = Center-ness * classification score
- 객체 중심과 멀리 떨어져 있는 경계 상자의 점수를 낮춤
- Down-Weight
