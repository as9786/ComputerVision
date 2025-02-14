# CoAtNet: Marrying Convolution and Attention for All Data Sizes

## 서론
- ViT는 CNN에 비해 제한적인 학습 능력을 지니고 있음
- CNN은 일반화 능력이 떨어짐
- 해당 논문은 위의 단점을 보완하고 장점을 합쳐 정확도와 효율성을 높임
- Depthwise convolution이 attention layer와 효과적으로 합쳐짐
- 적절한 방법으로 합성곱층과 attention layer를 쌓는 것은 높은 일반화 성능과 capacity를 얻을 수 있음
- CoAtNet = Convolution + Attention

## 모형

![image](https://github.com/user-attachments/assets/3f706027-dd36-4a65-bb2b-b7c111d2d7ff)

### 1. Merging convolution and self-attention
- Inverted bottleneck : 입력의 channel size를 4배로 확장한 후, 다시 원래 크기로 투영하여 residual connection을 가능하게 하는 구조
- Depthwise convolution

![image](https://github.com/user-attachments/assets/ec0cbc51-c467-45eb-9c4d-d10278bd9af4)

- Self-attention

![image](https://github.com/user-attachments/assets/20845031-d3ee-41ae-b85c-a294e56f305f)



#### 1. Input-adaptive Weighting
- Depthwise convolution kernel $w_{i-j}$는 입력에 독립적인 모수. Attention weight $A_{i,j}$는 입력에 의존
- Self-attention은 서로 다른 위치 사이의 관계를 잘 포착. 하지만 data의 수가 적으면 과적합 위험

#### 2. Translation Equivariance
- $w_{i-j}$는 두 지점 i와 j의 상대적인 위치만 고려. 절대적 위치를 고려하지 않음
- 이는 제한적인 크기에서의 일반화 성능을 향상
- ViT는 positional embedding을 사용하기 때문에 일반화가 부족

#### 3. Global Receptive Field
- Self-attention의 수용 영역은 사진 전체. 합성곱은 수용 영역이 작음
- 수용 영역이 크면 문맥 정보가 더 많아 모형 수용 영역이 더 커짐
- 하지만 모형의 복잡도도 높아짐

- 이상적인 모형은 translation equivariance를 통해 일반화 성능이 높으며, input-adaptive weighting과 global receptive field를 통해 capacity가 높아야 함
- Convolution + Attention을 위해 global static convolution kernel과 adaptive attention matrix를 더함
- Softmax normalization 전에 더하거나 후에 더하는 두 가지 방식 존재

#### Pre-normalization

![image](https://github.com/user-attachments/assets/18e1b00c-9de3-4465-a4ad-3cf4dea47453)

- Attention weight $A_{i,j}$가 translation equivaraince의 $w_{i-j}와 input-adaptive $x^T_ix_j$에 의해 결정. 상대적 크기에 따라 두 효과를 모두 볼 수 있음
- Parameter의 개수를 늘리지 않으면서 global convolution kernel이 가능하도록 하기 위해 vector $w_{i-j}$ 대신 scalar를 사용하기도 함
- Scalar w 사용은 모든 (i, j) 쌍의 정보가 pairwise dot-product attention을 계산하면서 모두 포함됨
- 그래서 post보단 pre를 사용

### 2. Vertical Layout Design
- 계산이 느려지는 것을 방지하기 위해 어느 정도 down-sampling으로 spatial size를 줄인 후 global relative attention 사용
- ConvNets의 구조를 모방하여 down sampling

