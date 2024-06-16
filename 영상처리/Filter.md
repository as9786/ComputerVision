# Mean filter

- Mean filter는 대상 점을 주변 pixel들의 평균값들로 대체 => Image blurring effect
- Filter의 모든 값이 동일
- Pixel 값의 급격한 변화가 줄어들어 날카로운 가장자리가 무뎌지고 noise의 영향이 크게 사라짐
- Mask의 크기가 커지면 커질수록 더욱 부드러운 느낌의 영상을 생성(대신에 연산량이 크게 증가)
- 이러한 특성은 대상 점과 가까운 pixel이 먼 pixel보다 더 연관이 있다는 사실을 반영하지 않음
- 가까운 pixel에 더 많은 가중치를 줄 필요가 있음

# Gaussian filter
- Mean filter의 문제점을 해결하기 위해 등장
- Gaussain distribution function을 근사하여 생성한 filter mask를 사용하는 filtering 기법
- Mean filter보다 자연스러운 흐릿함 생성

## Gaussian distribution
- 평균을 중심으로 좌우 대칭의 종 모양을 갖는 확률 분포(정규 분포라고도 함)
- 평균 근방에서 분포가 가장 많이 발생하고, 평균에서 멀어질수록 발생 빈도가 종 모양으로 감소하는 형태
- 평균과 표준 편차에 따라 분포 모양이 결정(영상에서는 주로 평균이 0인 분포 사용)
- 평균이 0이고 표준 편차가 $\sigma$인 1차원 정규 분포의 함수식은 아래와 같음
- $G_\sigma (x) = \frac{1}{\sqrt{2\pi \sigma^2}}exp^{-\frac{x^2}{2\sigma^2}}$

![image](https://github.com/as9786/ComputerVision/assets/80622859/da4820da-ffe0-4d6f-bb37-30dfb2cadca5)

- 2차원일 경우는 아래와 같음
- $G_\sigma (x,y) = \frac{1}{\sqrt{2\pi \sigma^2}}exp^{-\frac{x^2+y^2}{2\sigma^2}}$
