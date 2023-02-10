# Progressive Growing of GANs for Improved Quality, Stability, and Variation

## 1.1 문제점

- 이전까지 GAN 모형들은 high resolution image를 만드는 것이 힘들었음
- 고해상도일수록 판별기는 생성기가 생성한 image가 진짜인지 아닌지를 구분하기가 쉬워짐
- 고해상도로 만든다고 해도, memory issue로 mini-batch size를 줄여야 함 -> Batch size를 줄이면 학습과정 중 학습이 불안정

## 1.2 접근법

- 점진적으로 생성기와 판별기를 키우자
- 저해상도에서 고해상도로 키우기 위해 점진적으로 층을 추가 => High resolution image
- 논문에서는 1024 x 1024까지 생성

## 2. Progressive Growing of GANs

![image](https://user-images.githubusercontent.com/80622859/217967097-861c8e1c-318f-42e1-af15-95bad84f0bbd.png)

### 2.1 점진적으로 층을 추가해서 학습하는 장점

- Image distribution에서 large scale 구조를 먼저 발견하도록 도움을 줌
- Large scale : ex) 사람 얼굴에 대한 dataset이 있을 때, 전반적인 전체 얼굴의 형태
- G와 D의 model을 점진적으로 쌓아 올려가며 학습을 하는 것
- 처음에는 저해상도에서 보여질 수 있는 feature인 large scale들을 보면서 사람 얼굴에 대한 전반적인 내용들을 학습하고 점차 층을 쌓아 세부적인 특징들(눈, 코, 입 등)을 보면서 학습을 진행
- 모든 large scale을 동시에 학습 X(점진적으로)
- 모형에 층을 추가할 때 새로 추가하는 층을 부드럽고, fade in하게 넣어줌
- 학습된 이전 단계의 층들에 대한 sudden shock을 방지

![image](https://user-images.githubusercontent.com/80622859/217972780-ad9b3234-5d7a-43c7-989f-6daceedf6982.png)

- 학습이 안정적
- 해상도에 맞게 latent vector가 사상되면서 학습
- 안정적인 고해상도 image
- WGAN-GP Loss 사용

### 2.2 학습 방법

#### 생성기

![image](https://user-images.githubusercontent.com/80622859/217972920-43f58e3d-fd0d-4610-b983-7165af0f7edc.png)

##### Upscaling

- 부족한 pixel들을 채움으로써 더 선명하게 보이도록

![image](https://user-images.githubusercontent.com/80622859/218091074-75048335-d4c9-4778-a0de-67b0def3c10c.png)

- 각 층 맨 앞단에 위치시켜서 진행

##### Fade in

![image](https://user-images.githubusercontent.com/80622859/218091657-f03fe38b-fda6-4f9a-81bb-a7a0962004c8.png)

- 위의 그림에서 16 x 16을 upscaling을 할 때 32 x 32 image와 합쳐줄 때 pixel 마다 가중치를 두어서 저해상도와 새로운 image를 합침
- 해당 가중치 $\alpha$를 새롭게 출력된 image에 곱하고, upscaling된 저해상도 image에는 $1-\alpha$를 곱해줌
- 저해상도의 그림과 앞으로 학습시킬 고해상도의 detail이 합쳐짐
- $\alpha$는 0에서 점차 1로 증가(이전 층의 영향력을 줄여줌)
- 기존의 저해상도 층에서 학습된 방향을 일그러뜨리지 않고, 새로 추가된 층을 학습할 수 있음


##### Pixel normalization

- 그동안 GAN에서는 batch normalization 사용 => 공변량 변화(covariate shift) 문제 : Test data 분포가 train data 분포와 다른 상황
- GAN에 발생하는 신호의 증폭을 완화시키기 위해 정규화 필요 -> Pixel normalization
- 말 그대로 pixel 별로 정규화
- 각 pixel 별로 feature vector를 단위 길이(unit of length)로 정규화 해주고, 각 층의 맨 뒷 단에 적용
- 생성기의 upsampling 과정에서만 적용
- 새로운 층의 가중치 초기화는 He initializer

![image](https://user-images.githubusercontent.com/80622859/218093275-3f8c7324-fffe-40f0-b60d-e212591ad95a.png)

#### 판별기

![image](https://user-images.githubusercontent.com/80622859/218093994-b8efbb3d-f2b4-4e58-8cdb-dd40fd1de3aa.png)

##### DownScaling

![image](https://user-images.githubusercontent.com/80622859/218094089-6bfbc609-084b-4dab-9dce-c5a614c041a3.png)

- 저해상도에서 고해상도의 정보를 유추하는 절차

1. 신경망의 현재 해상도에 맞춰서 우리가 가지고 있는 training data를 downscaling하여 넣어줌. 저해상도 image로 변경되자만, 고해상도일 때 정보를 담고 있음 
2. Fade in 기법 사용

## Equalized Learning Rate(runtime weight scaling)

- 생성기와 판별기 간의 공정한 경쟁을 위해 각 층이 비슷한 속도로 학습하는 것이 필수
- Gaussian distribution으로 0~1 사이의 값으로 가중치 초기화
- He initializer
