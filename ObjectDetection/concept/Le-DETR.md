# Revisiting Real-Time Detection Transformer with Efficient Encoder Desine

## 초록
- DETR은 훌륭한 성능 향상을 이룸. 그러나 backbone에 과도한 사전 학습 비용으로 인한 처음부터 다시 생성하는 것이 어렵고, 참신한 backbone architecture의 탐색을 방해함으로써 연구 발전을 제약함
- Local attention mechanisms과 현대의 효율적인 합성곱을 결합한 EfficientNAT 제안
- 추론 속도와 성능을 개선한 hybrid encoder
- 이를 통해 Le-DETR(Low-cost and Efficient DEtection TRansformer) 제안
- 이전 대비 80% 사전 학습 데이터셋을 줄임

## 1. 서론

<img width="640" height="507" alt="image" src="https://github.com/user-attachments/assets/56a090e4-078e-4f54-a497-1b0b2b163049" />

- 
