# FaceNet: A Unified Embedding for Face Recognition and Clustering

## 초록
- 얼굴 사진에서 거리가 얼굴 유사성 측정에 직접 해당하는 간단한 euclidean space mapping
- 해당 공간에서는 FaceNet embedding을 feature vector로 사용
- Embedding 자체를 직접 최적화하도록 학습된 깊은 합성곱 신경망 사용
- 이는 표현 효율성이 좋아 얼굴 당 128 bite만 사용

## 1. 서론
- 신경망은 embedding 공간의 L2 loss가 얼굴 유사성에 직접 대응되도록 훈련됨
- 얼굴 검증은 두 embedding 사이의 거리를 임계깞으로 설정. 인식은 KNN, 군집화는 K-Means 등을 통해 수행ㄹ
- Triplet loss를 사용하여 128차원의 압축된 face embedding을 직접 출력

## 2. 방법
- 주요 구조 : Zeiler&Fergus network & InceptionNet
- Triplet loss를 통해 각 얼굴 쌍 사이의 margin을 적용하여 다른 얼굴들 사이의 차별성 강조
- Triplet loss : 영상 x를 d차원 euclidean space에 삽입하여 같은 사람의 사진들이 다른 사람의 사진보다 더 가깝게 함

### 2-1. Triplet selection
- 수렴 속도가 느리지 않게 삼중항을 선택하는 접근 방식
- 빠른 수렴을 위해 $x_a$가 주어지면 아래 식을 만족한은 $x_p$ 및 $x_n$을 선택해야 됨

<img width="567" height="210" alt="image" src="https://github.com/user-attachments/assets/371b7d01-cc5a-4d4e-974c-bd68dc37da45" />

- argmin과 argmax는 계산이 불가능하기 때문에 두 가지 중 하나로 선택해야 됨
- 가장 최근의 신경망 가중치를 기준으로 data subset에 대해 argmin과 argmax를 계산해서 n단계마다 offline으로 triplet 계산
- argmin : 가장 어려운 positive data, argmax : 가장 어려운 negative data
- 하지만 위 두 개를 찾는 것은 연산량이 많아 불가
- 삼중항 손실 : 기준(Anchor), 본인(positive), 타인(negative)
- 기준 <-> 본인(가깝게), 기준 <-> 타인(멀게)
- 학습이 잘 되기 위해서는 모형이 구별하기 힘들어하는 가장 어려운 조합(hard triplet)을 줘야 함
- 매 학습마다 모든 training set의 거리를 계산하는 것은 불가능 => 실시간으로 전체 dataset에 대해 수학적 극값을 찾는 연산 불가
- Offline : 매번 계산하는 것이 아닌 data subset만 추출. 가장 최근 신경망 가중치를 한 번 통과시켜 거리 계산
- Online : Triplet 생성하여 mini batch 내에서 hard positive/negative 선택
- 여기서는 online 방식 사용

### 2-2. 깊은 합성곱 신경망
- ZFNet에서 합성곱 층 사이에 1 x 1 합성곱층 추가

## 3. 평가
- 각 dataset에서 사진 쌍에 대한 FAR 및 VAL 비율을 계산하여 표준 오차 산정

### 3-1. FAR(False Accept Rate, 오인식률)
- 서로 다른 사람의 사진인데 모형이 동일 인물이라고 잘못 판단하여 통과시킨 비율

### 3-2. VAL(Validation Rate, 인증 성공률)
- 서로 같은 사람의 사진을 모형이 동일 인물이라고 올바르게 판단하여 통과시킨 비율

