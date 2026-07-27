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
- $x_t = \sqrt{1-\beta_t
- $p_{\theta} (x_0) := \int p_{\theta}(x_{0:T})dx_{1:T}$
- 
