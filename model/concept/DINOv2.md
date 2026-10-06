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

- 
