# YOLOv10: Real-Time End-to-End Object Detection

## 초록
- Existing YOLO architectures heavily rely on NMS, which improves accuracy but introduces latency
- A dual assignment strategy was proposed to resolve the duplicate prediction problem in order to build an NMS-Free YOLO model

## 이중 할당 전략
- 비 최대 억제는 여러 후보 상자에서 가장 높은 점수를 가진 상자를 선택 => 추가적인 계산 필요
- 하나의 객체에 하나의 예측만 할당하면 비 최대 억제가 필요 없지만 학습 시 성능이 떨어질 수 있음
- Dual label assignments + Consistent matching metric

<img width="442" height="182" alt="image" src="https://github.com/user-attachments/assets/f8f3bf03-090f-4677-922f-590289e26ee5" />

- One-to-many head & One-to-one head
- Only the one-to-one head is used during inference

## Consistent matching metric
- A metric for quantitatively evaluating the degree of matching between instances in both one-to-one and one-to-many assignment heads

<img width="287" height="32" alt="image" src="https://github.com/user-attachments/assets/b5978af4-23ce-4af3-8ec9-a9e725edf509" />

- p : 분류 점수, $\hat b$ : 예측 경계 상자, b : 정답 경계 상자, s : Spatial prior information indicating whether the anchor point of a prediction lies within an instance
- 두 개의 head가 비슷한 좋은 예측을 선택하도록 학습
- Matching score = Classification score + Localization quality + Spatial prior
- Achor point가 정답 경계 상자 내부에 있으면 사전 분포 점수를 높게 부여

## 모형 구조
### Classification head
- 3 x 3 depthwise separable convolution + 1 x 1 convolution

<img width="265" height="297" alt="image" src="https://github.com/user-attachments/assets/860f80d5-ad9c-4ed7-a133-386559fdfbac" />

### PSA(Partial Self-Attention)

<img width="141" height="296" alt="image" src="https://github.com/user-attachments/assets/19158bc8-bf23-42f4-95d5-e7f9468f2486" />

- 특징 전체가 아니라 일부 channel에만 self-attention 적용
- 256 channel => 64 channel-> Self-Attention, 192 channel -> 그대로 통과
- 계산량 감소
- 전역 정보 유지


