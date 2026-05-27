# Wiener filter
- 신호 처리와 영상 처리에서 사용하는 대표적인 noise 제거 및 복원 filter
- 원본 신호와 가장 가까운 결과를 통계적으로 추정
- Noise는 제거하고, 원래 정보는 최대한 보존

## 1. Idea
- 관측된 신호를 아래처럼 생각
- y(t) = x(t) + n(t)
- y(t) : 관측 신호(Noise 포함), x(t) : 원본 신호, n(t) : Noise
- 관측된 y(t)로부터 원본 x(t)를 가장 잘 추정하는 것

## 2. 개념
- 아래 값을 최소화
- $E[(x(t) - \hat x (t))^2]$
- 원본과 복원 결과의 평균 제곱 오차
- 현재 pixel의 통계적 특성, 주변 분산, noise variance 모두 고려
- 해당 부분이 질감인지 noise인지 통계적 판단

## 3. 영상 처리에서의 동작

- $\hat F (u,v)=\frac{H^* (u,v)}{|H(u,v)|^2 + \frac{S_n (u,v)}{S_x (u,v)}} G(u,v)$
- G(u,v) : Noise 포함 영상, H(u,v) : Blur/Degradation function, $S_n$ : Noise power spectrum, $S_x$ : Original image spectrum

## 4. 특징
- Noise 크기에 따라 동작이 달라짐
- Noise가 크면 smoothing 강하게, 작으면 원본 보존 위주
- 경계 보존 성능이 좋음

## 5. 한계
- Noise 통계 가정 필요(기본적으로는 Gaussian noise 가정) -> 실제 noise가 다르면 성능 저하
- 계산량 존재
- Over-Smoothing
