# PixelCNN++: Improving the pixelcnn with with discretized logistic mixture likelihood and other modifications

## 1. 초록
- Tractable likelihood를 가진 생성 모형
- 기존 PixelCNN에 몇 가지 수정을 진행
1. 256-way softmax 대신 discretized logistic mixture likelihood를 사용하여 학습 속도를 높임
2. 전체 pixel에 조건화해서 모형 구조 단순화
3. Downsampling
4. Short-Cut connection
5. Dropout => Regularize

## 2. 방법

### 2-1. Discretized logistic mixture likelihood
- PixelCNN은 모형에 유연성을 주지만 memory 부담이 큼
- VAE처럼 연속 분포를 가진 잠재 색상 값 v가 있다고 가정
- Observed sub-pixel x를 만들기 위해 양자화
- v를 모형화하는 간단한 연속 분포를 고름으로써 x를 위한 memory efficient predictive distribution을 얻음
- 연속 단일 분포를 logistic distributions의 혼합으로 골라 관찰된 이산화된 값 x의 확률을 계산
- 0과 255(Edge cases)를 제외하고 모든 sub-pixel values x에 대해 아래와 같음

<img width="650" height="162" alt="image" src="https://github.com/user-attachments/assets/b63d0257-2e93-44af-9ef8-19d5f522e31b" />

### 2-2. Conditioning on whole pixels
- 영상 내 위쪽과 왼쪽 전체 pixel을 조건으로 해서 predicted pixel의 모든 channels에 걸쳐 결합 예측 분포를 출력
- Pixel 자신에 대한 예측 분포는 simple factorized model로 해석
- Discretized mixture of logistics를 사용해 red channel 예측
- 다음으로 같은 형태의 예측 분포를 사용해 green channel 예측(같은 방식으로 blue channel까지)
- Red and green channels에 대해서만 선형 종속을 허용
- 따라서 영상 내 위치 (i, j)의 $pixel(r_{i,j}, g_{i,j}, b_{i,j})$에 대해 context $C_{i,j}$에 mixture indicator와 previous pixels로 구성된 분포 조건은 아래와 같음

<img width="718" height="138" alt="image" src="https://github.com/user-attachments/assets/6eea5008-7334-4214-9b36-a1362145b872" />

- Mixture indicator는 모든 3 channels에 걸쳐 공유

### 2-3. Downsampling versus dilated convolution
- Dilated convolution 대신 단순 downsampling 사용
- Additional short-cut connections을 통해 downsampling의 성능 개선 

<img width="1180" height="375" alt="image" src="https://github.com/user-attachments/assets/e2367670-04cc-493d-bf21-d73a2b69e0d7" />

### 2-4. Adding short-cut connections
- 
