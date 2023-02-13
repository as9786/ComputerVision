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
