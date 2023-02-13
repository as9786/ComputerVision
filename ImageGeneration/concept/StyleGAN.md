# StyleGAN : A Style-Based Generator Architecture for Generative Adversarial Network

## Abstract 

- 생성기를 통해 생성되는 image는 여전히 black box를 파악할 수 없음
- Image의 속성을 조절하기가 어려움
- Image quality가 불안정하여 부자연스러운 image도 다수 생성
- Style transfer 기반에 새로운 생성기
- Image를 style의 조합으로 보고, 생성기의 각 층마다 style 정보를 입힘
- 각 층에 추가되는 style은 coarse feature(성별, pose 등)부터 fine detail(머리색,피부 등)까지 다른 level의 시각적 속성을 조절
- 훨씬 안정적이고 높은 질의 image 생성
- PGGAN based

## Proposed method

### Mapping Network

![image](https://user-images.githubusercontent.com/80622859/218441244-0775da62-4fb9-4bff-9b62-a022d9da1853.png)

- Input vector Z로부터 직접 image를 생성하는 것이 아니라 mapping network를 거쳐서 intermediate vector W로 먼저 변환한 후 생성
- 기존 방법처럼 학습 시 (a)처럼 고정된 입력 분포에 training image distribution을 맞춰야 함
- (b)의 방식은 시각적 속성이 입력 공간에 비선형으로 사상되고, input vector로 시각적 속성들을 조절하기가 어려워짐
- (c)처럼 mapping network를 사용할 경우 W는 고정된 분포를 따를 필요가 없어지기 때문에, training data를 보다 유동적인 공간(intermediate latent space)에 사상 가능
- W를 이용하여 시각적 속성을 조절하기 용이해짐(Disentanglement)

### Style Modules

![image](https://user-images.githubusercontent.com/80622859/218441866-9ac9ca3c-de7f-475e-9cd4-01e4fc669332.png)

- ADaIN layer를 사용하여서 style 정보를 입힐 수 있도록 만듦
- 하나의 image를 생성할 때 여러 개의 style 정보가 층을 거칠 때마다 입혀질 수 있도록 하는 방식
- 학습시킬 parameter 필요 X
- Feed forward 방식의 style transfer network에서 사용되어 좋은 성능을 보임
- Instance norm은 하나의 image에 대해서 정규화를 수행하기 때문에 batch size가 N이라고 channel 단위로 정규화를 수행
- 정규화를 수행한 뒤 별도의 style 정보를 받아서 feature 상의 통계량을 바꾸는 방식으로 style을 입힌 것
- Adaptive Instance Normalization

![image](https://user-images.githubusercontent.com/80622859/218443819-dd2739c6-3039-45a3-89ac-6631bf7f4a8f.png)

- Mapping network를 통해 latent vector인 W를 뽑은 다음에 신경망이 image를 생성하는 과정에서 style을 입힘
- W는 선형 변환을 거쳐서 AdaIN에 들어가는 style 정보를 만듦
- 합성곱 이후마다 AdaIN을 통해 style이 입혀짐
- 특정 층에서 입혀진 style은 다음 합성곱층에만 영향을 줌
- 각 층의 style이 특정한 시각적 속성만을 담당하게 됨

### Noise

![image](https://user-images.githubusercontent.com/80622859/218444274-2aefa188-12c7-4714-98cd-88e38a460152.png)

- Stocastic variation을 처리할 수 있도록 구성
- 하나의 image에 포함될 수 있는 다양한 확률적인 측면을 조절할 수 있음
- 같은 사람에 대한 image라 할지라도 머리카락, 수염, 주름 등 stochastic 하다고 볼 수 있는 요소가 많이 존재
- 각 층마다 random noise 추가
- 더욱 사실적인 image 생성, Input latent vector는 image의 중요한 정보를 표현하는데 집중, 조절도 쉬워짐

![image](https://user-images.githubusercontent.com/80622859/218444551-f5de79b7-2830-4a6d-9fa9-7bf6351a29eb.png)

- Style은 high-level global attributes를 조절, noise는 stochastic variation을 조절
- (a) 모든 층에 noise 적용, (b) stochastic한 정보를 적용 X, (c) 뒷 쪽 층에만 noise 추가, (d) 앞 쪽에 noise 추가

![image](https://user-images.githubusercontent.com/80622859/218444857-cfdfb8aa-8dbd-4234-a647-0f82446d0fb5.png)

- 층의 위치에 따라 영향력이 다름
- Coarse, middle, fine style
- 앞 쪽 4개의 층이 coarse, 그 뒤 4개의 층이 middle, 나머지가 fine style

