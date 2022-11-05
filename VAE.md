# Variational AutoEncoders

- 신경망에서 차원을 압축하기 위해 고안된 방법
- Encoder-Decoder 환경에서 점진적으로 최적화를 통해 입력 값에서 필요한 정보를 압축한 vector를 encoding 하는 것이 목표

![캡처](https://user-images.githubusercontent.com/80622859/200107402-579eeb64-5ecb-4702-9e9c-9897efce2f44.PNG)

- AE는 맥락을 가지는 image를 생성하는 작업에 활용
- Encoding된 vector는 어떠한 특징(ex. 피부색, 머리색 등)을 담은 latent variable
- Decoding 시 만들고 싶은 특징에 대한 latent space에서 sampling한 vector를 활용하면 원하는 특정에 따른 image를 만들 수 있음
- 하지만 잘 통제된 latent vector를 찾는 것은 쉽지 않음 => VAE
- Decoder를 생성 목적으로 사용하기 위해서는 잠재 공간이 정제되어야 한다는 전제조건
- 이러한 정제성을 확보하기 위해 학습 과정에서 AE를 정규화하여 과적합을 방지하고, 잠재 공간이 생성에 적합한 성질을 가지도록 하는 것이 VAE의 핵심

- VAE에서는 입력이 잠재 공간에 대한 확률분포로 encoding
- 잠재 공간으로부터의 점은 해당 분포로부터 추출되고, 추출된 점이 decoding 되어 재구성 손실을 계산

![캡처](https://user-images.githubusercontent.com/80622859/200107562-3f12625c-a778-4e36-a701-a3b2e39316fe.PNG)

# Discrete Variational AutoEncoders
- 잠재 변수가 이산일 경우
- 이산 분포에 대한 역전파는 일반적으로 불가능하기 때문에 이러한 모형은 학습이 어려움
- 이산 잠재 변수를 사용하여 VAE를 역전파를 통해 학습할 수 있는 방법을 제안

![캡처](https://user-images.githubusercontent.com/80622859/200107632-f5d430f4-8d8a-45c7-bce2-92f44073a596.PNG)


