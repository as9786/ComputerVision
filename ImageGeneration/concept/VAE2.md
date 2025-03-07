# VAE(Variational Auto-Encoder)

## VAE
- Input image X를 잘 설명하는 feature를 추출하여 latent vector z에 담고, 이 z를 통해 X와 유사하지만 완전히 새로운 data를 생성하는 것을 목표
- 각 feature들이 gaussian distribution을 따른다고 가정하고 z는 각 feature의 평균과 분산값을 나타냄
- ex) 한국인의 얼굴을 그리기 위해 눈, 코, 입 등의 feature를 latent vector z에 담고, 그 z를 이용해 그럴듯한 한국인의 얼굴을 그려 냄 

## 구조

![image](https://user-images.githubusercontent.com/80622859/212450915-e19f9b8f-8b2c-4640-88cb-174a89dfff2e.png)

## VAE decoder
- 모형의 파리미터 $\theta$가 주어졌을 때, 우리가 원하는 정답인 x가 나올 확률인 $p_{\theta}(x)$를 높이는 것이 VAE 학습의 핵심

![image](https://user-images.githubusercontent.com/80622859/212453370-c72b3976-0d70-44c1-b564-52bb991f1d05.png)

- 적분식 -> 베이즈 공식 : x와 z가 동시에 일어날 확률을 모든 z에 대해서 적분 = x의 우도
- 하지만 위의 식을 계산하는 것은 다루기 힘듦 (P(x)의 값을 모름)

![image](https://user-images.githubusercontent.com/80622859/212454422-541a14d9-e74b-40ed-a474-43bcec596a64.png)

- Variational inference(변분추론)를 통해 해결
- Enocder의 역할은 실제 우리가 알고 싶은 P(z|x)를 신경망으로 가장 근사하는 Q(z|x)를 구할 수 있는 신경망이 됨
- p는 실제값, q는 p를 근사화하는 추정값

## ELBO(Evidence of Lower BOund)
- variational lower bound
- 우리가 관찰한 p(z|x)가 다루기 힘든 분포를 이루고 있을 때, 이를 조금 더 다루기 쉬운 분포인 Q(x)로 표현하는 과정에서 두 분포의 차이를 최소화히기 위해 사용

![image](https://user-images.githubusercontent.com/80622859/212456788-9e5e569b-631d-48d8-a0d1-73d1c5f30843.png)

- P(x)를 최대화 시키고 싶기에 P(x)에 log를 씌워줌
- 이는 기댓값 형태로 나오게 되는데 이 때 logP(x)는 그대로 두고 z가 enocder를 거쳐서 나오는 확률 분포를 따를 때의 기댓값

![image](https://user-images.githubusercontent.com/80622859/212457267-542bc8d0-d1f3-4ed3-84ed-6e81b49073bd.png)


## AE vs VAE
- 탄생 배경이 다름
- 구조가 비슷해서 Variational AE라는 이름이 붙음
- AutoEncoder의 목적은 encoder
- VAE의 목적은 decoder
- AE는 latent space의 어떤 하나의 값을 나타낸다면, VAE는 gaussian distribution을 나타냄
