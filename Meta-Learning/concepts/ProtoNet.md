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

- 
