# RF-DETR: Neural Architecture Search for Real-Time Detection Transformers

## 초록
- 기존 탐지 모형의 일반화 문제
- 가중치 공유 기법(Weight-sharing Neural Architecture Search, NAS)로target dataset에서 재학습 없이 수천 개 구조를 빠르게 평가.

## 1. 서론
- OVD model들은 일반적인 분야에서는 좋은 zero-shot 성능을 보임. 그러나 일반적이지 않은 곳에서는 어려움을 겪음
- Closed-Vocabulary detection models는 실시간 추론에서 장점을 가지지만, 성능이 비교적 떨어짐
- RF-DETR addresses this trade-off
- Propose a method scheduler-free that can generalize to real-world data distribution
- Inspired by OFA, vary model inputs such as image resolution and architectural components such as patch size during training
- 즉, 학습 중에 모형이 동작하는 설정을 계속 바꿔가면 학습
- 하나의 큰 모형이 여러 형태의 작은 모형들을 대표하도록 학습되고, 추론 때 원하는 설정만 골라서 사용

## 2. 방법론
- Change LW-DETR backbone CAEv2 to DINOv2 backbone
- Although DINOv2 is slower, its time is improved through NAS
- Batch normalize -> Layer normalize
- Add lightweight instance head(Inspired by MaskDINO)
- The encoder outputs are bilinearly interpolated and a lightweight projector is trained to generate a pixel embedding map
- Unlike MaskDINO, multi-scale backbone features are not integrated into te segmentation head to minimize latency
- DETR이 갖고 있는 query token(representative vector for each object)을 이용해서, pixel마다 어떤 물체에 속하는지 score map을 찍어 mask 생성
- Weight-sharing NAS는 서로 다른 입력 영상 해상도, patch size, window attention block, decoder layer and query token을 가진 수천 개의 모형 구성을 평가
- 학습은 매 반복마다 구성을 무작위로 뽑고 진행
- 하나의 큰 모형이 매번 다른 방식으로 학습
- Path embedding interpolation : Patch size를 계속 변경하여 학습
