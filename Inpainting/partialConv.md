# Image Inpainting for lrregular holes using partial convolutions

## 1. 서론

- Convolution이 유효 픽셀에서만 적용되도록 제한하는 masking 과정 추가
- 이후 normalize를 통해 결과 도출

## 2. 본론

### 1. Related Work

#### 1. Non-learning Based model
- 이웃한 픽셀을 이용하여 채워 넣는 기법
- 구멍이 작은 경우에만 가능
- texure의 분산이 작아야 가능
- 계산 비용이 매우 커서 실시간 처리가 어려움

#### 2. Deep learning based model
- 일정한 placeholder(빠져 있는 다른 것을 대신하는 기호나 텍스트의 일부) 값을 가지고 구멍의 값을 초기화
- context encoder / Semantic Image Inpainting with Deep Generative Model
