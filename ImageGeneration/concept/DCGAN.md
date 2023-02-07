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

- 별도의 pooling layer를 사용하지 않음. 대신에 strided convolution 사용 => Spatial downsampling
- 생성기에서는 downsampling 과정도 함께 학습 가능
- 판별기에서는 spatial upsampling 진행 가능
