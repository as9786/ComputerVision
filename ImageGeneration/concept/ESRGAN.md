# ESRGAN : Enhanced Super-Resolution Generative Adversarial Network

- SRGAN의 개선

## 서론

- SRGAN은 여전히 정답 영상과는 차이가 있음

![image](https://github.com/as9786/ComputerVision/assets/80622859/77ee9448-afa1-4546-b771-97bbb7ec5ed1)

### 1. Residual-in-Residual Dense Block

- SRGAN은 배치 정규화 사용
- Training dataset과 test dataset의 통계값이 많이 달라서 배치 정규화를 사용 시 일반화 성능 하락
- Range flexibility가 제거
- 밝기의 범위가 좁아짐
- BN layer 제거 => computational complexity와 memory usage에서 많은 이점

![image](https://github.com/as9786/ComputerVision/assets/80622859/2b482d36-bcdc-4244-873f-47d050cacf99)

![image](https://github.com/as9786/ComputerVision/assets/80622859/1c036312-eafe-48f7-be73-a8bbc8223600)
