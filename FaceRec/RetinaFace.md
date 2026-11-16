# RetinaFace: Single-stage Dense Face Localization in the Wild

## 1. 서론

- 수백 명이 찍힌 군중 사진처럼 엄청 작은 크기의 얼굴, 가려진 얼굴, 측면으로 돌아간 얼굴들이 존재
- 기존 얼굴 검출기들은 단순히 사각형만 찾는 데 집중했기 때문에, 극단적인 조건에서는 얼굴의 형태적 맥락을 파악하지 못해 검출에 실패
- 얼굴의 기하학적 구조를 신경망이 함께 이해하도록 강제

## 2. 방법

### 2-1. 손실 함수
- 4가지 multi-task loss
- 4가지 작업을 동시에 수행하도록 손실 함수 설계

<img width="481" height="37" alt="image" src="https://github.com/user-attachments/assets/4bb86a2b-41e0-4c88-a7cc-c3ec5e3e322a" />

1. 얼굴 분류($L_{cls}$) : 해당 영역이 사람 얼굴인지 배경인지 판별(Cross-Entropy)
2. 얼굴 상자 회귀($L_{box}$) : 얼굴의 정확한 좌상단/우하단 경계 상자 좌표를 미세 조정(Smooth-L1 loss)
3. 5 Facial Landmarks($L_{pts}$) : 양쪽 눈 중심, 코 끝, 양쪽 입꼬리 5개 좌표를 예측. Face Alignment(유사 변환) 입력값으로 그대로 쓰이는 핵심 기능
4. 3D 정밀 얼굴 복원($L_{pixel}$) : 자기 지도 방식으로 얼굴의 3D 정점과 조명/색상 정보를 복원해 내는 mesh decoder를 학습 과정에 추가. 학습에서만 사용

### 2-2. 모형 구조

[입력 이미지] 
     │
     ▼
1. Backbone (ResNet-50 / MobileNet) ──► 다양한 해상도의 특징 추출
     │
     ▼
2. FPN (Feature Pyramid Network) ────► 큰 얼굴부터 아주 작은 얼굴까지 다중 스케일 특징 결합
     │
     ▼
3. Context Module (SSH) ─────────────► 주변 맥락(어깨, 머리 모양 등) 정보를 수용하도록 수용영역(Receptive Field) 확장
     │
     ▼
4. Multi-task Heads ─────────────────► [분류] + [BBox] + [5-Landmark] + [(학습 시) 3D Mesh] 동시 출력


- Context module : 얼굴이 모자나 손에 가려졌을 때, 얼굴 자체만 봐서는 검출이 어려움. Deformable convoltion과 filter 효과를 내는 module을 적용해 얼굴 주변의 맥락까지 넓게 참고
