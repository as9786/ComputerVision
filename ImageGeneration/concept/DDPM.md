# Denoising Diffusion Probabilistic Models(DDPM)

## 서론
- 확산 모형을 발전
- Diffusion models are generative models that learn a parameterized Markov chain to generate samples from a target data distribution after a finite number of diffusion steps
- Forward process : A Markov chain progressively corrupts the data by adding Gaussian noise until the data is transformed into pure Gaussian noise
- Reverse process : The model learns to gradually remove the noise, starting from Gaussian noise, to generate samples that match the data target data distribution
- Since the diffusion process is composed of small Gaussian noise, the sampling chain can be modeled as conditional Gaussian distribution, allowing it to be parameterized by a relatively simple neural network
- 기존 확산 모형은 정의하기 쉽고 학습시키기 효율적이지만, 고품질을 만들지 못함. 반면, DDPM은 고품질을 만들 수 있을 뿐만 아니라 다른 생성 모형보다 우수한 결과를 보임

 ## 확산 모형

<img width="771" height="127" alt="image" src="https://github.com/user-attachments/assets/5dc9afdf-5bae-43e3-8f5d-95871c51feff" />

### Forward process

- $q(x_t|x_{t-1}) = N(\sqrt{1-\beta}x_{t-1}, \beta_t I)$
- 이전 사진 $x_{t-1}$이 주어졌을 때, 다음 사진 $x_t$의 확률 분포
- N : Gaussian distribution. 평균 + Gaussian noise
- $\sqrt{1-\beta_t} x_{t-1}$(평균) : 원래 사진에 얼마만큼 남길 것인지. $\beta=0.01$ -> $\sqrt{1-0.01}=0.995$. 원래 사진에 99.5%만 사용
- $\beta_T I$(분산) : 이번 단계에 넣는 noise 양
- 위 확률분포에서 표본 추출 시 아래식
- $x_t = \sqrt{1-\beta_t}x_{t-1} + \sqrt{\beta_t} \epsilon$
- $\sqrt{1-\beta_t}x_{t-1}$ : 원래 사진. $\sqrt{\beta_t} \epsilon$ : Noise ~ N(0,I)
- $\beta$가 높을수록 noise 양이 많아 짐
- DDPM은 위 식을 매번 계산 X
- 다음 식으로 변환
- $q(x_t|x_0) = N(\sqrt{\bar{\alpha_t}}x_0, (1-\bar{\alpha_t}I)$
- $\alpha_t = 1 - \beta_t$ : 원래 사진이 얼마나 남았는가
- $\bar{\alpha_t} = \prod_{s=1}^{t} \alpha_s = \alpha_1 \times \alpha_2 \times \cdots \times \alpha_t$
- 최종 : $x_t = \sqrt{\bar{\alpha_t}} x_0 + \sqrt{1-\bar{\alpha_t}} \epsilon$
- $\sqrt{\bar{\alpha_t}} x_0$ : 원래 사진 정보, $\sqrt{1-\bar{\alpha_t}} \epsilon$ : 추가된 Gaussian noise

### Reverse process
- 순수한 Gaussian noise를 원래 data 분포로 될돌림
- $p_{\theta} (x_0:T) = p(x_T) \prod_{t=1}^{T} p_{\theta} (x_{t-1}|x_t)$ 
- 생성 과정 전체를 하나의 markov chain으로 모형화
- $p(x_T)$ : Random Gaussian noise. 생성은 항상 N(0,I)에서 시작
- Reverse step : $p_{\theta}(x_{t-1}|x_t) = N(x_{t-1} ; \mu_{\theta}(x_t,t), \Sigma_{\theta} (x_t,t))$
- $\mu$ : 신경망이 예측. 다음 단계로 이동해야 하는 가능도가 높은 위치
- $\Sigma_{\theta} (x_t,t))$ : 얼마나 무작위로 움직일지
- DDPM에서는 평균을 직접 예측 X. Noise 예측 

### 손실 함수
- 우리가 알고 싶은 것 : $x_t$(현재 noise 사진) -> 모형 -> $x_{t-1}$ (이전 단게)
- 하지만 우리는 $x_t$만 보고 $x_{t-1}$이 무엇인지 모름
- $q(x_{t-1}|x_t)$는 계산 불가
- 하지만 학습에서는 원본 사진($x_0$)을 알고 있음
- $x_0$ -> $x_{t-1}$ -> $x_t$ : 전체 과정을 알게 됨
- $q(x_{t-1}|x_t, x_0)$ 계산 가능
- Forward process는 우리가 직접 정의 : $q(x_t|x_{t-1})=N(...)$
- Bayes rule
 - $P(A|B)=\frac{P(B|A)P(A)}{P(B)}$
 - $q(x_{t-1}|x_t, x_0)=\frac{q(x_t|x_{t-1}, x_0)q(x_{t-1}|x_0)}{q(x_t|x_0)}$
 - 사후 분포도 Gaussian
- 젇답 분포  : $q(x_{t-1}|x_t, x_0)$, 모형 : $p_{\theta}(x_{t-1}|x_t)$. 두 분포 모두 Gaussian
- $D_{KL}(q||p_{\theta})$ => 최소화
- KLD에서 두 분포가 Gaussian일 경우 닫힌 형태
- 전개 시 최종 손실 함수 : $L=E[||\epsilon - \epsilon_{\theta}||^2]$
