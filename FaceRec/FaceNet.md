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
