# EdgeCrafter: Compact ViTs for Edge Dense Prediction via Task-Specialized Distillation

## 초록
- Insufficient task-specific representation learning in small-scale ViT
- Propose a unified compact ViT framework for edge dense prediction centerd on ECDet
- ECDet는 지식 증류된 경량화된 백본과 엣지 친화적인 인코더-디코더 구조
- DINOv3 증류
- Standard patch embedding -> Lightweight covolutional stem. FPN -> 보간법 및 선형 변환을 활용한 멀티 스케일 특징 구성

## 1. 서론
- Edge device는 용량에 한계

<img width="862" height="452" alt="image" src="https://github.com/user-attachments/assets/48a89064-f3d9-440f-87b9-4c3f3ae7bdae" />

- ViT를 경량화하는 것은 쉽지 않음 이에 따라 두 가지 아이디어를 제시

1. Task-Specialized knowledge distillation
  - Teacher model : DINOv3 
2. Edge-friendly student architecture
  - Standard patch embedding -> Lightweight convolutional stem
  - 단순한 보간법과 선형 투영을 통한 multi-scale features
- 증류된 backbone과 encoder는 ECDet에서 직접 사용

## 2. 관련 연구

### Knowledge distillation from vision foundation models
- VFM -> Smaller backbone or unified representation

### 효율적인 객체 탐지
- YOLO families, DETR, RF-DETR etc

## 3. 방법

<img width="852" height="256" alt="image" src="https://github.com/user-attachments/assets/ced81c50-ed1a-4bd2-814c-6beaa4ffb6f1" />

- DINOv3 -> Compact ViT backbone (ECViT)
- Distilled backbone에 ECDet 구성
- Compact ViT backbone과 RF-DETR style encoder-decoder detector 결합
- 지역 정보 보존을 위해 convolutional stem 사용. 무거운 FPN 대신 선형 변환 기법 사용

### 3-1. ECDet Architecture

<img width="816" height="332" alt="image" src="https://github.com/user-attachments/assets/b865cf83-176d-48e9-97f1-cfad423f6c3c" />

- Backbone
  - Convolution stem : 3 x 3 convolution filter. stride 2
  - 한 번에 지역 정보를 집계하는 대신, Transformer block에 들어가기 전에 stem 단계에서 수용 영역을 점진적으로 확장
- Multi-scale feature generation
  - 마지막 두 개의 transformer blocks에서 출력된 토큰들을 활용
  - 평균을 낸 후 형태 변환을 통해 1/16 feature map 생성
  - 그 후 보간법과 1x1 convolution filter를 통해 1/8, 1/32 feature map 생성
- Encoder
    - RT-DETR
    - Attention-based Intra-scale Feature Interaction(AIFI)
    - 가장 낮은 해상도의 feature map은 AIFI를 통해 정제
    - 가장 낮은 해상도의 feature map에 self-attention을 적용하여 수용 영역을 확장, 장거리 문맥 정보 강화
    - 그 후 더 높은 해상도의 feature map과 CNN-based cross-scale feature fusion(CCFF)를 통해 조정 
    - High-Level scale로부터 얻은 문맥 정보를 전파하고, 이를 지역적인 공간 정보와 결합
- Decoder
  - DETR
  - Stacked self-attention, deformable corss-attention, FFN
 
### 3-2. Task-Specialized Distillation
- Detection-specialized teacher
  - 

### 3-2. Task-Specialized Distillation(Detection-specialized teacher)
- 
