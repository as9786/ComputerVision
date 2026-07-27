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

- $p_{\theta} (x_0) := \int p_{\theta}(x_{0:\T})dx_{1:T}$
- 
