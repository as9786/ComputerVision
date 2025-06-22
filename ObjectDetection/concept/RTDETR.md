# DETRs Beat YOLOs on Real-time Object Detection

## 서론

![image](https://github.com/user-attachments/assets/19a1dc09-1289-405d-b5df-f71abaefc892)

- 실시간 객체 탐지는 중요한 연구 분야. 물체 추적, 감시 카메라, 자율 주행 등과 같은 광범위한 응용 분야
- 기존 실시간 탐지기는 속도와 정확도 사이의 합리적인 trade-off를 달성한 합성곱 신경망 기반 구조를 채택
- 위와 같은 경우 후처리가 필요(비 최대 억제)
- 일반적으로 최적화가 어렵고 추론 속도를 느리게 만듦
- Transformer encoder는 input seqeunce의 길이가 늘어나 높은 계산 비용이 발생
- 위 문제를 해결하기 위해 Hybrid encoder encoder 설계
- Multi-scale feature scale 내 상호 작용과 scale 간 융합을 분리함으로써 encoder는 다양한 크기의 특징들을 효율적으로 처리
- Decoder의 object query 초기화 방식이 탐지 성능에 중요
- Decoder에 더 높은 품질의 초기 object query를 제공하는 IoU-aware selection 제안
                      
## 비 최대 억제 분석
- 중복되는 예측 상자를 제거하는데 사용
- Score & IoU threshold 두 가지 초매개변수가 필요
- 점수 임계값보다 낮은 점수를 갖는 예측 상자는 제거, 두 예측 상자의 IoU가 IoU threshold를 초과할 때마다 점수가 낮은 상자는 제거
- 위 과정은 모든 유형의 모든 상자가 처리될 때까지 반복적을 ㅗ수행
- 실행시간은 입력 예측 상자와 2개의 초매개변수에 따라 달라짐

## 모형

![image](https://github.com/user-attachments/assets/03d1c39e-787f-45d9-ab4c-34f26d4d9d23)

- Backbone, hybrid encoder, Trasformer decoder로 구성
- Backbone의 마지막 세 단계 출력 특징 ${S_3,S_4,S_5}$를 encoder에 대한 입력으로 활용
- Hybrid encoder는 크기 내 상호 작용과 크기 간 융합을 통해 multi-scale feature를 일련의 영상 특징으로 변환
- IoU-aware query selection은 decoder에 대한 초기 object query 역할을 하기 위해 encoder output sequence에서 고정된 개수의 영상 특징을 선택하는데 사용
- 보조 예측 헤드가 있는 decoder는 object query를 반복적으로 최적화하여 상자와 신뢰도 점수를 생성

### 1. Efficient hybrid encoder

#### Computational bottlenect analysis
- Deformable-DETR은 학습 수렴을 가속화하고 성능을 향상시키기 위해 multi-scale feature 도입을 제안하고 계산을 줄이기 위한 deformable attention mechanism을 제안
- 그럼에도 input sequence의 길이가 급격히 증가하면 여전히 encoder가 계산 병목 현상을 일으키고 DETR의 실시간 구현을 방해

![image](https://github.com/user-attachments/assets/35ece385-ae09-44df-b57a-e99621c0795b)

- 높은 수준의 특징은 영상의 물체에 대한 풍부한 의미적 정보를 포함하는 낮은 수준의 특징에서 추출
- 직관적으로 연결된 multi-scale features에 대해 특징 상호 작용을 수행하는 것은 중복
- DINO-R50 multi-scale transformer encoder를 제거하여 baseline A로 사용
- (e)가 저자들이 선택한 구조

#### Hybrid design

![image](https://github.com/user-attachments/assets/771beb29-d84c-4581-b9c2-5081ad27754f)

- Attention-based Intrascale Feature Interaction(AIFI) module과 CNN based Cross-scale Feature-fusion Module(CCFM)의 두 가지 module로 구성

![image](https://github.com/user-attachments/assets/557e1fa0-05e5-49f4-b681-e797f410bb93)

### 2. IoU-aware Query selection
- DETR의 object query는 decoder에 의해 최적화되고 predictor head에 의해 분류 점수 및 경계 상자에 사상되는 trainable embedding set
- 이러한 object query는 명시적인 물리적 의미가 없기 때문에 해석하고 최적화하기 어려움
- 학습 중에 IoU 점수가 높은 특징에 대해 높은 분류 점수를 생성. 반대로 IoU 점수가 낮은 특징에 대해 낮은 분류 점수 생성
- 따라서 분류 점수에 따라 모형이 선택한 상위 K개의 encoder feature에 해당하는 예측 상자는 분류 점수와 IoU 점수가 모두 높음

![image](https://github.com/user-attachments/assets/d86f01df-4809-4d2b-948d-fbc9d75fc2ae)




                     
