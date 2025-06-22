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

                     
