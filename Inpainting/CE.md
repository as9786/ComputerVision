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

![캡처](https://user-images.githubusercontent.com/80622859/182595681-c4360420-cbd2-4386-a97e-e711eb5c2dee.PNG)

### 5. Loss Function
- 누락된 영역이 실제 영역을 맞추는 내용으로 학습.
- 누락된 영역을 채우는 방법이 여러 가지 존재 -> context 내의 연속성과 출력의 여러 모드 모두를 처리하기 위해 분리된 공동 손실 함수를 가짐으로써 학습
- Reconstruction loss : 누락된 영역의 전체 구조를 맥락과 관련하여 포착하면서, 예측에서 여러 모드를 평균화
- Adversarial loss : particular mode(특정 모드)를 선택하는 효과
- 각 실측값 이미지 x에 대해 context encoder는 출력 F(x)를 생성
- $\hat M$은 픽셀이 누락된 곳이면 1이고 입력 픽셀이면 0인 binary mask

![캡처](https://user-images.githubusercontent.com/80622859/182596685-1c877dee-a993-4dc9-8208-2c5763048474.PNG)

- 학습 중에 이러한 mask는 자동으로 생성

#### Reconstruction Loss(재구성 손실 함수)
- L2 distance 사용

![캡처](https://user-images.githubusercontent.com/80622859/182597339-ddc19091-6f39-4ff3-8d9e-11c8fc24b187.PNG)

- x : image, $\hat M$ : binary mask, $1-\hat M$ : 손실되지 않은 이미지의 영역을 나타내는 mask
- $1-\hat M$에 x를 요소별 곱을 하게 되면 구멍이 뚫린 이미즈를 얻게 됨
- L1과 L2 큰 차이 없음
- 단순 loss를 사용할 경우 decoder가 예측된 물체의 윤곽을 생성하도록 유도할 수 있지만, 세부사항 파악을 못함
- L2 loss가 높은 정밀도 texture보다 흐릿한 solution을 선호 -> 평균 픽셀 단위의 오차는 최소화 할 수 있지만 평균 이미지가 흐릿해짐
- 이를 adversarial loss를 추가함으로써 해결

#### Adversarial Loss(적대적 손실)
- GAN 기반

![캡처](https://user-images.githubusercontent.com/80622859/182598721-eb508729-4d49-4bd5-ab2a-7e2b9c2a6214.PNG)

- GAN의 기본 손실함수
- z : noise, G(z) : 가짜 이미지, x : 진짜 이미지
- D의 목적으로 GAN의 loss 함수를 최대가 되도록 하는 것. G의 목적은 GAN의 loss 함수를 최소가 되도록 하는 것
- 하지만 이는 CE에 쉽게 훈련되지 않음 <- D(Discriminitor)가 실제샘플이랑 예측샘플 분류를 하는데, 예측 샘플에서 손상된 영역을 복원한 이미지가 될거고 완전히 매끄럽지 않음. 그러면 D는 이 경계를 가지고 분류를 하게 되어서 과적합 발생)
- G(Generator)가 noise vector에 의해 조절되지 않았을 때 더 나은 결과를 보였다는 것을 발견
- 최종 적대적 손실 함수

![캡처](https://user-images.githubusercontent.com/80622859/182599330-fcbd7d90-29c0-448c-8cb4-6293164ab360.PNG)

- 누락된 영역뿐만 아니라 context encoder 출력 전체가 실제처럼 보이도록 이끌게 됨

- Joint loss

![캡처](https://user-images.githubusercontent.com/80622859/182599554-458d00c1-d9d6-44d7-b4d9-83ec1bc7e01d.PNG)

### 6. Region Masks
- 제거된 영역은 어떤 모양이든 될 수 있지만, 논문에서는 아래의 세 가지 종류를 제안

![캡처](https://user-images.githubusercontent.com/80622859/182599788-45bfa877-e278-473a-a673-add4a778ae1f.PNG)

#### 1. Central region
- 이미지 중앙에 정사각형 patch가 있는 가장 간단한 모양
- Inpainting에는 매우 효과적이지만 central mask의 경계에 고정된 특징(낮은 수준)을 학습
- 제거된 영역에 대응하는 낮은 수준의 image의 특징을 찾음 => 낮은 수준의 mask가 없는 image에 대해서는 일반화되지 않음

#### 2. Random block
- 신경망이 masking된 영역의 일정한 경계에 적응하는 것ㅇ르 방지하기 위해서 masking process를 random하게 적용
- 고정된 위치에 하나의 큰 mask를 적용하는 것이 아니라, 작은 mask들을 여러 개 설정하여 이미지의 1/4까지 덮을 수 있도록 함
- 이러한 masks는 겹칠 수 없음
- 뚜렷한 경계가 존재하는 문제 발생

#### 3. Random region
- 경계선을 완전히 제거하기 위해 PASCAL VOC 2012 dataset에서 얻은 random mask를 가지고 이미지에서 임의의 형상을 제거
- 이미지의 최대 1/4까지 덮음
- 위의 두 가지처럼 일반적인 특징을 찾아내는 것보다 훨씬 좋은 특징을 찾아냄
- 따라서 random region을 dropout하는 것을 모든 과정에서 사용

![Qualitative-segmentation-results-on-PASCAL-VOC-2012-validation-set (1)](https://user-images.githubusercontent.com/80622859/182600688-df74d1f6-6769-4710-88dc-bd7304db88ac.png)

##  4. Implementation details
- Caffe, Torch, Adam, masking된 입력 image에서 누락된 영역은 평균값으로 채움
- 






