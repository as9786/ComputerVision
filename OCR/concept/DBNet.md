# Real-Time Scene Text Detection with Differentiable Binarization

## 서론
- 분할 기반 모형은 pixel 단위 data를 다루므로 글자 탐지에서 많이 다뤄짐
- 해당 방법은 회전되거나 기울어진 영상에서도 좋은 성능을 보이나 후처리가 복잡해 연산량이 많음
- 정확도 향상을 위해 progressive scale expansion을 숭핸 PSENet, 분할 결과에 pixel embedding을 하는 방법으로 pixel 간 거리를 군집화하는 방법이 SOTA
- 기존 방식은 분할 신경망을 이진화된 영상으로 만들기 위해 고정된 임계값을 사용
- 해당 논문은 임계값을 학습
- Joint optimization = Binarization operation + Segmentation network

![image](https://github.com/user-attachments/assets/356ea1c8-44bf-412d-9536-22b97de317ff)

- 하지만 이진화 함수는 특정 값 이상이면 1, 아니면 0이기 때문에 미분 불가능 => Differentiable Binarization(DB, 이진화 근사 함수) 사용

## 방법

![image](https://github.com/user-attachments/assets/4f1f9da5-1938-448f-8e78-b480302ce849)

- 입력 영상은 Feature-Pyramid Backbone(FPB)으로 넣음
- Feature pyramid 구조를 통해서 크기 변화에 강건하게 만듦
- 최종적인 feature map을 사용해서 probability map과 threshold map 생성

![image](https://github.com/user-attachments/assets/f88b915f-f400-4801-a261-48f1fe3a3af9)

- i, j : 좌표, t : 미리 정의한 임계점, T : Adaptive threshold, K : Amplifying factor, $\hat B$ : Approximate binary map
- 고정된 숫자에서 0과 1을 나누는 것이 아니라, 학습된 값을 기준으로 나누도록 DB 적용

![image](https://github.com/user-attachments/assets/3667d020-8bc6-4377-8f7a-9cce009bea3a)

- (a) : Input image, (b) L Probability map, (c) : Threshold map without supervision, (d) : threshold map with supervision
- 합성곱 신경망은 입력 영상의 종횡비가 획일적이라 다양한 종횡비를 대처하기 어려우므로 deformable convolution network 사용
