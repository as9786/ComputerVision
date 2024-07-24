# YOLOv7: Trainable bag-of-freebies sets new state-of-the-art for real-time object detectors

## 서론

- 정확도를 향상시키기 위한 학습 비용을 강화하지만 추론 비용은 증가시키지 않는 최적화된 module 및 최적화 방법
- 이러한 방법을 학습 가능한 bag-of-freebies라고 부름
- Model re-parameterization을 위해 서로 다른 신경망의 층에 적용할 수 있는 모형 re-parameterization 전략을 기울기 전파 경로 개념으로 분석하고 계획
- Coarse-to-fine lead guided label assignment

## 구조

### 1. Extended efficient layer aggregation networks

![image](https://github.com/user-attachments/assets/8a565b8a-14a8-4c21-bcb4-4b13c52fc89c)


