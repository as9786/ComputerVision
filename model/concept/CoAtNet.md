# CoAtNet: Marrying Convolution and Attention for All Data Sizes

## 서론
- ViT는 CNN에 비해 제한적인 학습 능력을 지니고 있음
- CNN은 일반화 능력이 떨어짐
- 해당 논문은 위의 단점을 보완하고 장점을 합쳐 정확도와 효율성을 높임
- Depthwise convolution이 attention layer와 효과적으로 합쳐짐
- 적절한 방법으로 합성곱층과 attention layer를 쌓는 것은 높은 일반화 성능과 capacity를 얻을 수 있음
- CoAtNet = Convolution + Attention

## 모형

### Merging convolution and self-attention
- Inverted bottleneck : 입력의 channel size를 4배로 확장한 후, 다시 원래 크기로 투영하여 residual connection을 가능하게 하는 구조

#### 1. 
