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

- Contracting path : Size가 줄어드는 경로(왼쪽)
- Expansive path : Size가 늘어나는 경로(오른쪽)

### Contracting path(수축 구간)

- 전형적인 CNN

![image](https://user-images.githubusercontent.com/80622859/213978011-599fb1bd-d272-4194-9926-06fce55393d2.png)

- 특성 추출을 하며 점차 feature map의 크기가 줄어드는 구조
- 3 x 3 filter를 가진 합성곱층을 2번 적용하며 이 과정에서 활성화 함수로는 ReLU 사용
- Max pooling(pool_size = (2,2), stride = 2) 사용
- Downsampling
- Downsampling 할 때마다 channel의 크기를 2배 늘림

### Bottle Nect(전환 구간)

- 3 x 3 합성곱층, ReLU, batch noramliazaion, dropout
- Dropout을 통해 일반화

### Expansive path(확장 경로)

- Contracting path와 좌우로 대칭되는 구조
- 3 x 3 filter의 합성곱층을 2번 적용한 뒤 feature map의 너비와 높이를 2배로 늘림(Upsampling)
- Upsampling 시 마다 channel의 크기를 반으로 줄임
- 반으로 줄인 feature map에 contracting path에서 같은 층에 있는 feature map과 합쳐줌(Concatenation, copy and crop)
- Crop을 해주는 이유로는 feature map의 크기가 다르기 때문
- 마지막 층에는 1 x 1 합성곱층을 사용해 우리가 분류할 class의 개수 만큼의 크기로 channel의 수를 줄여줌

- 총 23 개의 CNN layer 

## Training

### Overlap-tile strategy

- 큰 image를 겹치는 부분이 있도록 일정 크기로 나누고 모형의 입력으로 활용

![image](https://user-images.githubusercontent.com/80622859/213980646-47d1cc44-2fe6-4ca4-99df-4aded2bed346.png)

### Mirroring Extrapolate

![image](https://user-images.githubusercontent.com/80622859/213980929-ab35234b-a447-4689-89b5-7bd43e4ecb75.png)

- Image 경계에 위치한 image를 복사하고 좌우 반전을 통해 mirror image를 생성한 후 원본 image 주변에 붙여 입력으로 사용

### Weight Loss

- GPU를 최대한 활용하기 위해 image file을 여러 개의 batch로 나눔
- 학습용 dataset의 단위가 image가 아닌 image의 일부
- Momentum = 0.99 => 현재 시점의 가중치를 상당히 많이 반영
- Energy function : 마지막에 얻은 feature map에 pixel 단위로 softmax 연산을 수행하고, 여기에 cross entropy loss function을 적용

![image](https://user-images.githubusercontent.com/80622859/213978999-6776e304-620d-42ce-882d-2886e12a6797.png)

- x : feature map에 있는 각 pixel, w(x) : weight map, pixel 별로 가중치를 부과하는 역할

![image](https://user-images.githubusercontent.com/80622859/213979065-5b3556d6-d70f-4349-8bfc-62ac93e10d99.png)

- 같은 세포라도 pixel 값에 차이가 있으니 그러한 부분을 보완해 줌
- d1 : 가장 가까운 class의 테두리와의 거리, d2 : 두 번째로 가까운 class의 테두리와의 거리
- $\sigma = 5, w_0 = 10$
- w(x)는 pixel x와 경계의 거리가 가까우면 큰 값을 갖게 되므로 해당 pixel의 loss 비중이 커지게 됨 => 학습 시 경계에 해당하는 pixel을 잘 학습

![image](https://user-images.githubusercontent.com/80622859/213979231-cdbfa6e5-f02e-4b15-8a3a-5e15f9861b51.png)

## Data Augmentation

- Shift, rotation
- Random-elastic deformation

![image](https://user-images.githubusercontent.com/80622859/213980298-faa5f22a-397c-4bde-879b-4f7f01933a10.png)
