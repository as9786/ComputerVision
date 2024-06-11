# Swin Transformer V2: Scaling Up Capacity and Resolution

## 초록

- Swin transformer의 가중치를 최대 30억 개까지 확장하고, 1536 x 1536 해상도의 영상을 학습할 수 있도록 기술 제안
- Vision model은 크기의 불안정성 문제를 지님
- Downstream vision task는 고해상도 영상 또는 window를 요구함
- 저해상도로 사전 학습된 모형을 고해상도 모형으로 전이할 경우 대게 성능이 하락
- 해상도가 높을 때 GPU 문제
- 이와 같은 문제를 해결하기 위해 2 가지 방법 제안
1. Large vision model의 안정성을 개선하기 위한 post normalization & scaled cosine attention
2. 저해상도에서 사전 학습된 모형을 고해상도 영상으로 효과적으로 전이하기 위한 log-spaced continuous position bias technique
3. GPU memory 소비량을 크게 절약하여 일반 GPU로 large vision model을 학습할 수 있는 중요한 세부 구현

## 모형

### 3.1 A brief review of swin transformer

#### 정규화
- Swin transformer는 transformer와 ViT의 표준을 따름

![image](https://github.com/as9786/ComputerVision/assets/80622859/1e4a8a5c-403a-4c5d-a57c-3a2db1c97444)

- Swin transformer model을 소형에서 대형으로 확장하면 더 깊은 층의 활성화 값이 크게 증가
- 모형 전이 학습 시 고해상도에 적용할 경우 성능 하락. 상대적 위치 편향(Relative position bias) 조절할 필요가 있음
- Pre normalization은 모형 용량을 확장할 때, 더 깊은 계층에서 활성화 값이 크게 증가

### Post normalization

![image](https://github.com/as9786/ComputerVision/assets/80622859/1798592c-e19e-4cde-8bc2-b5e639264a65)

- Residual block의 출력은 병합되기 전에 정규화. 

![image](https://github.com/as9786/ComputerVision/assets/80622859/3a5b04c7-3213-48ca-8356-86c6f2fe7fe3)

- 각 층에서의 분산이 더 작아짐

### Scaled cosine attention
- Post normalization에서 large vision modle이 일부 층과 head의 학습된 attention map이 특정 pixel에 영향을 많이 받는 것을 확인
- 이를 완화하기 위해 scalied cosine function 사용

![image](https://github.com/as9786/ComputerVision/assets/80622859/510ddd3d-c956-42bc-b9d5-572ae0d480c3)

### Scaling up window resolution

- Window 해상도에서 relative position bias를 원활하게 전달할 수 있도록 하는 log-spaced continuous position bias
- Parameterized biases를 직접 최적화하는 대신, 상대적 좌표에 대한 meta network 채택
- ReLU 활성화 함수가 중간에 있는 2개 층으로 구성된 MLP

