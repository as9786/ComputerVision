# Denoising Diffusion Probabilistic Models(DDPM)

![다운로드](https://user-images.githubusercontent.com/80622859/201042842-eccb71ec-73ed-47bc-9a9a-3bf4da3f039c.png)


- Diffusion process에서는 원래 이미지가 있을 때, 아주 조금의 noise를 넣고, 이것을 여러 번 반복하여 원래 이미지와 거의 독립적인 noise를 만듦 
- 신경망은 diffusion process의 역과정인 reverse process의 coefficient를 학습

## Diffusion process(from data to noise)

![다운로드](https://user-images.githubusercontent.com/80622859/201042927-6b2581df-897b-4f07-af87-2b64d32ba2eb.png)

- q : Diffusion process이며 미세한 gaussian noise를 추가하는 과정
- 만일 $x_{t-1}$이 조건으로 주어지면, $x_{t-1}$ 이전의 $x_{t-2}, x_{t-3}...$과 독립적
- x의 아래 첨자는 0에서 t까지의 과정을 포현하는데, $x_0$은 noise가 없는 data이고, t가 커짐에 따라 점점 noisy해져서 $x_T$는 gaussian noise

## Reverse process(from noise to data)

![다운로드](https://user-images.githubusercontent.com/80622859/201044235-7cacca3a-fd20-4783-beeb-44dd510b0ff4.png)

- p : Reverse process, gaussian noise를 걷어내는 과정
- p와 q 모두 Markov chain

- 신경망으로 표현되는 p model이 q를 보고 noise를 걷어내는과정을 학습하는 것
- q는 noise를 아주 조금 추가하는 과정
- 단순히 q의 평균과 표준편차와 같아지도록 학습한다면 p 또한 당연히 noise가 추가되는 과정으로 학습됨

## 2. DDPM loss

### 1. VAE

![캡처](https://user-images.githubusercontent.com/80622859/201462729-912829c4-0533-4ab9-a7f8-33395d77a350.PNG)


