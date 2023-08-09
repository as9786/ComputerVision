# Xception : Deep Learning with Depthwise Separable Convolutions

- Inception module에 대한 고찰로 탄생
- Cross-channel correlations와 spatial correlations를 독립적으로 계산하기 위해 고안
- 새로운 inception module 제안

## 1. Inception hypothesis

- Inception v3에서 사용하는 일반적인 inception module

![image](https://github.com/as9786/ComputerVision/assets/80622859/f496383d-4fb4-4859-acd6-b4ffaa10ec79)

![image](https://github.com/as9786/ComputerVision/assets/80622859/96e8907d-7bb2-4954-a6c4-720f8f7c069b)

- 1 x 1 conv 이후에 3 x3 conv 연산이 수행 = Cross-channel correlations와 spatial correlations을 독립적으로 수행
- 위의 연산이 inception module의 성능이 좋은 이유
- Xception은 완벽히 cross-channel correlation과 spatial correlations을 독립적으로 계산하고 사상하기 위해 고안

## 2. Depthwise Separable Convolution

- 
