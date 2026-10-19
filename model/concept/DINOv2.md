# DINOv2: Learning Robust Visual Features without Supervision

## 1. 서론
- 기존 foundation model들은 text-guided pre-training을 채택
- 위 방식은 두 가지 문제
  1. Pixel-Level information 학습 어려움
  2. 영상 단독으로 학습 불가
- DINOv2
  - Image/Patch level discriminative self-supervised learning
  - 정제된 방대한 양의 dataset
  - Memory 사용은 줄이면서 빠른 학습 기법

## 2. 방법

### 2-1. Data processing 

<img width="1753" height="499" alt="image" src="https://github.com/user-attachments/assets/4c87ce38-bfbc-43d8-ae89-4ac297a430f7" />

1. Collecting raw images(Uncurated data) : 인터넷에서 사진 모음
2. 중복 제거
3. Self-Supervised image retrieval
    - Curated/Uncurated data에 대해 ViT 모형을 통해 embedding
    - Uncurated data에 대해 K-means clustering 수행
    - 각 curated data에 대해 가장 가까운 N개의 uncurated data를 고르거나 아니면 가장 가까운 군집을 찾고 그 안에서 m개를 고름

### 2-2. Discriminative self-supervised pre-training

<img width="470" height="472" alt="image" src="https://github.com/user-attachments/assets/4428f347-e6db-4233-834b-61a8062e7c91" />

- Image-Level objective : 지식 증류 방법 활용
- Patch-Level objective : 학생 모형에 넣는 영상들은 몇 개의 patch masking. 선생 모형에는 원본을 넣어서 나오는 결과를 patch-wise하게 cross entropy 계산

<img width="923" height="569" alt="image" src="https://github.com/user-attachments/assets/925ebe49-1dfb-46d3-b479-59e6f535dc01" />

- Untying head weights between both objectives : Cross entropy를 계산할 때 쓰이는 tensor를 얻기 위해 몇 개의 층으로 구성된 head를 서로 공유
- Sinkhorn-Knopp centering : Sinkhorn-Knkopp batch normalization 도입. 선생 모형과 학생 모형 간의 domain gap을 줄여줌
- KeLeo regularizer : 배치 내 여러 특징들이 있으면 그 특징 사이의 거리를 최대한 균등하게 만드는 방법 


