# Deformable Convolution Networks

- Deformable convolution, deformable RoI pooling
- 3 x 3 conv filter를 사용하면 3 x 3 수용 영역에서만 특징을 추출
- 이 경우에는 translation-invariance가 생겨 객체 탐지와 분할에 안 좋은 영향
- 해당 논문은 고정된 수용 영역에서만 특징을 추출하는 것이 아니라, 좀 더 유연한 영역에서 특징을 추출
- Grid 내의 값을 sampling하는 것이 아니라 좀 더 광범위한 grid cell의 값을 sampling

![image](https://github.com/as9786/ComputerVision/assets/80622859/e253657f-b93f-43a1-8bb6-4694bdcd7fa0)

- (a)는 standard convolution filter에서 값을 추출하는 영역. 이외에는 deformable convolution으로 값을 추출하는 영역
- 더 넓은 범위에서 값을 추출함으로 translation variance를 얻음

## Deformable Convolutional Networks

![image](https://github.com/as9786/ComputerVision/assets/80622859/6d75641b-d0c8-46bb-9bea-d996fe30847c)

- Input feature map에서 두 개의 가지로 나뉨
- 첫 번째 가지에서는 offset을 계산. 또 다른 가지는 offset의 정보를 받아 합성곱 연산을 수행해 출력
- Standard convolution filter equation

![image](https://github.com/as9786/ComputerVision/assets/80622859/7370c6fe-bb45-4289-b2fe-0ba0bbd61a8d)

- p : Location
- Deformable convolution은 offset을 추가

![image](https://github.com/as9786/ComputerVision/assets/80622859/a2a09a38-47ac-4c1e-89b8-592ad4c21153)

- Offset이 추가 되어 좀 더 넓은 범위의 grid 영역에서 특징을 추출
- 해당 offset은 학습 가능
- Offset은 아주 작은 값(소수가 될 수 있음)
- 소수점 위치의 값을 쌍선형 보간법을 통해 계산

![image](https://github.com/as9786/ComputerVision/assets/80622859/7a479f9a-2bdc-4051-b397-859d9e2da99c)

![image](https://github.com/as9786/ComputerVision/assets/80622859/e92de4df-1d75-4773-af80-5e134a8cf4ef)

![image](https://github.com/as9786/ComputerVision/assets/80622859/ddf21423-9fb1-4004-8016-7146e8f7bb9f)

- Deformable convolution을 적용하면, 객체 크기에 따라 수용 영역이 다름
- 표준 합성곱은 객체 크기와 상관 없이 고정된 영역에서 특징을 추출
- 일반적으로 객체 탐지나 분할은 사전 학습된 모형을 사용함
- 모든 층에 deformable convolutoon을 사용하는 것이 아니라, 마지막 층 몇 개만 변경

## Deformable RoI Pooling
- RoI pooling : RoI를 일정한 grid로 나누어서, 해당 grid에 속하는 값을 평균 또는 최대 값을 취하여 고정된 feature map 생성
- 생성된 RoI 범위 내에서 grid를 분할하는 것이 아니라, 생성된 RoI 범위보다 넓은 범위의 값을 이용하여 RoI pooling 수행

![image](https://github.com/as9786/ComputerVision/assets/80622859/5d3dcd9a-50f9-4fcd-afed-2bbadf4e94ed)

- Deformable convolution과의 차이점은 offset을 전결합 계층으로 계산
- RoI pooling으로 feature map을 생성하고, 여기에 전결합 층을 거쳐서 offset 생성
- Offset 정보를 활용하여 deformable RoI pooling을 수행해 최종 feature map 생성

## 결론
- 객체의 크기와 수용 영역은 상관관계가 있음
- 배경이나 큰 물체의 경우에 넓은 범위의 수용 영역이 필요
- 고정된 3 x 3 filter를 사용하는 것이 아니라 더 넓은 밤위에서 값을 추출하는 방법
- 기존의 합성곱 연산이 갖는 translation invariance를 deformable 방식으로 감소





