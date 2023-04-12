# Neural Discrete Representation Learning

![image](https://user-images.githubusercontent.com/80622859/231402649-7732a7ac-f24e-4c9a-9956-e130e82d6a8e.png)

- Learning from Continuous to Discrete
- 모형은 입력 x로부터 받아 encoder를 통해 출력 $z_e (x)$를 생성
- z는 categorical distribution(균일 분포)
- 이 때, discrete latent variable z는 shared embedding space인 e로부터 가장 가까운 이웃과의 거리 계산에 의해 결정
- 가장 가까운 vector로 결정
- 여기에는 e인 embedding space를 codebook으로 불리움. 
- Codebook은 기본적으로 vector를 요소로 가지는 list
- $e \in R^{K*D}$, K는 discrete latent space의 크기가 됨(K-way categorical)
- D는 각각의 latent embedding vector인 $e_i$의 차원 수
- K개의 embedding vector가 존재하며, 이를 수식으로 나타내면 $e_i \in R^D, i \in 1,2,...,K$

![image](https://user-images.githubusercontent.com/80622859/231407597-cb1d32f8-f1a4-427a-881b-35b111492d02.png)

- K는 one-hot vector의 개수, d는 one-hot vector의 차원
- Encoder의 출력값과 codebook의 vector들 간의 거리를 계산
- (B,H,W,C) image -> (B * H * W, C) => C개의 vector
- 각각의 vector들과 초기된 codebook vector 간의 거리를 계산하여서 가장 가까운 거리의 vector의 index를 부여

![image](https://user-images.githubusercontent.com/80622859/231429481-01799f86-e0be-4b05-af14-800b88552c09.png)

![image](https://user-images.githubusercontent.com/80622859/231432108-d9ea5ad7-eaf6-46c9-82ab-4fb75ca100c1.png)

## Learning

### 1. Reconstruction loss

- 실제 경사가 없음
- argmin 연산은 비선형적이고 미분이 불가능
- decoder input $z_q(x)$에서 encoder output $z_e(x)$로 경사 복사
- Forward에서는 $z_q(x)$가 decoder로 전달되고, backward에서는 경사가 encoder로 그대로 전달
- Encoder output과 decoder input은 동일한 D차원을 공유
- 경사에는 재구성 손실을 최소화하기 위한 정보 포함

### 2. Codebook loss
- $z_q (x)$에서 $z_e(x)$로 경사가 그대로 사상되기 때문에, $e_i$는 재구성 손실에서 경사 정보를 받지 못함
- Embedding vector를 학습하기 위해 가장 간단한 dictionary learning vector quantization(VQ) 사용
- $e_i$와 $z_e(x)$ 사이의 $l_2$ error를 통해 $e_i$를 $z_e(x)$로 이동하도록 학습

### 3. Commitment loss
- Embedding vector는 무한하기 때문에, codebook loss에서 $e_i$는 encoder vector만큼 빠르게 학습되기 어려우며 임의로 커질 수 있음
- Encoder vector와 embedding vector에 commit하여 encoder vector가 embedding vector와 유사해질 수 있도록하는 commiment loss를 추가
- $\beta$ hyperparameter의 변화에 따라 큰 성능 차이를 보이지 않으므로, 제안한 모형이 $\beta$ 값에 대해 robust($\beta=0.25$)

![image](https://user-images.githubusercontent.com/80622859/231434535-ecc3ea66-8129-4702-9962-f6ad3b77219a.png)



