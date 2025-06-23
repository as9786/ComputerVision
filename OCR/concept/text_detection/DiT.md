# Self-supervised Pre-training for Document Image Transformer)

- 문서 사진 관련 작업을 위해 고안되 자가 지도 사전 학습 방법
- Non-label data에 대해서 자가 지도 학습하여 문서의 특징과 pattern을 학습하고, 그 후 DLA와 같은 작업에 backbone network로 적용 가능
- 과적합을 방지하여 일반화 능력 향상. 학습 수렴 속도 향상
- Vanillar transformer 사용

## 사전 학습 전략

### MIM
- Image를 image patch와 visual token으로 표시

![image](https://github.com/user-attachments/assets/d90e30c6-8000-4e06-b0cf-7ec6cc9e8e73)

- 탐지 작업에 적용하기 위해 mask R-CNN, cascade R-CNN 등의 방식을 뒤에 적용
