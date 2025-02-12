- 사진의 경계를 검출하기 위해 사용
- Image pixel 값의 급격한 변화를 검출하고, 그 급격한 변화를 edge라고 함

![image](https://github.com/user-attachments/assets/4b651496-2e51-4923-bc59-8616274a7c6a)

- h =1 : 인접 pixel과의 거리
- f(x) : 인접 pixel과의 값의 차이

# 목적
- 객체를 탐지하기 위해 사용
- 경계를 검출하기 위해 사용

# 원리

![image](https://github.com/user-attachments/assets/b7f0f82e-d914-49a5-9c10-d81f29140861)

- Horizontal Sobel filter. x축을 기준으로 좌 우 pixel 간의 미분을 사용

![image](https://github.com/user-attachments/assets/62d871b7-c7ff-4a9c-8802-f1754c0db191)

- Vertical Sobel filter. y축을 기준으로 좌우 pixel 간의 미분을 사용
- 수평 수직 경계를 검출기 위해서는 수평과 수직 둘 다 사용. $\sqrt{sobel_{horizontal}^2 + sobel_{vertical}_^2}$



