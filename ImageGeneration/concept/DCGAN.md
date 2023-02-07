# Unsupervised Representation Learning with Deep Convolutional Generative Adversarial Networks

- Deep Convolutional Generative Adversarial Networks(DCGAN)
- GAN의 경우에는 구조가 다소 불안정하고, Neural Network(NN)이 기본적으로 지닌 black box의 한계점이 존재
- 어떠한 과정을 거쳐서 결과가 나오는지에 대한 설명이 부족
- DCGAN 공헌
1. 안정적인 학습
2. 판별기가 이미지 분류에서 다른 비지도 알고리즘과 비교했을 때 대등한 성능
3. DCGAN이 학습한 filter들을 시각화하고, 특정 filter가 특정 객체를 생성하는 역할을 한다는 것을 알아냄
4. Vector 산술 연산이 가능(Semantic quality)

## 구조

- 이전에는 LAPGAN과 같이 합성곱층을 넣으려는 시도가 있었으나 유의미한 성능 향상이 없었음 

### 1. Max Pooling To Strided Convolution

![image](https://user-images.githubusercontent.com/80622859/217151911-06039755-57cb-4073-9cc9-3e949185297d.png)

- 별도의 pooling layer를 사용하지 않음. 대신에 strided convolution 사용 => Spatial downsampling
- 생성기에서는 downsampling 과정도 함께 학습 가능
- 판별기에서는 spatial upsampling 진행 가능
- CNN에서 pooling layer는 차원 축소뿐만 아니라 과적합을 방지하기 위한 목적으로 사용
- Pooling 과정에서 위치와 관련된 정보 등을 의도적으로 버림으로써 image의 불변적인 특징만을 뽑아냄
- 생성 모형에서는 세세하고 정교한 image를 생성하기 위해서는 모든 정보들을 포함하고 있는 것이 좋음

#### Fractionally Strided Convolution(Transposed Convolution)

![image](https://user-images.githubusercontent.com/80622859/217153355-cd3af097-40dd-4bee-985c-0849cb820cd2.png)

- Deconvolution과 같이 convolution으로 추출한 특징들을 다시 원본으로 되돌림
- 원본으로 복원하기 위해서는 위의 그림과 같이 feature map의 각 원소 사이, 그리고 바깥 부분에 모두 padding을 넣어주어야 함.

### 2. Eliminate Fully-Connected Layers

![image](https://user-images.githubusercontent.com/80622859/217152022-f1cf8198-b581-4d0a-9f5b-26e2479cda37.png)

- G에 noise vector z를 넣는 첫 번째 층과 D에서 출력값 결과를 판단하는 마지막 softmax layer를 제외하고는 전결합 계층을 모두 삭제

### 3. Batch Normalization

- 경사의 흐름이 deep model에서도 잘 흐르게끔
- 모든 층에 추가하면 문제가 발생하고, G의 출력층과 D의 입력층에는 적용하지 않음
- 이외에도 ReLU, Leaky RELU 


