# VAE(Variational Auto-Encoder)

## VAE
- Input image X를 잘 설명하는 feature를 추출하여 latent vector z에 담고, 이 z를 통해 X와 유사하지만 완전히 새로운 data를 생성하는 것을 목표
- 각 feature들이 gaussian distribution을 따른다고 가정하고 z는 각 feature의 평균과 분산값을 나타냄
- ex) 한국인의 얼굴을 그리기 위해 눈, 코, 입 등의 feature를 latent vector z에 담고, 그 z를 이용해 그럴듯한 한국인의 얼굴을 그려 냄 

## 구조

![image](https://user-images.githubusercontent.com/80622859/212450915-e19f9b8f-8b2c-4640-88cb-174a89dfff2e.png)

## 수식적 증명
- 모형의 파리미터 $\theta$가 주어졌을 때, 우리가 원하는 정답인 x가 나올 확률인 $p_{\theta}(x)$를 높이는 것이 VAE 학습의 핵심

## AE vs VAE
- 탄생 배경이 다름
- 구조가 비슷해서 Variational AE라는 이름이 붙음
- AutoEncoder의 목적은 encoder
- VAE의 목적은 decoder
- AE는 latent space의 어떤 하나의 값을 나타낸다면, VAE는 gaussian distribution을 나타냄
