# Neural Discrete Representation Learning

![image](https://user-images.githubusercontent.com/80622859/231402649-7732a7ac-f24e-4c9a-9956-e130e82d6a8e.png)

- Learning from Continuous to Discrete
- 모형은 입력 x로부터 받아 encoder를 통해 출력 $z_e (x)$를 생성
- 이 때, discrete latent variable z는 shared embedding space인 e로부터 가장 가까운 이웃과의 거리 계산에 의해 결정
- 가장 가까운 vector로 결정
- 여기에는 e인 embedding space를 codebook으로 불리움. 
- $e \in R^{K*D}$, K는 discrete latent space의 크기가 됨(K-way categorical)
- D는 각각의 latent embedding vector인 $e_i$의 차원 수
- K개의 embedding vector가 존재하며, 이를 수식으로 나타내면 $e_i \in R^D, i \in 1,2,...,K$

