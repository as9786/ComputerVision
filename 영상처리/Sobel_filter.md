- 사진의 경계를 검출하기 위해 사용
- Image pixel 값의 급격한 변화를 검출하고, 그 급격한 변화를 edge라고 함
- 1차 미분을 사용하여 영상에서 밝기가 가장 급격하게 변하는 구간과 그 방향을 직관적으로 찾아내는 기법

# Sobel filter
- 가로 방향과 세로 바향의 밝기 변화율을 각각 계산하는 필터
- 단순히 인접한 픽셀과의 차이만 구하면 노이즈에 매우 취약. Sobel filter는 중심 픽셀 주변에 gaussian blur와 유사한 가중치를 주면서 미분을 동시에 수행

![image](https://github.com/user-attachments/assets/4b651496-2e51-4923-bc59-8616274a7c6a)

- h =1 : 인접 pixel과의 거리
- f(x) : 인접 pixel과의 값의 차이

## 목적
- 객체를 탐지하기 위해 사용
- 경계를 검출하기 위해 사용

## 원리

![image](https://github.com/user-attachments/assets/b7f0f82e-d914-49a5-9c10-d81f29140861)

- Horizontal Sobel filter. x축을 기준으로 좌 우 pixel 간의 미분을 사용

![image](https://github.com/user-attachments/assets/62d871b7-c7ff-4a9c-8802-f1754c0db191)

- Vertical Sobel filter. y축을 기준으로 좌우 pixel 간의 미분을 사용
- 수평 수직 경계를 검출기 위해서는 수평과 수직 둘 다 사용. $\sqrt{sobel_{horizontal}^2 + sobel_{vertical}^2}$
- 경계선 방향(Gradient direction) : 밝기가 어느 방향으로 급격하게 변하는지 각도를 구함. $\theta=arctan(\frac{G_y}{G_x})$
- 



