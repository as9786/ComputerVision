# Generative Adversarial Nets
- 진짜와 동일해 보이는 이미지를 생성하는 model


![다운로드](https://user-images.githubusercontent.com/80622859/188362200-b0b0d132-9fe3-4dc5-a8d1-d37376fe752a.png)

- 기존 지도학습의 한계를 뛰어넘은 model
- 기존의 지도학습의 경우 dataset이 필수. 이러한 dataset을 만드는 과정에 많은 비용 발생
- GAN은 비지도학습에 속하며, data를 직접 생성하는 큰 장점을 가짐

![다운로드 (1)](https://user-images.githubusercontent.com/80622859/188362341-89f9474b-4fb5-4b42-936f-45374d18c23b.png)


## Abstract
- 두 개의 분리된 모델
- Generative model(생성기,G) : data의 분포를 포착
- Discriminative model(판별기,D) : 한 sample이 생성기가 아닌 실제 training data로부터 왔을 것이라는 확률을 추정하는 model
- 위를 동시에 학습하는 adversarial process 과정
- G의 학습절차는 D가 잘못된 결정을 하게 만들 확률을 최대화하는 것

## 1. Introduction
- 적대적 신경망(adversarial nets) : G가 D를 속이도록 하고, D는 어떤 sample이 G가 modeling한 분포로부터 나온 것인지 실제 data 분포로부터 나온것인지를 결정하는 법을 학습. 이와 같은 경쟁구도는 두 model이 모두 각각의 목적을 달성시키기 위해 스스로를 개선하도록 함
- (G는 D를 더 잘 속이도록 원본 data를 더 잘 모방한 분포를 학습, D는 진짜/가짜 data를 더 잘 간파하도록 data의 특징을 더 잘 파악하도록 학습)
- 실제 data 분포와 model이 생성한 data의 분포 간의 차이를 줄이는 것
- G에 random noise를 더함으로써 data를 생성하며 이를 판별하기 위해 MLP model 사용 = adversarial nets
- Generator Network : random noise vector를 입력받아 image를 만드는 upsampling 진행
- Discriminator Network : Network에 전달된 image가 실제인지 가짜인지를 판별

## 2. Adversarial Nets

![캡처](https://user-images.githubusercontent.com/80622859/188363607-c82caa6e-7f27-4487-9eac-35a174657bc7.PNG)

- x : sample image의 data, $p_data (x)$ : image data들의 확률분포, z : generator에 입력되는 noise 영역, $p_z (z)$ : noise의 확률 분포

![다운로드 (2)](https://user-images.githubusercontent.com/80622859/188364143-5b8efbcd-efeb-4ac7-b203-84edbf26fcad.png)

- Generator의 목표 : Discriminator가 구분하지 못할 정도로 실제 data와 유사한 data를 만드는 것
- Discriminator의 목표 : Generator가 만든 것과 실제 data를 잘 구분해 내는 것
