# An Image is Worth 16x16 Words: Transformers for Image Recogintion as Scale

- Transformer를 사용한 구조가 수 많은 SOTA가 되고 있으며 그 시작점은 ViT
- 더 많은 data를 더 적으 cost로 사전 학습
- Image Classification을 비롯하여 다양한 분야에서 사용
- 대용량의 학습 자원과 data가 필요
- Text data에서는 이미 transformer가 가장 좋은 성능을 보이고  있음

## Visual Tranformer의 의의

![캡처](https://user-images.githubusercontent.com/80622859/185046721-e5fd8e00-d419-4737-9a37-e849c5213071.PNG)

1. 자연어 처리에 많이 사용되는 transformer를 vision task에 적용
2. 기존의 제한적인 attention 매커니즘에서 벗어나, CNN 구조 대부분을 transformer로 대체(입력층인 sequence of image patch에서는 제외)
3. 대용량 dataset을 사전 학습 -> small image dataset에서 전이 학습 => 훨씬 적은 계산 resource로 우수한 결과

## Visual Transformer 요약
- 이전 vision task에서 self-attention 적용의 한계

### Self-Attention
- 단어 간의 관계성 연산 결과를 활용하여 연관성이 높은 단어끼리 연결해주기 위해 활용(단어에 맥락을 붙여넣어주는 방법)
- Q,K,V 모두 동일한 embedding vector에서 도출됨
- Time-step을 활용하지 않음, 이전 단어에 대한 attention 결과를 활용하지 않음. 단지 단어 한 개에 대해 모든 단어에 대하여 attention score를 구하므로 이전 연산이 현재 단어에 대한 연산에 영향을 끼치지 못함
- Encoder는 모든 단어에 대하여, decoder는 이전에 예측했던 모든 단어에 대하여 hidden vector Q를 구하여 활용
- Hidden state vector를 온전히 보존하여 decoder의 길이가 길어지더라도 초기 정보가 지워지지 않음
- Bidirectional model

- 기존의 transformer를 최대한 그대로 적용시키고자 함
- Image를 patch로 분할 후 sequence로 입력 -> NLP에서 단어가 입력되는 방식과 동일
- 지도 학습
- JFT-300M 사전 학습 후, 전이 학습 => SOTA
- 편향이 없음

## ViT Method
- NLP의 transformer의 구조를 거의 바로 사용 가능

![캡처](https://user-images.githubusercontent.com/80622859/185048302-7aa34e43-b003-4759-b03d-0e08fc41d19f.PNG)

### ViT 핵심구조

#### 입력 embedding
- Token embedding을 1D sequence로 입력
- 2D Image(HxWxC) -> $N \times (P^2 \cdot C)$
- (P,P) : Image patch 해상도 
- N : Patch의 수 = $HW/P^2$
- D : 모든 층에서의 동일한 latent vector size -> Flatten한 patch를 학습 가능한 Linear projection(E)를 사용하여, D 차원으로 mapping
- Patch Embedding이 출력됨

#### [CLS] Token
- BERT의 [class] token처럼, 학습 가능한 embedding patch $z_0^0 = x_{class}$를 추가
- $z_L^0$ : 최종 L번째 층의 0 번째 token. 사전 학습과 미세조정을 수행하는 classification head가 부착

#### Classification Head
- 사전 학습 : 1-hidden layer인 MLP(Multi-Layer preceptron; 다층 퍼셉트론)

##### MLP
- 단층 퍼셉트론 : 입력층과 출력층만 있는 구조

![캡처](https://user-images.githubusercontent.com/80622859/185049928-0246b211-7c1b-4ee1-b8e9-241aaa1fb2b0.PNG)

- 결과값을 내놓는 부분은 활성 함수 존재. 즉 활성 함수가 1개밖에 없는 구조
- 제대로 된 학습이 불가 -> MLP

![캡처](https://user-images.githubusercontent.com/80622859/185050130-8748c859-62b5-41bc-b9a5-b80bdba1fabf.PNG)

- 미세조정 : 1-linear layer

#### Position embedding
- Patch Embedding의 위치 정보를 유지하기 위함
- Image이지만 1D position embedding 사용

#### Transformer
- 위의 embedding sequence가 encoder의 입력으로 들어감
- Transformer Encoder : Multi-Head로 구성된 self-attention 매커니즘 적용

##### Multi-head Attention

![캡처](https://user-images.githubusercontent.com/80622859/185051059-460d2beb-2398-4248-b630-a86b95b0d427.PNG)

![캡처](https://user-images.githubusercontent.com/80622859/185051086-fbbf2d1a-c2e8-4e20-be2c-875cdbfa6b00.PNG)

- 2가지 방법으로 attention layer 성능을 향상시킴
- 병렬 연산

### Hybrid architecture
- Image patch에 대해 바로 적용하기도 하고 CNN의 feature map에 대해서 ViT를 적용하는 것

### Inductive bias
- 우리가 ML/DL을 수행할 때 많은 data에 대해서 귀납적으로 문제를 더 잘 풀기 위해 설계한 model 또는 목적함수의 추가적인 가정
- Transformer의 경우에는 위의 경우가 필요하지 않고 대신에 대용량의 data가 필요

## 미세 조정
- 큰 dataset에 대해서 사전학습을 하고 작은 dataset에 대해서 fine-tuning하는 과정
- 사전훈련된 $z_L^0$에 붙은 MLP를 제거하고 0으로 초기화된 DxK 선형변환 층을 추가(K는 미세조정 dataset class 개수)
- 고해상도 image를 사용하는 것이 좋다고 알려져 있음 => patch size를 일정하게 유지한 채 큰 크기의 image 사용
