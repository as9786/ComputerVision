# Pixel Recurrent Neural Networks

## PixelRNN

![image](https://user-images.githubusercontent.com/80622859/232209288-0cc3e507-b24d-4bb0-9dfb-375cbaa2284b.png)

- i번째 pixel 값을 결정하기 위해서는 i-1 번째까지의 pixel이 주어진 상태로 판단
- 추가적으로 곱사건이므로 조건부확률은 product 연산
- 매우 복잡한 분산이 되므로 이를 해결하기 위해 신경망 사용

![image](https://user-images.githubusercontent.com/80622859/232209329-2190cbf3-df7a-48ba-b9db-ad1772796ae3.png)

- RNN을 학습할 때처럼 새로운 상태를 결정하기 위한 식은 다음과 같음

![image](https://user-images.githubusercontent.com/80622859/232209342-6335034f-761c-4368-ac15-5effbfb2f971.png)

- 새로운 상태를 판단하기 위해서는 이전 상태를 고려한 상태로 판단
- 이러한 특성을 활용해서 접근한 것이 pixelRNN
- 다만, RNN의 문제와 동일하게 연속적으로 판단해야 하기 때문에 느림

## PixelCNN

![image](https://user-images.githubusercontent.com/80622859/232209489-38c0a2d5-256c-4715-9d8e-23d04647f0b0.png)

- 현재의 pixel 값을 판단하기 위해 이전까지의 pixel까지의 정보를 가지고 CNN을 처리
- Masking strategy를 적용

![image](https://user-images.githubusercontent.com/80622859/232209532-9f267a87-2bca-4078-b06d-bcc746a5d1ef.png)

- 왼쪽의 사각형은 입력 영상의 각 pixel 값을 의미하고, 노란색은 현재 추정해야하난 pixel의 위치
- 오른쪽 사각형은 masking하는 pixel로 추정해야하는 pixel 이전까지를 1, 추정해야하는 pixel과 그 이후 pixel에 대해서는 0으로 masking
- 따라서 입력 영상에 masking을 처리하게 되면 이전 pixel value까지만 고려

![image](https://user-images.githubusercontent.com/80622859/232209632-1c5c0abd-9f99-43bb-aa68-59ebea4b4349.png)

- 영상의 경우 channel을 무시하면 1개의 pixel이 가질 수 있는 값은 0~255
- 실제 pixel value와 masking strategy를 적용한 CNN의 output value를 softmax loss를 통해 모형으로 훈련
- 직접적인 정답이 없는 비지도 학습
