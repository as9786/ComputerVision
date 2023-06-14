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

## 손실 함수

- p : real domain, a : animation domain
- Gr
