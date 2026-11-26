# Laplacian of Gaussian

- Gaussian blur를 먼저 하고, 그 결과에 Laplacian(라플라시안 2차 미분) 연산을 적용하는 기법

## 1. 배경
- 영상에서 경계선을 찾는 가장 기본적인 방법은 픽셀 값의 변화율을 구하는 1차 미분(Sobel, Prewitt filter 등)
