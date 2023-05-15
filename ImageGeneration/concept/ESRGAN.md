# ESRGAN : Enhanced Super-Resolution Generative Adversarial Network

- SRGAN의 개선
- SRGAN은 여전히 정답 영상과는 차이가 있음

![image](https://github.com/as9786/ComputerVision/assets/80622859/77ee9448-afa1-4546-b771-97bbb7ec5ed1)

## 1. Residual-in-Residual Dense Block

- SRGAN은 배치 정규화 사용
- Training dataset과 test dataset의 통계값이 많이 달라서 배치 정규화를 사용 시 일반화 성능 하락
- Range flexibility가 제거
- 밝기의 범위가 좁아짐
- BN layer 제거 => computational complexity와 memory usage에서 많은 이점

![image](https://github.com/as9786/ComputerVision/assets/80622859/2b482d36-bcdc-4244-873f-47d050cacf99)

![image](https://github.com/as9786/ComputerVision/assets/80622859/1c036312-eafe-48f7-be73-a8bbc8223600)

- 기존 SRResNet 구조는 그대로 가져가면서 block만 교체
- BN layer가 빠지고 단순히 residual connection만 사용한 것이 아닌 dense connection도 사용
- BN 유뮤 

![image](https://github.com/as9786/ComputerVision/assets/80622859/4077b4ae-9fe0-4fe9-8c12-9b3e34639002)

## 2. Relativistic GAN

- 판별기가 a가 b보다 진짜 같은지를 판단

![image](https://github.com/as9786/ComputerVision/assets/80622859/d1109b4b-7d3c-47cf-86bc-12482c73564f)

- 손실함수
- 판별기 손실 함수
- 
![image](https://github.com/as9786/ComputerVision/assets/80622859/1ec2601b-b11e-4c97-97c9-112bcedd5051)

- 생성기 손실 함수

![image](https://github.com/as9786/ComputerVision/assets/80622859/a48e5583-ba17-4604-94a8-9fd7e58fecff)

- 기존의 GAN은 생성기에서 real image가 영향을 주지 않지만, relativistic GAN에서는 real image가 생성기에 영향을 줌

- SRGAN과 RaGAN

![image](https://github.com/as9786/ComputerVision/assets/80622859/14a1a04e-bda5-49e6-a0f4-da82b31a8bc5)

## 3. Perceptual Loss

- SRGAN에서는 perceptual loss를 VGG loss와 GAN loss를 통틀어서 언급
- 본 논문에서는 VGG loss만 perceptual loss
- 기존에는 activation 이후의 feature map을 사용. 본 논문에서는 activation 이전의 feature map 사용
- Activation 이후의 feature map을 사용하면 층이 깊어질 수록 sparse 해진다는 단점
- 정답 영상과 밝기 복원에 있어서도 성능 차이

![image](https://github.com/as9786/ComputerVision/assets/80622859/23d40e0a-c9f3-4352-b29a-3aaa5c5c2822)

- 분류를 위해 학습된 VGG가 아닌 material recognition을 위한 미세 조정된 VGG 사용
- Perceptual loss에 대한 연구가 앞으로도 중요

## 4. Total loss

![image](https://github.com/as9786/ComputerVision/assets/80622859/0fa4eda0-3beb-4a6b-8f95-811bf65cb539)

- L1 lㄷoss 사용
- Local optima를 피함
- 초기에 완전한 fake image를 생성하지 않아서 학습을 texture에 집중할 수 있도록 해줌

## 5. Network Interpolation

- PSNR-oriented 방식으로 학습한 초기 가중치와 최종 가중치를 보간법을 이용하여 사용

![image](https://github.com/as9786/ComputerVision/assets/80622859/6f30d169-0d0a-4910-a9d8-f479a25317a8)

- 단순히 가중치를 곱해서 더함

![image](https://github.com/as9786/ComputerVision/assets/80622859/5f296281-0af2-4096-ac06-c36d71c642ed)

## 결론

- 평가 지표로는 우수하지 않지만 직접 눈으로 봤을 때 훨신 나음

![image](https://github.com/as9786/ComputerVision/assets/80622859/45207bd0-2eb9-4a07-b853-1b64f288b68a)



