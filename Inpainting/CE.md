# Context Encoders: Feature Learning by Inpainting

## 1. Image inpainting
- 영상이나 image에서 훼손된 부분을 복원하거나 불필요한 문자나 특정 물체를 제거한 후 삭제된 영역을 자연스럽게 채우는 방법

![캡처](https://user-images.githubusercontent.com/80622859/182582437-406c15e9-eef5-4def-ab04-403b750df0f9.PNG)

## 2. Context Encoder(CE)

### 1. Intro
- context 기반의 픽셀 예측을 통해 비지도 학습된 이미지 학습 algorithm
- Auto encoder와 유사
- 주변 환경에 조건화된 임의 영역의 context를 생성하도록 훈련

#### Auto Encoder(A.E)
- 입력을 출력으로 복사하는 신경망

![캡처](https://user-images.githubusercontent.com/80622859/182587600-d724141d-f182-4a20-9849-c3658d501906.PNG)

- 간단한 신경망과 달리 네트워크에 여러가지 제약을 가함으로써 어려운 신경망으로 만들엊 ㅜㅁ
- ex) 은닉층의 node 수를 입력층의 것보다 작게하여 데이터를 압축(Undercomplete AE), 입력 데이터에 noise를 추가한 후 원본 입력을 복원할 수 있도록 신경망 학습
- Encoder : 인지 네트워크(recognition network), 입력을 내부 표현으로 변환
- Decoder : 생성 네트워크(generative network), 내부 표현을 출력으로 변환

#### CE에서 AE를 사용할 경우  문제점 
- AE는 input image를 이용하여 저차원의 병목 계층(bottlenect)을 통과한 후 재구성함
- 하지만 이러한 과정은 의미있는 표현을 학습하지 않을수도 있고, 압축에 한계가 발생
- 누락된 부분을 채우는 작업은 전체 image의 내용을 확인하고, 누락된 부분에 대해서 자연스러운 painting이 필요

- CE를 학습할 때, standard pixel-wise reconstruction loss(표준 픽셀 단위 재구성 손실)과 reconstruction plus an adversarial loss(재구성 및 상대적 손실)을 모두 실험
- 결과 : 후자의 경우가 출력의 여러 종류를 더 잘 처리할 수 있기 때문에 훨씬 더 좋은 결과를 출력

#### Denosing autoencoder 
- 복원 능력을 더 강화하기 위해 기본적인 AE의 학습방법을 변형

![캡처](https://user-images.githubusercontent.com/80622859/182590288-9b1c6f27-4a1c-47b0-8b67-9f5d14529bdf.PNG)

- noise가 없는 원 data에 noise를 가하여 $\tilde x$ 생성. 
- 논문에서는 위의 그림처럼 noise가 위치해 있는 pixel 값을 모두 0으로 만듦

#### CE에서 Denoising AE를 사용할 경우 문제점
- 입력 이미지를 손상시키는 과정은 매우 단순한 과정으로 원상태로 복구하기 위해 많은 의미있는 정보를 요구하지 않음
- CE는 훨씬 더 어려운 작업인 근처 pixcel에서 hint를 얻을 수 없는 image의 큰 누락 영역을 채울 수 있음
- 자연어처리의 Word2Vec과 유사

### 2. CE의 구성
