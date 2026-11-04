# ArcFace : Additive Angular Margin Loss for Deep Face Recognition

## 초록
- 일반적인 사진 분류와 동일한 방법
- 얼굴 인식 과제는 데이터가 얼마 없고, 라벨도 많음
- Additive angular margin loss 도입
- 확률을 각도 개념을 활용하여 분류하게 되는 방식으로 변경. 기존 방식보다 class 간 경계 형성을 모형이 더 잘 학습하게 됨

## 1. 서론

<img width="738" height="467" alt="image" src="https://github.com/user-attachments/assets/74a410d5-d122-41fa-89ad-f6316d6c719b" />

- 각도가 가까운 객체는 가깝게, 각도가 멀어진 객체는 더 멀게 학습

## 2. 관련 연구

### SphereFace
- 신경망의 마지막 완결 연결층의 가중치 행렬은 각 class의 중심 지표로 표현될 수 있음

## 3. ArcFace
- Softmax를 사용하게 되면 intra-class는 비슷하게 embedding이 형성됨. Inter-Class는 다르게 embedding 형성
- 얼굴 인식은 사람들로만 구성되어있기 때문에 intra-class
- 해당 이유로 성능 저하 발생
- 위 문제를 해결하기 위해 편향을 없애고, vector 간 각도에 집중

<img width="692" height="110" alt="image" src="https://github.com/user-attachments/assets/989f5dab-9b23-46fa-8358-a73d3917acb8" />

- $\theta_j$는 가중치(W)와 특징(x)의 각도
- 가중치 : 사람의 대표 얼굴(기준점, center)
1. 모형의 출력으로 feature vector(x)
2. 출력 차원이 512차원이라고 가정. 1000명 중 누구인지 맞추기 위해 완전연결계층에 512 x 1000 가중치 행렬 곱함
3. W를 세로로 쪼개면 $W_j$는 512차원 vector
- Ex) $W_1$ : 유재석 기준 얼굴, $W_2$ : 강호동 기준 얼굴
- 모형이 유재석 사진 100장을 받고 1번 정답을 맞추기 위해서는 $W_i^T x_i$가 최고점이 나와야 함
- 내적 점수가 높기 위해서는 두 vector 방향이 같아야 함(각도가 
- W와 x는 L2 norm으로 정규화(1로 제한). Scale-factor s로 re-scale

### 3-1. 학습

<img width="1280" height="451" alt="image" src="https://github.com/user-attachments/assets/8cf4f890-904b-472f-9612-9e15ae72306c" />

1. 특징과 가중치의 cosine similarity를 구하여 cosine 값을 구함
2. acrcos function을 활용하여 두 vector 각도 계산 ($arccos=cos^{-1}$ : 내적 값을 넣으면 각도를 계산)
3. 각도에 angular margin penalty m을 더하여 $cos(\theta_{yi}+m)$을 계산
4. s를 곱해주고, softmax 취함
5. Cross entropy loss를 구하고, 역전파하여 신경망 학습

<img width="705" height="120" alt="image" src="https://github.com/user-attachments/assets/347c821e-ee67-4da1-be49-9af943c7d3cc" /> 
