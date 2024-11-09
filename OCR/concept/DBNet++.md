# Real-Time Scene Text Detection with Differentiable Binarization and Adaptive Scale Fusion

## 초록
- 분할 방법은 글자 탐지에서 매우 각광을 받고, 좋은 성능을 보임
- 임의의 모양과 극단적인 종횡비에도 pixel-level descriptions를 통해서 탐지
- 그러나 분할 방식은 복잡한 후처리 방식과 모형의 견고성에 제한을 받음
- 후처리는 모형 최적화와는 별개로 시간 소모가 큼
- DB module뿐만 아니라 ASF module을 통해서 규모 견고성을 향상시킴. 다양한 크기의 특징들을 상황에 따라 융합
- 크기 견고성(Scale robustness) : 다양한 크기의 입력에도 일관되게 성능을 발휘하는 것
- DB + ASF => SOTA

## 1. 서론
- 배경 글자 탐지에서는 분할 모형이 이점을 지님
- 하지만 이는 복잡한 후처리 문제 등 다양한 문제점 또한 지니고 있음

![image](https://github.com/user-attachments/assets/1bf2759b-0276-48f7-872c-b24744d1cc29)

- 위의 파란색 후처리 과정은 분할 신경망으로부터 나온 probability map을 일정한 임계점을 통해서 binary map으로 전환
- Pixel clustering과 같은 heuristic technique 사용(Group pixel -> 글자 영역)
- 이는 분할 신경망의 학습 과정 이외로 처리해주어야 함
- 효과적으로 하기 위해 이진화 작업을 분할 신경망에 추가(Joint optimization, 빨간색 선)
- DBNet과 다른 점은 크기 견고성을 향상시키기 위해 multi-scale feature maps를 합침(ASF module)

## 2. 방법

![image](https://github.com/user-attachments/assets/cd5994f1-b011-4339-acec-bb42efa7ce02)

1. 영상을 FPN에 입력
2. Pyramid features는 같은 크기로 upsampling 후에 ASF(Adaptive Scale Fusion)의 입력으로 들어감. 그 후, contextual feature F를 출력. F는 probability map(P)와 threshold map(T)를 예측하는데 사용
3. P와 F를 통해서 approximate binary map($\^{B}$)을 계산
- 학습 시에는 지도 학습 방식이 P, T, $\^{B}$에 적용($\^{B}$와 P는 손실 함수를 공유)
- 추론 시에는 $\^{B}$ 또는 P을 통해서 경계 상자를 예측

### 3.1 Adaptive Scale Fusion

- 다른 크기의 특징들은 다른 수용 영역을 지님. 그러므로 다른 크기의 text instances에 집중을 하게 됨
- 얕고, 크기가 큰 특징들은 작은 글자들을 잡아냄.
- 단순히 더하거나 연쇄적으로 합치는 기존의 분할 방법과 다르게, ASF는 동적으로 다른 크기의 특징들을 합침
- ASF module에 들어가기 전에 모든 feature maps은 같은 크기로 조정

![image](https://github.com/user-attachments/assets/ee5273d3-edfa-42aa-b698-2444139b4404)



