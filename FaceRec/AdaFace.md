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
3. 
