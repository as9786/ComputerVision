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

### Image data에 대한 확률분포
- Image data는 다차원 특징 공간의 한 점으로 표현. Image 분포를 근사하는 model을 학습할 수 있음
- ex) 사람의 얼굴에는 통계적인 평균치가 존재 -> model은 이를 수치적으로 표현
- Image에서는 다양한 특징들이 각각의 확률 변수가 되는 분포. 다변수 확률분포(Multivariate probability distribution)

![330px-Multivariate_Gaussian](https://user-images.githubusercontent.com/80622859/188365253-56f72c76-64a1-469b-bbdd-62583a0559ce.png)

### Genrative Models
- 실존하지 않지만 있을 법한 data를 생성할 수 있는 model
- 여러 개의 변수에 대한 결합 확률 분포의 통계적 모형


## 1. Introduction
- 적대적 신경망(adversarial nets) : G가 D를 속이도록 하고, D는 어떤 sample이 G가 modeling한 분포로부터 나온 것인지 실제 data 분포로부터 나온것인지를 결정하는 법을 학습. 이와 같은 경쟁구도는 두 model이 모두 각각의 목적을 달성시키기 위해 스스로를 개선하도록 함
- (G는 D를 더 잘 속이도록 원본 data를 더 잘 모방한 분포를 학습, D는 진짜/가짜 data를 더 잘 간파하도록 data의 특징을 더 잘 파악하도록 학습)
- 실제 data 분포와 model이 생성한 data의 분포 간의 차이를 줄이는 것
- G에 random noise를 더함으로써 data를 생성하며 이를 판별하기 위해 MLP model 사용 = adversarial nets
- Generator Network : random noise vector를 입력받아 image를 만드는 upsampling 진행
- Discriminator Network : Network에 전달된 image가 실제인지 가짜인지를 판별

## 2. Adversarial Nets

![캡처](https://user-images.githubusercontent.com/80622859/188363607-c82caa6e-7f27-4487-9eac-35a174657bc7.PNG)

- x : sample image의 data, $p_data (x)$ : image data들의 확률분포, z : generator에 입력되는 noise 영역, $p_z (z)$ : noise의 확률 분포, G(z) : new data instance, D(x) : training data로부터 나왔는지에 대한 확률(진짜 : 1, 가짜 : 0)

![다운로드 (2)](https://user-images.githubusercontent.com/80622859/188364143-5b8efbcd-efeb-4ac7-b203-84edbf26fcad.png)

- Generator의 목표 : Discriminator가 구분하지 못할 정도로 실제 data와 유사한 data를 만드는 것
- Discriminator의 목표 : Generator가 만든 것과 실제 data를 잘 구분해 내는 것

<img width="722" alt="images_minkyu4506_post_746ecd2c-b61d-47d2-aa22-651006042850_스크린샷 2021-09-05 오후 3 08 27" src="https://user-images.githubusercontent.com/80622859/188365663-24c3a2bf-1387-436f-bab7-7e8206ddc5ba.png">

- 초록색 분포 : generative model의 분포, 검정색 분포 : 원본 data의 분포, 파란색 분포 : discriminator의 분포
- 시간이 지나면서 generative model G가 원본 data의 분포를 학습
- 학습이 잘 되었다면 통계적으로 평균적인 특징을 가지는 data를 쉽게 생성 가능

### GAN의 수렴 과정
- 생성자의 분포가 원본 data의 분포에 수렴하도록 만드는 것. $P_g$ -> $P_{data}$, D(G(z))->1/2(학습이 다 이루어진 후에는 진짜와 가짜를 구별할 수 없기 때문에 50% 확률값을 가지게 됨 = 판별자가 더 이상 구별을 못함 

## Global Optimality 

### 판별기의 global optimum point
- G가 고정되어 있을 때

![render](https://user-images.githubusercontent.com/80622859/188366954-6b231fce-2dbe-4afa-827e-c5380b70dfbe.png)

![render (1)](https://user-images.githubusercontent.com/80622859/188367457-83730db2-c210-46f7-8ac3-c93f2ea5ae97.png)

![render (2)](https://user-images.githubusercontent.com/80622859/188367611-d6b09bcf-d5ab-4e1f-898f-db479688bbd0.png)

### 생성기의 global optimum point
- Global optimum point is $p_g = p_{data}$

![render (3)](https://user-images.githubusercontent.com/80622859/188368571-d742b82d-c328-469b-bbdb-0027b7d7a73c.png)

#### KL divergence(쿨백-라이블러 발산)
- 두 확률분포의 차이를 보여주는 식

![eq34](https://user-images.githubusercontent.com/80622859/188368742-7a39e459-38c2-4d7e-b2cd-bf470b007399.png)

#### Jensen-Shannon Divergence
- KL divergence에서 나온 개념을 distance metrics로 사용하기 위한 변환식
- 두 분포가 동일할 때는 JSD 값은 0

![render (4)](https://user-images.githubusercontent.com/80622859/188369100-65af428e-13ea-4702-8e9a-0ca0fc1ef7c5.png)

- 위의 증명들은 model 학습이 잘 되었을 때 위와 같은 값을 가져야한다는 것을 의미.
- 학습이 수렴하는 방법에 관한 식 X
- 역전파 수행

## GAN 알고리즘
- 판별기 학습 후 -> 생성기 학습
- 생성기 학습 후 -> 판별기 학습



