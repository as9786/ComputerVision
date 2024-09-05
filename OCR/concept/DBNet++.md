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
- 
