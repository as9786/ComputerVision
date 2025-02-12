# Prototypical Networks for Few-shot Learning 

## 초록

- Trainset에 없는 새로운 class에 대해 학습할 때, 새로운 class에 대한 dataset이 부족할 경우를 대처하기 위한 방안 제안
- 각 class의 prototype representation까지의 거리를 계산해서 classification을 수행할 수 있는 거리 공간(metric space)을 학습
- 이는 제한된 data에서 유익하고 단순한 유도 편향을 반영하여 우수한 성능을 보여줌

## 서론
- Few-shot learning은 train dataset에는 없는 새로운 class에 대해 적은 data만을 가지고 있을 경우, 새로운 class를 분류하는 작업
- ProtoNet은 각 class에 대해 single prototype representation이 있는 embedding을 기초로 접근
- 신경망을 사용하여 embedding space를 학습. Embedding space에서 설정된 support set의 평균으로 class prototype 생성
- ProtoNet은 각 class의 prototype 역할을 하기 위해 meta-data를 공유 공간(shared space)에 embedding하는 것을 학습
- 분류를 수행할 때, Embedding된 query point에서 가장 가까운 class prototype을 찾음
- 각 class의 평균으로 prototype을 만듦. Euclidean distance를 사용해 query point와 거리 계산
- 가장 가까운 거리의 prototype을 결정하고 해당 class로 예측

## Prototypical Networks

- Few shot classification에서는 N개의 support set example이 존재. $S={(x_1,y_1), (x_2,y_2),...,(x_N,y_N)}$. $S_k$ : class k에 대한 dataset

![image](https://github.com/user-attachments/assets/5f5ff1d1-b312-4a3f-b973-0444c4493caf)

![image](https://github.com/user-attachments/assets/2b06e5e0-c86f-4d07-9224-948facd6df1d)

- Negative log probability를 최소화. 확률적 경사 하강법 적용. Training episode는 training set에서 임의의 class를 선택하여 만듦
- 남은 것 중 일부를 query point로 사용
- Support set에 대해 혼합 밀도 추정 사용
- 거리 계산으로는 Bregman divergences 사용(사실상 squared Euclidean distance)



