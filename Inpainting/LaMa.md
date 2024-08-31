# Resolution-robust Large Mask Inpainting with Fourier Convolutions

## 서론
- Image inpainting 문제를 풀기 위해서는 영상을 잘 이해하고 잘 합성하는 것이 중요
- Inpainting을 학습할 때, 주로 실제 영상을 자동으로 masking한 dataset을 필요로 함
- 영상의 전체적인 구조를 이해하기 위해서는 큰 수용 영역이 필요
- 합성곱 신경망은 충분히 큰 수용 영역을 가지지 못함
- LaMA는 위의 문제를 3 가지 방법으로 해결
1. Fast Fourier Convolution(FFC)
2. 큰 수용 영역을 가진 분할 신경망 기반 perceptual loss 사용
3. 효과적인 mask 생성을 위해, 위 두 가지를 효과적으로 사용

## 방법

### 1. Global context within early layers

- 수용 영역을 최대한 크게 할려고 함
- FFC는 초기 층에서 전역 정보를 사용하기 위해 고안
- 기존의 합성곱 층을 사용하는 local branch, real FFT를 사용하는 global branch 두 가지로 나눔
- 
