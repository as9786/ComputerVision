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

$$W_j^T x_i = \||W_j\|| \||x_i\|| cos \theta_j$$

- $\theta_j$는 가중치(W)와 특징(x)의 각도
- 
