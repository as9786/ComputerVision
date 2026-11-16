# AdaFace: Quality Adaptive Margin for Face Recognition

## 초록
### 연구 배경
- SphereFace, CosFace, ArcFace 등 margin based softmax loss function이 좋은 성능을 보임
- 해당 손실 함수들은 특징 공간에서 다음 조건을 만족하도록 학습
1. 같은 사람의 얼굴 특징은 서로 가깝게
2. 다른 사람의 얼굴 특징은 서로 멀리
3. 사람 간 경계를 더 명확하게 구성
- 어려운 표본이라고 해서 모두 같은 이유로 어려운 것은 아님

### 기존 연구 문제점
- 사진 품질은 좋지만 구분이 어려운 경우
- 사진 품질이 낮아 얼굴 정보가 부족한 경우
- 해당 문제는 모형의 구분 능력 부족보다는 입력 영상의 정보 부족일수도 있음

### 해결 방안
1. 얼굴 인식 모형에서 feature vector 추출
2. 정규화 전 feature vector size 계산
3. 해당 크기를 영상 품질의 지표로 사용
4. 품질에 따라 각도 여백과 가산 여백을 조정
5. 결과적으로 영상 품질과 표본 난이도에 따라 경사의 방향을 다르게 만듦

## 1. 서론
- 표본 난이도와 영상 품질은 구분해야 됨

<img width="487" height="232" alt="image" src="https://github.com/user-attachments/assets/8531f5ee-3351-41f9-a145-79c5f4f2a647" />

### 표본 난이도
- 현재 모형이 해당 얼굴을 분류하기 얼마나 어려워하는지 의미
- 정답 클래스의 예측 확률이 낮음
- 다른 사람과 유사도가 높음
- 결정 경계 근처에 위치함

### 영상 품질
- 입력 영상에서 신원을 구분할 수 있는 정보가 얼마나 있는지

## 2. 방법

### 2-1. 전체 구조
- AdaFace는 새로운 얼굴 탐지기가 아님
- 특징을 어떤 방식으로 학습할지 결정하는 손실 함수
- 학습 목적 함수의 설계

### 2-2. Feature norm
- 정규화 전 feature norm과 영상 품질 사이의 관계 분석
- 상관계수 : 0.5235
- 영상 정보가 어느 정도 feature norm에 반영된다고 관찰하고 대리 지표로 사용
- 영상의 feature norm을 그대로 사용 X
- 학습 중 관찰되는 feature norm의 평균과 표준편차를 사용해 정규화하고, 범위를 제한

$$q_i = clip(h \cdot \frac{\|z_i\| - \mu}{\sigma + \epsilon},-1,1)$$

- $q_i$ : i번째 영상의 정규화된 품질 대리 지표
- $|z_i|$ : 정규화 전 feature norm
- $\mu, \sigma$ : 학습 중 추정한 feature norm의 평균과 표준편차
- h : 품질 지표의 분포 범위를 조절하는 값
- $\epsilon$ : 0으로 나누는 상황을 방지하는 값
- -1에 가까울수록 현재 학습 분포에서 상대적으로 낮은 norm

### 2-3. Margin
- ArcFace에서는 정답 클래스에 고정된 각도 여백을 적용
- AdaFace에서는 품질 지표 $q_i$를 사용해 두 가지 여백을 조절
1. 각도 여백(Angular margin) : $g_{angle} = -mq_i$
2. 가산 여백(Additive margin) : $g_{add} = m(1+q_i)$
- 정답 클래스 logit : $f_y = s[cos(\theta_y + g_{angle}) - g_{add}]$

$$f_y = s[cos(\theta_y - mq_i) - m(1+q_i)]$$

- 정답이 아닌 class : $f_j = 
