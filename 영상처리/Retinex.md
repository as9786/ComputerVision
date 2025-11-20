# Retinex
- 인간 시각 모형(Human Vision Model)을 기반으로 만든 영상 처리 이론
- 조명(Illumination)과 반사(Reflectance)를 분리해서 조명 영향을 제거하고, 실제 물체의 색/명암을 복원하는 방법
- 그림자, 조명 불균일(uneven lighting), 역광(backlight) 그리고 과노출/저노출 등을 해결하는 최적화 방식

# 1. 원리
- 영상은 두 요소로 구성
- R(x), Reflectance : 물체 고유의 정보(질감, 글자, 모양, pattern)
- L(x), Illumination : 그림자, 조명, 빛의 양, 밝기
- 우리가 원하는 건 R(x)
- 실제 촬영된 사진은 위 두 가지가 섞여 있음. I(x) = R(x) x L(x)
- Retinex는 조명 L(x)를 제거하고 R(x)만 남기기 위한 기술
  
# 2. 수식
- R(x) = log(I(x))-log(L(x))

# 3. 조명 추정
- L(x) 추정을 위해서 Gaussian blur로 모형화
- 조명은 천천히 변하고(low frequency), 반사 성분은 갑자기 변함(high frequency)
- L(x)= I(x) x Gaussian(sigma)
- sigma가 크면 클수록 더 부드로운 조명 모형
- sigma가 작으면, 좀 더 local illumination

# 4. SSR(Single-Scale Retinex)
- $SSR(x)=log(I(x))-log(I(x) \times Gaussian(\sigma))$
- sigma가 작으면 너무 날카로워지고, 너무 크면 부드럽고 그림자가 남음

# 5. MSR(Multi-Scale Retinex)
- SSR을 여러 sigma로 처리해서 평균
- $MSR(x)=\frac{1}{N} \times \Sigma[log(I(x))-log(I(x)\times Gaussian(\sigma_k))]$

