# Wasserstein GAN

- EM distance(Earth-Mover, Wasserstein-1)
- EM distance : Computes minimum amount of mass that needs to be transported to transform one distribution into the other, over all possible joint distributions between them
- 해당 EM distance를 손실로 사용

## 1. 기존 생산적 적대 모형의 문제
- 기존 GAN은 JS/KL divergence를 사용
- 두 분포가 겹치지 않으면 경사가 0
- 학습이 불안정(Model collapse)
- 손리이 의미가 없음

## 2. 방법
- 거리를 바꾸자
- 확률 분포가 얼마나 다른가 -> 한 분포를 다른 분포로 바꾸는 비용=Wasserstein distance를 최소화하도록 학습
- 기존에는 판별기가 진짜인지 가짜인지 분류
- 판별기 -> 점수 함수(Critic)
- 확률이 아니라 realness score 출력

### 2-1. 손실 함수

- $min_G max_D E_{x\sim P_{real}}[D(x)]-E_{z\sim P_z}[(D(G(z))]$
- 멀리 떨어져 있어도 얼마나 이동해야 하는지 알 수 있음
- 손실이 낮을수록 분포가 가까워짐

### 2-2. Lipschitz constraint
- 판별기 = 1-Lipschitz 함수
- 출력 변화가 너무 급격하면 안됨
- 입력 변화에 비해 출력이 너무 급격하게 변하지 않도록 제한하는 조건
- $f(x_1)-f(x_2)| \leq K \cdot ||x_1-x_2||$
- 변화율이 K 이하로 제한
- 출력의 기울기가 제한된 함수
-  WGAN에서 K=1 => 경사가 1 이하 
