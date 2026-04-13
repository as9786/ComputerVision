# Focal Loss for Dense Object Detection

## 1. 서론

- Class imbalance occuers due to the diffference in the number of positive and negative samples
- Since most samples are negative, inefficiencies arise during the training
- Before : A two-stage cascade approach was used to filter region proposals end eliminate background samples + Sampling heuristic
- 위 방법들은 한 단계 탐지기에서는 적용이 어려움 
- 한 단계 탐지기는 영역 제안 과정이 없어 풜씬 더 많은 후보 영역을 생성
- The class imbalance problem is more severe than in two-stage detectors

## 2. 방법

<img width="800" height="237" alt="image" src="https://github.com/user-attachments/assets/8f81de93-ba29-41d2-b17f-0527f6952f22" />

- Focal loss function
- A scaling factor based on the number of classes is added to the cross entropy loss
- 쉬운 표본의 기여도를 자동적으로 낮추고 어려운 예시에 대한 기여도를 높임

### 2-1. Focal Loss
- Solve the class imbalanced
- Cross entropy : 모든 표본에 대한 예측 결과들에게 동등한 가중치를 부여
- 어떠한 표본이 쉽게 분류될 수 있음에도 불구하고 작지 않은 손실을 유발
- Balanced cross entropy
  - $CE(p_t)=-\alpha log(p_t)$
  - Balances the positive and negative samples. 그러나 난이도에 따른 균형은 잡지 못함
- $FL(p_t) = =(1-p_t)^{\gamma} log(p_t)$
- 쉬운 예시는 가중치를 낮추고 hard negative sample에 집중
- $(1-p_t)^{\gamma}$ : Modulating factor, $\gamma$ : Tunable focusing parameter

<img width="747" height="200" alt="image" src="https://github.com/user-attachments/assets/711926d0-9e96-49bb-af2d-18d99fefba55" />

- $p_t$ : 정답 class에 대한 예측 확률. 얼마나 확신하는지
- $p_t$가 낮으면 어려운 예시, 반대의 경우 쉬운 예시
- $p_t$ ↓ -> $(1-p_t)^{\gamma} \approx 1$ -> 손실 거의 변화 X => 모형이 더 집중
- $p_t$ ↑ -> $(1-p_t)^{\gamma} \approx 0$ -> 손실 크게 감소 X => 영향 ↓
- $\gamma$는 쉬운 예시에 대한 가중치를 부드럽게 조절
- $\gamma = 0$ = Cross entropy. As the $\gamma$ value increases, the influence of the modulating factor becomes stronger

### 2-2. RetinaNet
- Feture pyramid by ResNet + FPN
- Classification subnetwork
- Bounding box regression subnetwork

