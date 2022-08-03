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
- Encoder-Decoder 구조
- Encoder : 영역이 누락된 input image의 latent feature representation 생성
- latent feature representation : Convolution을 거쳐 나온 중간 결과, decoder 입력 직전 상태의 encoder의 출력값

![캡처](https://user-images.githubusercontent.com/80622859/182592006-fcb34d47-f341-45c0-a655-caceaa7e5d1f.PNG)

- Decoder : feature representation을 사용하여 누락된 image의 content를 생성(누락된 영역 복원)
- AE와 동일하게 비지도학습으로 진행. 
- Model이 image를 이해하는 것 뿐만 아니라 누락된 부분에 대해서도 해결 방안을 생성해야 함
- 누락된 영역을 채움과 동시에 주어진 맥락과 일관성을 유지하는 방법이 여러 가지가 있기 때문에 multi-modal
- CE의 encoder와 decoder를 다 학습하여 reconstruction loss(L2)와 adversarial loss를 최소화
- Reconstruction loss : 누락된 영역의 전체 구조를 맥락과 관련하여 포착
- Adversarial loss : particular mode(특정 모드)를 선택하는 효과

### 3. CE의 평가
- Encoder와 Decoder 독립적으로 진행
- Encoder는 image patch의 context만 encoding하고 resulting feature를 사용하여 dataset에서 가장 가까운 인접 context를 검색하면 원래 patch와 의미적으로 유사한 patch가 생성.
- 다양한 이미지 이해 작업을 위해 encoder를 미세 조정하여 학습된 feature representation을 검증
- Decoder는 CE가 누락된 영역을 채울 수 있는 것을 보여줌.

##  3. CE for image generation

![캡처](https://user-images.githubusercontent.com/80622859/182593193-df416a4c-212a-441e-9603-0ca801d799e4.PNG)

### 1. Encoder-Decoder pipeline
- Encoder : 영역이 누락된 입력 이미지를 가져와 latent feature representation을 생성
- Decoder : feature representation을 사용하여 누락된 이미지 content를 생성
- Encoder와 decoder는 채널 단위의 fully connected layer로 연결 -> decoder의 각 단위가 전체 이미지 컨텐츠에 대해 추론

### 2. Encoder
- 위의 그림처럼 없어진 부분을 가진 입력 이미지를 latent vector로 만듦
- Encoder는 AlexNet 참조
- ex) 227 x 227 input image, AlexNet의 5개의 conv + pooling layers를 사용하여 6x6x256의 feature representation 계산
- CE는 AlexNet과 달리 ImageNet으로 분류 학습을 하지 않음. 처음부터 무작위로 초기화된 가중치로 context 예측에 초점을 두어 훈련

### 3. Channel-wise fully connected layer
- Encoder와 Decoder를 완전히 연결하면 parameter의 수가 많아져서 GPU에 과부하
- 해결하기 위해 channel-wise fully connected layer 이용
- 입력층에 nxn인 feature map이 m개 있으면 nxn차원의 m개의 feature map을 출력하여 decoder에 전달
- 이 때 각 feature map마다 활성화함수를 적용하며 전달(일반적인 FCL과 달리 feature map을 연결하는 parameter가 존재하지 않으며 feature map 내에서만 정보를 전달)
- FCL을 할 경우 parameter의 수는 $mn^4$가 되지만 위의 과정을 거칠 경우 $m^2n^4$가 됨(편향은 무시)
- stride = 1

### 4. Decoder
- 전달받은 feature map을 사용하여 image pixel 생성
- ReLU 활성화 함수를 거친 학습된 filter가 있는 5개의 up-convolutional layer(고해상도 이미지를 생성하는 컨볼루션)로 이루어져 있음.
