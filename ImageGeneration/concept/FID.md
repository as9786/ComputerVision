# Frechet Inception Distance

## 정의
- 실제 영상과 생성된 영상이 얼마나 유사한지 계산하는 지표
- 이 점수가 낮을수록 유사

## 탄생 배경
- 기존에 있던 IS(Inception Score)를 개선시키기 위해 개발
- GAN의 성능 평가를 위해 특별히 개발
- IS는 생성된 영상만 사용하여 성능을 평가. FID는 실제 imageset과 생성된 imageset을 비교하여 성능을 평가
- 영상의 평균과 공분산을 계산하여 multivariate Gaussian으로 만든 뒤, Wasserstein-2 distance라 불리는 Frechet distance를 사용하여 두 분포 사이의 거리를 측정

## FID 계산 방법
- Pretrained inception v3 model 사용. 출력층을 제거하고 마지막 pooling layer의 activation을 이용
- 2,048개의 activation이 있으므로, 각 영상은 2048개의 activation feature로 예측
- 위로 구한 vector들을 토대로 아래 식을 계산
- $d^2((m,C), (m_w, C_w))=\| m-m_w \|_2^2 + T_r(C+C_w) - 2(CC_w)^{1/2})$
- m : Feature-Wise -mean, C : 공분산, T : 대각합 
