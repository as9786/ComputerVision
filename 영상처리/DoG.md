# Difference of Gaussians

## 1. 개념
- 서로 다른 표준편차를 가진 두 개의 gaussian kernel로 영상을 각각 smoothing 한 뒤, 두 결과의 차이를 구하는 연산

$$DoG(x,y)=I(x,y) \ast G(x,y,\sigma_1) - I(x,y) \ast G(x,y,\sigma_2)$$

## 2. 사용 이유

### 2-1. Band-Pass filter(대역 통과 필터)
- Gaussian blur는 low-pass filter(저주파 통과 필터)로, 영상을 뭉툭하게 만들어 고주파 성분(noise, 미세한 질감 등)을 제거
- 두 개 서로 다른 low pass filter의 차이를 구하면, 특정 주파수 대역의 성분만 남개 되는 대역 통과 필터로 남게 됨

### 2-2. 가장자리 검출
- 영상에서 값이 급격하게 변하는 경계썬이나 특징적인 점을 도드라지게 만들어 줌

### 2-3. LoG(Laplacian of Gaussian)의 고속 근사화 
