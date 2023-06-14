# AnimeGAN : A Novel Lightweight GAN for Photo Animation

![image](https://github.com/as9786/ComputerVision/assets/80622859/3325e55f-3583-4399-ba15-dde77f2deb84)

## 생성기

![image](https://github.com/as9786/ComputerVision/assets/80622859/d8f54ad8-cf93-4dbc-868f-4abb29060edb)

- 대칭적 구조
- 표준 합성곱, depth wise separable convolution, inverted residual blocks(IRBs), upsampling/downsampling module로 구성
- 가장 마지막 층에는 1 x 1 convolution filter

### Down-Conv

![image](https://github.com/as9786/ComputerVision/assets/80622859/54e72eb6-f184-4541-8a7c-8a5d39aa369a)

- Max-pooling을 사용하여 downsampling을 하면 특징 정보가 손실
- 위의 문제를 해결
- Depth separable convolution을 통해서 나온 값과 resize를 통해서 나온 값을 더해주는 개념

### Up-Conv
- Feature map의 해상도를 키우는 역할

### 8 consecutive & identical IRBs
- 신경망 주앙에 IRBs module을 두어서 생성기의 가중치들을 줄임
- Point-wise convolution(c=512) + Depth-wise convolution(c=512) + Point-wise convolution(c=256)
- Depth wise separable convolution = Point-wise convolution + Depth-wise convolution이므로 사실상 DSConv를 사용했다고 봐도 됨


## 판별기
- 일반적인 합성곱 신경망
- Spectral normalization을 통해 훈련을 안정적으로 진행

### Spectral normalization
- 각 층의 가중치의 최댓값 = Lipschitz norm
- Lipschitz norm은 함수의 기울기를 일정 미만으로 제한
- 각 층의 가중치를 Lipschitz norm으로 나누어줌
- 
## 손실 함수

- p : real domain, a : animation domain

- Color animation image a에서 grayscale Gram matrix를 취해 gray scale image 생성

### Gram matrix

![image](https://github.com/as9786/ComputerVision/assets/80622859/a4c7c473-245d-47fb-84c8-2cfc4a70a112)

- l : 층
- F : Filter
- i,j : Filter index
- Pixel 별 공분산을 구하게 됨
- x라는 입력이 있다고 하자(x는 사진이며, 2차원)
- 이를 1차원으로 평탄화

![image](https://github.com/as9786/ComputerVision/assets/80622859/5c568e75-a769-47ff-a593-c49d22d388c4)

- Filter를 통과하면 아래와 같음(Filter는 2개)

![image](https://github.com/as9786/ComputerVision/assets/80622859/8eb87a53-9560-4a00-b77c-01b77adb9d51)

- 위의 공식에 대입하면 아래와 같음

![image](https://github.com/as9786/ComputerVision/assets/80622859/34a663f1-08db-4678-a740-217a67458ee3)

- 최종적 손실 함수

![image](https://github.com/as9786/ComputerVision/assets/80622859/9f73271d-3cdd-4e72-85f9-30c9440bad9b)

![image](https://github.com/as9786/ComputerVision/assets/80622859/682b61ce-12a2-4ea8-8392-d201f273c42a)

### Content loss
- 생성된 사진이 입력 사진의 content를 유지시키도록 함
- Pre-trained VGG19 사용

![image](https://github.com/as9786/ComputerVision/assets/80622859/6eada111-28db-4ef3-8865-7fb132e803c3)

### Grayscale style loss

- 생성된 사진의 질감이나 선 등이 anime style이 되도록 강제

![image](https://github.com/as9786/ComputerVision/assets/80622859/bd3c27c6-9eb5-4f48-8b9e-85939f64e330)

### Color recon loss

- 생성된 사진과 원본 사진의 색깔이 유사하도록
- RGB 대신 YUV 사용
- Y(밝기)/U(청색 색차)V(적색 색차)
- 색깔에 해당하는 U, V channel에 대해서는 Huber loss를 사용 -> 색깔에서의 차이가 크면 보다 penalty 부여
- Y channel에 대해서느 L1 loss

![image](https://github.com/as9786/ComputerVision/assets/80622859/a5b018af-642c-4142-99be-41b7cb1a11ac)




