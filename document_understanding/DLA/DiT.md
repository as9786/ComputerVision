# DiT: Self-supervised Pre-training for Document Image Transformer


## 1. 서론

- Human-labeled document image에 의존적이지 않음
- 다양한 AI task 잘 다룸
- 본 논문에서는 사진 분류, DLA, 표 탐지 등 다양한 작업을 수행

## 2. DiT

### 2.1 모형 구조

![image](https://github.com/user-attachments/assets/15dde87c-0645-44fc-9006-d6e092941ced)

- ViT와 같이 transformer를 backbone으로 사용
- 문서 사진들을 겹치지 않는 여러 개의 patch로 나눠서 sequential type의 patch embedding 생성.
- 1D positional embedding과 합쳐 각 image patch를 transformer의 입력으로 줌.
- Multi-head attention을 적용하여 encoder로부터 각 image patch에 대한 출력값을 받음

### 2.2 사전 학습

- MIM(Masked Image Modeling)
- BEiT 방식 차용

### 2.3 미세 조정

#### 문서 분류
- RVL-CDIP dataset
- Average pooling을 사용해서 각 image patch를 종합 -> Global representation을 만들고 해당 feature를 간단한 선형 분류기로 넘김

#### DLA
- PubLayNet
- Mask R-CNN, Cascasde R-CNN을 detection framework로 사용
- 서로 다른 크기의 transformer block 사용. 이를 통해 단일 크기의 ViT를 여러 크기로 구성하여 FPN 적용


## 3. 실험

### 3.1 환경
- Random resized cropping

