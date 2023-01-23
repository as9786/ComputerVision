# U-Net : Convolutional Networks for Biomedical Image Segmentation

- Biomedical image 분석에 사용한 모형

![image](https://user-images.githubusercontent.com/80622859/213976856-76a2eef2-6e00-4660-93ff-c6483686df6d.png)

- 위와 같이 세포를 찍은 사진
- 사진 속에 세포를 구분하는 일 수행

![image](https://user-images.githubusercontent.com/80622859/213976898-ccaab684-9d60-44f2-9c76-7b819775618c.png)

## Introduction

- 위의 세포 분류에서 보듯 한 image 안에 여러 개의 세포들이 들어있기 때문에 pixel 별로 class 분류를 해야하는 localization이 포함된 분류가 필요
- 본 논문에서는 pixel과 pixel 주변의 영역을 받아 pixel에 담긴 정보가 어떤 객체인지를 판단하는 방식을 사용
- 이 경우 학습 데이터는 image 단위가 아닌 image 속 일부(patch)가 한 단위가 되기 때문에 훨씬 풍부한 dataset을 구현할 수 있음
- 즉, 적은 학습 데이터로도 훌륭한 성능을 낼 수 있음
- 하지만, patch별 연산으로 인해 학습 속도가 느리고, 서로 중복된 영역을 가지는 patch들이 많아 중복된 예측 결과도 나온다고 함
- Patch의 크기가 크면 더 많은 pooling layer을 요구하여 localization accuracy가 떨어짐
- Patch의 크기가 작으면 little context만 알 수 있음
- FCN의 구조를 개선하여 만듦
1. 특성을 추출하여 점차 해상독 떨어지는 feature map 얻음
2. Upsampling
3. Upsampling 시 CNN에서 축소하는 과정에서 얻은 같은 해상도의 feature map을 더해줌

![image](https://user-images.githubusercontent.com/80622859/213977490-6981645e-b45c-467e-be56-4ed035708847.png)

- U자 형태
- 전결합 계층을 사용하지 않음 -> patch에서 얻은 정보만 가지고 patch에서 분류를 수행할 수 있고 이 과정을 image 전체에 대해 시행
- Memory 효율적
- Data augmentation

## Network Architecture
