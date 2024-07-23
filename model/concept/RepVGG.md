![image](https://github.com/user-attachments/assets/27e3f094-246a-4650-bf2a-b5cba25b99ae)- 훈련 때는 3 x 3, 1 x 1, identity convolution으로 이루어진 multi-branch 모형을 사용하되, 추론 때는 re-parameterization이라는 기법을 사용해 multi-branch를 3 x 3 convolution으로만 이루어진 plain modle로 바꾸어 활용
- 이를 통해 multi-branch로 더 정교하게 훈련된 가중치와 더 빠른 추론 속도를 얻음
- 3 x 3 convolution filter에 최적화된 추론용 hardware에 적합한 모형

# 서론

- InceptionNet의 branch-concatenation 같이 복잡한 multi-branch 구조를 사용해 모형을 만들거나 활용하기 어려움
- Xception이나 mobileNet 등에 있는 depthwise convolution은 memory allocation cost를 높이거나, 몇몇 hardware에서 지원 안 함
- 최신 모형보다 resnet, VGG 등 추론 속도가 빠른 모형이 여전히 사용
- 최신 모형의 단점들인 복잡성, 느린 속도 그리고 hardware 장치 범용성 등을 해결함과 동시에 높은 성능을 달성한 모형 제안(RepVGG)
- 추론 시에 사용하는 RepVGG는 VGG 형태의 plain model(3 x 3 convolution filter와 ReLU를 정직하게 쌓은 형태)
- ResNet과 같은 multi-branch model은 ensemble 형식

![image](https://github.com/user-attachments/assets/30fd5bba-7635-4345-9691-c3e0ca087602)

- 모형을 훈련 때와 추론 때 형태가 다름
- 훈련 : Multi-branch, 추론 : Plain
- 훈련 모형에서 추론 모형으로 바꾸는 것을 structual re-parameterization이라고 함
- 특정 구조의 가중치가 다른 구조와 결합된 다른 가중치로 변환될 수 있다면, 전자를 후자로 동등하게 대체 가능

# 관련 연구

## 1. From single-path to multi-branch
- ResNet, InceptionNet, DenseNet 그리고 NAS(Nueral Architecture Search)

## 2. Effective training of single-path models
## 3. Model re-parameterization
- DiracNet
## 4. Winograd convolution
- 3 x 3 convolution filter를 가속화하는 algorithm
- 일반 3 x 3 convolution filter보다 곱셈 연산이 4/9
- 핵심은 곱셈 연산을 줄이고 덧셈 연산을 늘림

# Building RepVGG via structual re-param

## 1. Simple is fast, memory-economical, flexible

### Fast
- 최근 모형들은 이론상 VGG보다 FLOPS가 작지만, 속도는 더 느림
- FLOPS와 속도 간의 불일치는 MAX(Memory Access Cost, 메모리 접근 비용)와 병렬도로 인해서 발생
- FLOPS는 위의 두 가지를 고려하지 않음
- MAC은 group wise convolution에서 많은 시간 사용
- 논문에서는 독립적인 convolution filter만을 사용해서 병렬도를 낮추지 않음으로써 연산 속도 증가

![image](https://github.com/user-attachments/assets/1b3808b1-f8da-4403-8173-4cd84429ce46)

### Memory-Economical
- Multi-branch model들은 그것을 더하거나 이어붙이기 위해서 multi-branch를 통과한 feature들을 유지해야 함 -> Memory 낭비

### Flexible
- Multi-branch model은 구조적으로 여러 가지 제약이 존재

## 2. Training-time multi-branch architecture
- 학습 시에는 multi-branch model

## 3. Re-param for plain inference-time model
- 1 x 1 convolution weights와 identity conv를 모두 3 x 3 conv로 바꾸는 것. conv + BN을 conv + bias로 교체

![image](https://github.com/user-attachments/assets/46ebafd6-32b2-48fb-ac2d-b51ca6c79230)
