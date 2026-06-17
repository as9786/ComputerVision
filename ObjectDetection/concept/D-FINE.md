# Re-Define Regression task in DETRs as Fine-grained Distibution Refinement

## 초록
- 경계 상자 회귀 문제를 재정의 -> 뛰어난 위치 정밀도
- Fine-Grained distribution refinement(FDR) & global optimal localization self-distillation(GO-LSD)
- FDR transforms the regression process from fixed coordinate prediction into an iterative refinement of probability distributions, providing fine-grained intermediate representations that significantly improve localization accuracy
- GO-LSD adopts a bidirectional optimization strategy that distills localization information from refined distributions into shallow layers, while reducing the difficulty of residual prediction task in deeper layers
- D-FINE achieves a better trade-off between speed and accuracy by applying lightweight optimizations to computationally intensive modules and operations

## 1. 서론
- DETR has two major limitations
1. 경계 상자 회귀에서 고정 좌표 방식은 위치적 불확실성을 반영하지 못함. 최적화에 어려움
2. 전통적인 지식 증류 방식은 탐지 작업에 비효율적. It has issues of high training cost and limited synergy with anchor-free models

## 2. 사전 지식

### Localization Distillation(LD)
- 단순한 분류 확률이나 특징을 모방하는 대신, 교사 모형으로부터 유용한 위치 정보를 증류 -> 학생 모형 성능 향상
- However, this approach also has limitations, as it relies on an anchor-based architecture and incurs additional training costs

## 3. 방법

<img width="1260" height="642" alt="image" src="https://github.com/user-attachments/assets/6855716b-77e9-41d6-90ae-33aa45422b31" />

- It significantly improves performance through FDR and GO-LSD without introducing additional parameters or increasing training time

### FDR

- FDR iteratively optimizes probability distributions that provide corrections for bounding box prediction, thereby offering more fine-grained intermediate representations
- FDR utilizes a non-uniform weighting function to enable more precise and progressive adjustments at each decoder layer, thereby improving localiztaion accuracy and reducing prediction errors
- It it compatible with anchor-free, end-to-end frameworks, enabling more flexible and robust optimization
- Initially, the first decoder layer predicts binary bounding boxes and preliminary probability distributions through the conventional bounding box regression head and the D-FINE head
- The initial bounding boxes are used as reference boxes, and the subsequent layers refine them by adjusting the distributions in a residual manner
- 경계 상자를 고정된 좌표값으로 바로 예측하지 않고, 각 상자 가장자리의 위치 보정량을 확률 분포로 표현한 뒤 decoder layer마다 점진적으로 정제
- 기존의 DETR은 중심 좌표, 너비와 높이를 하나의 고정된 값으로 회귀
- 기존 방식은 이 가장자리가 정확히 어디쯤 있어야 하는가에 대한 불확실성을 잘 표현 못 함
- 기존 경계 상자 회귀 : 왼쪽 경계는 x=120
- FDR : 왼쪽 경계는 x=118~123 근처일 가능성이 높고, 다음 decoder layer에서 이 분포를 더 좁혀가자
- 중간 표현이 더 풍부
- Non-Uniform weighting function
    - 경계 상자가 이미 정답에 가까울 때는 아주 미세한 조정. 많이 틀렸을 때는 큰 보정
    - 모든 위치를 균일하게 다루는 것이 아닌, 상황에 따라 조정 정도를 정함 

### GO-LSD
- 기존의 D
