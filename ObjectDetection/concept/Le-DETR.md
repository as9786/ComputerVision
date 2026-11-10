# Revisiting Real-Time Detection Transformer with Efficient Encoder Desine

## 초록
- DETR은 훌륭한 성능 향상을 이룸. 그러나 backbone에 과도한 사전 학습 비용으로 인한 처음부터 다시 생성하는 것이 어렵고, 참신한 backbone architecture의 탐색을 방해함으로써 연구 발전을 제약함
- Local attention mechanisms과 현대의 효율적인 합성곱을 결합한 EfficientNAT 제안
- 추론 속도와 성능을 개선한 hybrid encoder
- 이를 통해 Le-DETR(Low-cost and Efficient DEtection TRansformer) 제안
- 이전 대비 80% 사전 학습 데이터셋을 줄임

## 1. 서론

<img width="640" height="507" alt="image" src="https://github.com/user-attachments/assets/56a090e4-078e-4f54-a497-1b0b2b163049" />

### 1-1. 기존 연구의 한계
- 기존 RT-DETR, D-FINE, DEIM 등은 우수한 탐지 성능을 보이지만 backbone 사전학습에 많은 비용 필요
- 지식 증류와 Additonal Training Images(ATI)에 의존
- 특히 추가 사전학습 data가 공개되지 않아 새로운 backbone 개발에 제약

### 1-2. 연구 가설
- 기존 DEIM과 D-FINE은 주로 decoder architecture와 학습 목적 개선에 집중
- Le-DETR은 backbone과 encoder 구조 개선에 집중

## 2. 방법

<img width="1351" height="556" alt="image" src="https://github.com/user-attachments/assets/15230ea9-5f9a-45b4-b477-050557410999" />

### 2-1. 전체 구조
- 기존 실시간 DETR 3단계(Backbone, hybrid encoder, DETR decoder)
- Backbone : EfficientNAT
- Hybrid encoder에 NAIFI를 도입하여 local attention 기반 특징 추출 수행
- Decoder에 flash attention 적용

### 2-2. EfficientNAT

<img width="602" height="321" alt="image" src="https://github.com/user-attachments/assets/4817289b-0029-4b4e-b556-d2190ead51e7" />

- 초기 단계에서는 합성곱을 통해 효율적으로 지역적 특징을 추출하고, 마지막 단계에서는 neighborhood attention을 통해 특징 표현력 강화

#### Neighborhood attention
- 서로 인접한 국소 영역 중심의 attention mechanism
- 기존 attention의 연산량 문제를 해결하고, 기존의 sliding window 방식이 가진 경계선 왜곡 문제를 해결
- 

