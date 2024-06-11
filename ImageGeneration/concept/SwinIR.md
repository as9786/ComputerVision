# SwinIR: Image Restoration Using Swin Transformer

## 서론
- 영상 복원 : 저해상도 영상을 고해상도 영상으로 재구성
- Denoising task & Super Resolution
- 오랫 동안 합성곱 신경망으로 해결
- 몇 가지 단점
1. Convolution kernel은 shared parameters로써 영상 영역에 같은 kernel이 사용됨(Content-independent between images and convolutional kernel)
2. Long-range dependency를 효과적으로 modeling할 수 없음

- 위와 같은 문제를 해결하기 위하여 ViT 사용
- 하지만 ViT는 영상들을 patch 단위로 나누면서 각 patch를 독립적으로 처리하기 때문에 다른 문제가 발생
1. Patch 단위로 attention을 하기 때문에 border pixels가 neighboring pixels에 대한 정보를 이용 X
2. 복원된 영상에 border artifacts가 생길 수 있음(이는 overlapping patch를 통해서 해결할 수 있지만 추가 연산 필요)

- 위와 같은 문제들은 patch 내에서만 attention을 한다는 것이 큰 원인
- 그래서 swin transformer를 사용하여 해결

## 방법

![image](https://github.com/as9786/ComputerVision/assets/80622859/58344646-1116-48b4-b75b-95715ca32d4a)

### Shallow feature extraction module 
- 합성곱 신경망을 사용하여 shallow feature를 추출하며, reconstruction module에 직접 전달되어 low-frequency information이 보존되도록 함
- 저해상도 영상에 3 x 3 합성곱 층을 사용하여 특징 추출
- Shallow layer에 합성곱 신경망을 사용하는 이유는 합성곱이 저차원 정보를 처리하는데 좋은 성능을 보임
- 간단하게 입력 영상을 high-dimensional feature space mapping

### Deep feature extraction module
- Residual Swin Transformer Blocks(RSTB)
- 여러 개의 swin transformer layers를 통해 local attention과 cross-window integration으로 deep feature 추출
- Feature enhancement를 위해 층 끝에 합성곱층을 추가하였고, 특징 집계를 위해 residual connection 사용
- RSTB와 3 x 3 합성곱 층으로 구성
- 입력으로는 shallow feature extraction module의 출력이 들어감
- 마지막에 합성곱 층을 사용함으로써 귀납적 편향을 더해줌

#### RSTB
- Swin transformer block에 residual connection과 합성곱층을 더해준 것
- 두 가지 장점
1. 합성곱 층의 spatially invariant filters(영상 지역마다 같은 kernel을 가지는 것)가 SwinIR의 translation equivariance(넣는 입력에 따라 출력 값이 변함)를 향상
2. Residual connection을 통해 다른 level의 feature를 합쳐줌

### Reconstruction module
- Shallow와 deep features를 합쳐서 최종 출력
- Shallow feature와 deep feature를 합쳐주는 역할

![image](https://github.com/as9786/ComputerVision/assets/80622859/645621f7-335a-4ad5-9fb3-035b6fb95052)

- $H_{rec}$은 작업에 따라 달라짐
- SR일 경우, sub-pixel convolution layer를 통해 upsampling
- 그 외일 경우, 단일 합성곱 층

## 손실 함수

- SR : L1 pixel loss
- 그 외 : Charbonnier loss

![image](https://github.com/as9786/ComputerVision/assets/80622859/331c64e0-8ca3-47bc-b3c0-535d00f367a7)





