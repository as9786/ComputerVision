# MogFace: Towards a Deeper Appreciation on Face Detection

## 1. 서론
- 얼굴 dataset(WIDER FACE)와 COCO set은 근본적인 환경 차이 때문에 3가지 문제 발생
1. 극단적인 스케일 편차(Scale distribution bias)
    - 20 pixel 이하의 소형 객체가 18%에 불과한 반면, WIDER FACE는 전체 얼굴의 55%가 20 pixel 미만.
    - 기존 범용 data augmentation은 이러한 극단적인 크기 차이를 올바르게 학습 못함

2. Label assignment
3. 오탐지 문제 : 얼굴과 유사한 질감을 가진 손, 나뭇가지, 복잡한 배경을 얼굴로 잘못 오인하는 false alarm

## 2. 방법
- Tri-Pillar(핵심 전략) 
### 2-1. Selective Scale Enhancemnet(SSE)
- 기존 random crop 방식은 영상 고유의 맥락 정보와 크기 분포를 왜곡
- FPN의 각 계층이 가장 잘 표현할 수 있는 얼굴 크기의 통계적 분포를 수학적으로 산출
- 그 후 피라미드 계층별 표현력을 극대화하도록 원본 영상의 크기 분포를 정밀하게 재구성하는 증강 기법 적용

### 2-2. Ali-AMS(Adaptive Online Incremental Anchor Mining 
- 기존 고정 IoU 방식은 훈련 초기와 후기에 요구되는 anchor quality 차이를 유연하게 반영하지 못함
- 학습이 진행되는 동안 신경망의 예측 상태를 실시간으로 감시하여 어떤 anchor를 positive로 지정할지 스스로 적응하며 점진적으로 발굴하는 label assignment method 제안

### 2-3. HCAM(Hierarchical Context-Aware Module)

<img width="825" height="276" alt="image" src="https://github.com/user-attachments/assets/a6ef4d93-e495-46f0-a115-6546ff87fd73" />

- 얼굴 영역 하나만 좁게 보고 판단하면 주변의 다른 것들을 오인(False Alarm)
- FPN 전반에 걸쳐 넓은 수용 영역을 가지는 합성곱 층을 계층적으로 배치
- 시각적 맥락을 단계적으로 취합

### 2-4. 모형
- Backbone : ResNet-101
- Nect & Head : FPN 위에 HCAM module이 통합. Multi-scale anchor를 통해 single-stage 방식 
