# CenterNet: Keypoint Triplets for Object Detection

## 초록
- 기존의 두 단계 방식은 비효율적
- To enable efficient prediction, we assume a single anchor per object
- One-Stage

## 서론
- Two stage detector : 여러 경계 상자 중 최적으 경계 상자를 만드는 작업
- Anchor : 경계 상자의 중심

## 방법
- 합성곱 신경망
- Encoder-Decoder. 3 decoders
- Heatmap : $\hat Y \in [0,1]^{W/R \times H/R \times C}$
- R : stride, C : Keypoint type(Class type)
- 각 개체가 중심점이 될만한지 판단
- $\hat Y_{x,y,c}$=1 : Keypoint(Center point)
- Anchor-Free
- 객체 하나 = 중심점 하나
