# Real-Time Object Detection Meets DINOv3

# 초록
- 단순하면서 효과적인 dense O2O에 기반하여, DEIM은 더 빠른 수렴과 향상된 성능을 보여줌
- Backbone : DINOv3 or distilled using DINOv3
- Spatial Tuning Adapter(STA)
- 단일 크기 출력을 효율적으로 다중 크기 특징으로 변환. 강력한 의미적 표현에 대한 세밀함을 보완=> 검출 성능 향상

## 1. 서론
- DETR-based approaches are preferred due to their end-to-end design
- Propose DEIMv2 by integrating the DEIM pipeline with DINOv3
- STA operates in parallel with DINOv3 and efficiently transforms the single-scale output of DINOv3 into multi-scale features required for object detection without additional parameters
- 동시에 입력 사진을 빠르게 down sampling하여  매우 작은 수용 영역을 갖는 세밀한 다중 크기 특징을 제공함으로써 DINOv3가 제공하는 강한 의미적 정보를 보완
- Decoder simplification
- FFN -> SwitchFFn. LayerNorm -> RMSNorm => 성능 저하 없이 효율성 높임
- 반복적 정제 과정 동안 object query의 위치가 크게 변하지 않는다는 점을 이용하여, 모든 decoder layer에서 query positional embedding 공유
- Copy-Blend augmentation => 감독 신호 향상 및 모형 성능 향상

<img width="827" height="267" alt="image" src="https://github.com/user-attachments/assets/bc2379a7-f68d-4591-b92f-d1bc67007ed8" />

## 2. 방법

### 전체 구조
- Follow the design of RT-DETR(Backbone, hybrid encoder, decoder)
- Backbone에서 추출된 다중 크기 특징은 먼저 encoder를 거쳐 초기 검줄 결과를 생성. 상위 K개의 후보 경계 상자를 선택.
- Decoder는 이 후보들을 반복적으로 정제하여 최종 결과 예측
- Backbone : ViT-based variants and HGNetv2-based variants

### Spatial Tuning Adapter
- 완전 합성곱 신경망. 세밀한 다중 크기 특징을 추추하기 위한 초경량 순전파 신경망. Bi-Fusion
- ViTDet : ViT에 deconvolution을 적용하여 최종 ViT 출력을 다중 크기 특징으로 변환하는 Feature2Pyramid module
- STA is simpler
- No parameter. 쌍선형 보간법 사용
- 1 x 1 합성곱으로 구성된 Bi-Fusion 연산자를 통해 추가 강화

### Efficient decoder
- Deformable attention decoder
- 비선형 표현 능력을 강화하기 위해 SwiGLUFFN 통합. 효율적으로 학습을 안정화하고 가속하기 위해 RMSNorm 적용
- Shared single positional embedding

### Enhanced Dense O2O
- 배경 없이 새로운 객체를 추가하는 copy-blend
- Copy-Paste와 달리 새로운 객체를 사진과 자연스럽게 혼합

### 학습 설정 및 손실 함수
- 다섯 가지 손실 항의 가중합
- MAL + FGL(Fine-Grained Localization) + DDF(Decoupled Distillation Focal) + L1(Bbox loss) + GIoU

<img width="448" height="32" alt="image" src="https://github.com/user-attachments/assets/bd2df00c-a3bf-4ce1-a3b7-d2ba7f8cccae" />

- $\lambda_1=1, \lambda_2=0.15, \lambda_3=1.5, \lambda_4=5, \lambda_5=2$


