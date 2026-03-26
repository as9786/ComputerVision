# Emerging Properties in Self-Supervised Vision Transformers

## 1. 서론
-  By directly predicting the outputs of a teacher network constructed with a momentum encoder using cross-entropy loss, self-supervised training is simlified
- Work both CNN and ViT

## 2. 방법

### SSL with Knowledge Distilation

<img width="242" height="231" alt="image" src="https://github.com/user-attachments/assets/24d26af1-16de-4535-aedf-58133b60de4a" />

- 자기 지도 학습 방법들과 구조가 같음. 지식 증류와 유사

<img width="262" height="51" alt="image" src="https://github.com/user-attachments/assets/3765b137-b48f-4805-84e4-8deb2577aec4" />

- 입력 사진은 교사 모형과 학생 모형으로 입력
- 출력 결과에 softmax 적용
- $\tau$ : Temperature parameter. 출력 분포의 뾰족함
- 교사 모형과 학생 모형의 분포를 일치시킴 <- cross entropy
- Multi-Crop strategy
    - 주어진 영상에서 서로 다른 시각인 집합 V 구성
    - $V = {x_1^g, x_2^g, ..., local\ view_i}$
    - Local view -> Student model, Gloal view -> Teacher model

### 교사 모형
- 학생 모형의 이전 반복을 교사 모형으로 사용
- 교사 모형은 학습 동안 가중치를 얼림
- 학생 가중치에 지수 이동 평균을 사용하는 momentum encoder
- Update rule : $\theta_t \leftarrow \lambda \theta_t + (1-\lambda)\theta_s$

### 신경망 구조
- ViT or ResNet backbone (f) + Projection head (h)
- 배치 정규화 사용 X
- h = MLP(3 layers) + L2 normalization

### 붕괴 회피
- Centering + Sharpening
- Centering : 특정 쏠림 방지 => 평평하게
- Sharpening : Centering의 반대 효과 => 뾰족하게


