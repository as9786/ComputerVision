# Unpaired Image-to-Image Translation using Cylce-Consistent Adversarial Networks

## GAN

![image](https://user-images.githubusercontent.com/80622859/232204328-236a0fe1-5f76-4294-ab47-5c73afe87e81.png)

- 완벽히 한 쌍을 이루는 data만 사용해 학습
- 완벽히 같은 조건을 지닌 data를 구하기는 어려움
- 말을 얼룩말로 바꾸기 위해서는 똑같은 배경의 얼룩말 사진을 학습시켜야 함

## 1.Abstract

- Image-to-image translation :  쌍의 train image를 활용해 입력과 출력을 사상하는 작업
- 쌍을 구하는 일은 쉽지 않음
- CycleGAN은 x라는 domain으로부터 얻은사진을 target domain인 y로 변환하는 방법 사용
- 한 집합에서 고유한 특징들을 포착하고 이 특징을 다른 집합으로 전이

![image](https://user-images.githubusercontent.com/80622859/232204826-d2bd22df-60b5-4083-9117-8a14c87cf97e.png)

## 2. Introduction

- Domain 간의 관계과 존재한다는 가정
- $\hat y = G(X)$
- Image X와 생성기 G가 주어졌을 때, 판별기는 $\hat y = G(X)$와 y를 구분하게 학습
- 적어도 입력에 해당하는 출력값이 domain Y에 속하는 사진처럼 학습할 수 있음
- 다만, 해당 방식은 각각의 입력과 출력이 의미있는 방식으로 짝지어지는 것을 보장 X
- Mode-collapse(어떤 입력이든 모두 같은 출력으로 도출되는 것)
- 위와 같은 문제를 해결하기 위해 cycle consistent(주기적 일성)이라는 속성 도입
- 영어로 된 문장을 불어로 번역했다면 해당 불어 문장을 다시 영어로 변역 시 본래의 문장이 도출되어야 함
- G와 F를 동시에 학습하고, $F(G(x)) \approx x $이도록 만든는 주기적 일관성 손실 추가
- 손실 함수 = 적대적 손실 + 주기적 일관성 손실

## 3. Formulation

![image](https://user-images.githubusercontent.com/80622859/232205480-224b5cfa-a61c-476e-8701-ce74c3c3335b.png)

- 2개의 생산적 적대 모형 필요
- X에서 Y의 사진을 만들어주는 생성기와 사진이 진짜인지 판단하는 판별기, 그리고 역방향 학습까지 고려
- Generator G : X->Y mapping
- Generator F : Y->X mapping
- Discriminator $D_y$ : 실제 domain Y의 image y와 G가 생성한 $\hat y = G(x)$를 구분
- Discriminator $D_x$ : 실제 domain X의 image x와 F가 생성한 $\hat x = F(y)$를 구분

## 4. Adversarial Loss
- G: X->Y와 $D_y$에 대해서는 아래와 같은 목적함수 사용

![image](https://user-images.githubusercontent.com/80622859/232205684-761be9d3-b400-4004-a879-7093badfe1ad.png)

- G는 위의 함수를 최소화, D는 위의 함수를 최대
- $min_G min_{D_y} L_{GAN}(F,D_y,X,Y)$
- 마찬가지로 F:Y->X와 $D_x$에 대해서도 다음과 같이 나타냄
-  $min_F min_{D_x} L_{GAN}(F,D_x,Y,X)$

## 5. Cycle consistency loss

![image](https://user-images.githubusercontent.com/80622859/232205824-8ed11134-4639-4c2b-9aec-f60bc77ba145.png)

- 각각 생성한 사진을 다시 원본으로 복구할 때, 원본과 복구 값 간의 거리를 구함.
- 생성된 사진이 다시 원본으로 대응될 수 있게끔 학습하면서 다양성을 최대한 제공

![image](https://user-images.githubusercontent.com/80622859/232205856-3709d9fe-07e2-490f-9ce0-37d50ad82fc6.png)

- 복원한 사진이 원본 사진과 유사함을 알 수 있음

![image](https://user-images.githubusercontent.com/80622859/232205875-6a49ac62-da91-4801-8fe8-57f24c2feab2.png)

## 6. Full objective

![image](https://user-images.githubusercontent.com/80622859/232206093-c421de8d-7a4c-4ade-8072-f7be699c4f3c.png)

- $\lambda$는 두 함수의 상대적인 중요도에 따라 결정
- 본 논문의 풀고자 하는 목표는 다음과 같음

![image](https://user-images.githubusercontent.com/80622859/232206150-50f3d91c-628f-4436-b76e-d18f58353710.png)

- X->Y GAN의 적대적 손실과 Y->X GAN의 적대적 손실을 더하고, 각각 다시 원본으로 복구하는 주기적 일관성 손실 값을 더해준 값이 최종 손실. 이를 최소화 

## 7. Limitations and Discussion

- 주로 분위기나 색상을 바꾸는 것으로 style을 학습하여 다른 사진을 생성
- 기하학적인 모향을 변경하는 데는 어려움
- Dataset의 분포가 불안정하면 제대로 생성 X

![image](https://user-images.githubusercontent.com/80622859/232206234-ce7e3c7f-1b70-4c24-9108-607e7ebeeeb8.png)

- Apple->Orange로 바꿀 때 단순히 색상만 변경
- 사람을 태운 말을 얼룩말로 바꿀 때 사람까지 얼룩말 무늬로 바뀜. 이는 학습한 data에서 사람이 얼룩말을 탄 사진이 단 한 장





