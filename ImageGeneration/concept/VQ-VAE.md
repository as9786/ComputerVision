# Neural Discrete Representation Learning

![image](https://user-images.githubusercontent.com/80622859/231402649-7732a7ac-f24e-4c9a-9956-e130e82d6a8e.png)

- Learning from Continuous to Discrete
- 모형은 입력 x로부터 받아 encoder를 통해 출력 $z_e (x)$를 생성
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
- 각각의 vector들과 초기호된 codebook vector 간의 거리를 계산하여서 가장 가까운 거리의 vector의 index를 부여

![image](https://user-images.githubusercontent.com/80622859/231429481-01799f86-e0be-4b05-af14-800b88552c09.png)

## Learning

- decoder input에서의 경사를 가져와서 학습

![image](https://user-images.githubusercontent.com/80622859/231429875-ace07831-2f50-444a-99fb-3f9ee63b90cd.png)

- 
