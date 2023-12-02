# Adversarial Autoencoders

## 초록

- 변분 추론을 수행하기 위해 GAN을 사용하는 probabilistic autoencoder. Hidden code vector의 aggregated posterior를 임의의 사전 분포와 매칭하여 변분 추론을 수행
- Aggregated posterior를 사전 확률에 매칭시키는 것은, 사전 공간의 특정 영역에서 표본을 생성할 때 의미있는 표본을 생성하는 것을 보장
- AAE는 decoder를 가정한 사전 확률을 data distribution으로 사상하는 deep generative model을 학습
- Semi-supervised classification, 비지도 군집화, 차원 축소 등

## 1. Introduction
- 고차원적이고 풍부한 분포를 포착하는 생성 모형
- VAE : 잠재 변수에 대한 사후 분포를 가정하고 이에 대한 모수를 추론하는 신경망(변분 추론)
- GAN : 따로 분포에 대한 가정을 하지 않고 data distribution으로부터 신경망의 출력 분포를 직접적으로 형성
- GMMN : Data distribution을 학습하기 위해 moment matching cost function

## 2. Method

![image](https://github.com/as9786/ComputerVision/assets/80622859/72b75748-52f9-4795-8aef-4b5b592b80c9)

- 윗단은 일반적인 autoencoder. Image x를 받아 reconstructed image를 복원
- 아랫단은 새로운 판별기가 encoded latent vector distribution인 q(z)와 임의의 표본 p(z)를 구분하게 됨
- z가 auto encoder의 encoding 과정을 거쳐서 얻은 모수 분포 q(z)에서 나온 것인지, 아니면 사용자가 직접 정의한 분포에서 나온 것인지 구별


### 학습
- Reconstruction phase(AE) : AE와 동일하게 encoder-decoder 학습
- Regularization phase(Adversarial networks) : AAE의 latent vector z를 학습
1. 
