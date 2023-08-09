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

- Depth convolution 이후에 pointwise convolution 수행

![image](https://github.com/as9786/ComputerVision/assets/80622859/77f75af6-a82f-4154-bb5e-6d609a740523)

![image](https://github.com/as9786/ComputerVision/assets/80622859/1b837fd7-1ae0-49aa-936a-f2786bb2fb37)

- Depthwise convolution은 input channel에 각각 독립적으로 3x3 conv 수행
- Pointwise convolution은 모든 channel에 1x1 conv 수행, channel 수 조절
- Xception은 depthwise separable convolution을 수정해서 inception module에 사용

## 3. Modified Depthwise Separable Convolution(Extreme Inception)

![image](https://github.com/as9786/ComputerVision/assets/80622859/39abd21e-7040-4635-a114-180b3f71523f)

![image](https://github.com/as9786/ComputerVision/assets/80622859/371d1eb9-1412-4ec3-a43d-6d3c2171223a)

- Pointwise convolution 이후에 depthwise convolution 사용
- Channel은 n개의 segment로 나뉨
- 나눠진 segment 별로 depthwise convolution 수행
- 연산의 순서가 다름
- 비선형 함수를 사용하지 않음

![image](https://github.com/as9786/ComputerVision/assets/80622859/3dceae6c-1d8c-4ef5-b443-927fdff10fec)

- 비선형 함수를 사용하지 않았을 시, 성능이 더 좋음

## Xception architecture

![image](https://github.com/as9786/ComputerVision/assets/80622859/33df1b39-7043-4380-809c-4c7d769ebbe9)

- 14개의 module로 구성, 36 개의 합성곱층 존재
- Skip-connection 사용
- 입력은 entry flow를 거쳐서 middle flow를 8번 거침
- 최종적으로 exit flow

