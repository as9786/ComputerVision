# Generating Diverse High-Fidelity Images with VQ-VAE-2

## Abstract
- VQ-VAE에서 사용되는 자기 회귀 모형을 확장하고 강화하여 이전보다 높은 일관성 높은 표본 생성
- 간단한 feedforward encdoer 및 decoder network를 사용
- VQ-VAE는 압축된 잠재 공간에서만 자기 회귀 모형을 표본 추출해야 하며, 이는 특히 큰 사진의 경우 pixel 공간에서 표본 추출하는 것보다 훨씬 빠름

## 1. Instroduction
- GAN은 고품질 및 고해상도 사진을 생성
- 하지만 모형의 표본이 실제 분포의 다양성을 완전히 포착 X
- GAN은 평가하기 어려움.
- 우도 기반 방법은 Negative Log Likelihood(NLL) 최적화
- 보이지 않은 data에 대한 모형 비교 및 일반화 측정이 가능
- 우도 기반 모형은 원칙적으로 data의 모든 mode를 포함. Mode collapse와 GAN에서 볼 수 있는 다양성 부족 문제에 시달리지 않음
- Pixel space에서 우도를 직접 최대화하는 것은 어려움
- 본 논문에서는 loss compression의 idea를 사용하여 생성 모형이 무시할 수 있는 정보를 modeling하는 것을 완화
- AE의 중간 표현을 vector quantization하여 사진을 이산 잠재 공간으로 압축
- 이러한 표현은 원래 사진보다 30배 이상 작지만 decoder가 왜곡 없이 사진을 재구성할 수 있도록 함

## 2. Method
- 2단계 접근 방식
- 계층적 방식 훈련. 유도된 이산 잠재 공간에 pixelCNN 적용

![image](https://user-images.githubusercontent.com/80622859/232704332-c0a9d70c-8c45-4105-bedd-acfa22ca4287.png)

## 2.1 Stage 1 : Learning Hiearchical Latent Codes

- Vector quantization된 code에 계층 구조를 사용하여 large image modeling
- 물체의 모양과 같은 전역적인 정보를 분리하여 질감과 같은 지역적인 정보를 추출
- 각 수준에 대한 이전 모형은 해당 수준에 존재하는 특정 상관 관계를 포착
- 전역적인 정보를 modelingㅎ는 top latent code와 top latent code에 따라 조절되는 bottom latent code는 지역 세부 사항을 나타냄
- 256 x 256 사진는 bottom level에서 64 x 64로 줄어들고, top level은 32 x 32 크기를 갖음
- Decoder 부분에서는 encoding된 vector quantized code를 전부 받아서 decoding 수행
- Residual block과 strided transposed convolution으로 수행

## 2.2 Stage 2 : Learning Priors over Latent Codes
- Stage 1에서 학습한 모형으로부터 표본 추출을 할 수 있도록 사전 분포를 latent code로 학습시키는 단계
- 사전 확률을 train dataset로 학습시킴으로써 성능을 향상시키고 marginal posterior와 prior 간 거리를 줄임. 학습된 prior로부터 sampling된 latent varialbe은 decoder가 학습하는 동안 관찰한 것과 비슷
- Top latent map에서의 prior는 전체 구조를 modeling하는 책임이 있으므로 mulit-head self-attention layer를 사용. 공간적 위치 간 상관관계를 얻기 위해 더 큰 수용 영역을 사용
