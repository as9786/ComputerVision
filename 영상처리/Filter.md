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

![image](https://github.com/as9786/ComputerVision/assets/80622859/a3f36ab3-39ba-4f21-b5e2-5f538de991ce)

- 연속 함수이지만 이산형 mask를 만들기 위해, x와 y 값이 정수인 위치에서만 정규 분포값을 추출하여 생성
- 평균이 0이고 표준 편차가 $\sigma$인 정규 분포는 x가 $-4\sigma$에서 $4\sigma$ 사이인 구간에서 대부분의 값이 나타나므로, Gaussian filter mask size는 보통 $8\sigma + 1$로 정함
- 

- 위의 식을 사용해서 kernel을 만들면 Gaussian filter
- 표준 편차의 값이 클수록 분포는 완만해지고, 값이 작을수록 분포는 뾰족해짐
- 표준 편차의 값이 클수록 대상 점에서 멀어질 때, 값이 작아지는 정도가 크기 때문에 blurring 효과는 커짐
- 반대로 표준 편차 값이 작을수록 blurring 효과는 작아짐

![image](https://github.com/as9786/ComputerVision/assets/80622859/f6b4a5ec-5332-4260-a998-b868be8a4b45)

## Low-pass filter, high-pass filter
- 영상으로부터 high-frequency를 제거하는 filter
- 영상에 Gaussian filter를 적용하면 흐릿한 영상을 얻음
- 흐릿한 영상을 원래 영상에서 빼면 영상의 세부적인 부분을 얻을 수 있음

![image](https://github.com/as9786/ComputerVision/assets/80622859/fa432b32-6ce7-4ae9-a22f-52db91166495)

- 위와 같이 세부적인 부분을 추출하는 연산을 high-pass filter라고 함

## Sharpening
- 원본 영상에서 세부적인 부분을 더하면 더욱 선명한 영상을 얻을 수 있음

![image](https://github.com/as9786/ComputerVision/assets/80622859/c8ea8e74-050c-47ed-ac3f-262c3eb980f4)

