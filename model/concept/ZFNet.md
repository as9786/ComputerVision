# Visualizing and Understanding Convolutional Networks: ZFNet

## 초록
- 새로운 시각화 기술을 도입하여 합성곱 층의 특징을 시각화하여 합성곲 신경망이 어떻게 동작하는지 이해하고, 더 좋은 모형 구조 고안

## 1. 서론
- 입력 영상이 모형 내부의 feature map을 어떻게 활성화시키는지 시각화
- 학습이 진행되는 동안 특징이 어떻게 학습되는지 시각화
- 입력 사진의 특정 부분을 가린 채 분류를 진행하면서 합성곱 신경망에서 분류가 어떻게 진행되는지 분석

## 2. 관련 연구
- 그동안 특징을 input image pixel space에 투영하여 시각화하려는 시도는 대부분이 첫 번째 층에서 진행
- 높은 층에서는 그러한 방법 작동 X. Hessian 등 수치적 계산 방법으로만 특징이 어떻게 형성되는지 대략적인 이해 제공

## 3. 방법
- AlexNet 기반

### 3-1. Visualization with a Deconvnet
- Conv -> ReLU -> Max pooling의 반대 과정을 수행함으로써 활성화를 입력 공간에 사상(Deconvnet)
- 각각의 합성곱 층에 해당하는만큼 deconvnet을 부착
- 원하는 활성을 입력 공간에 사상시키기 위해, feature map의 다른 활성은 모두 0으로 만든 후 feature map을 deconvnet에 통과
- Deconvnet : Unpooling -> Rectify -> Deconvolution

### 3-2. Unpooling
- Max pooling의 역연산
- 하지만 max pooling은 여러 값들 중 최대값만 남기는 연산이므로 완벽한 역연산 불가
- Switch라는 방법론 도입. Pooling이 일어나는 과정에서 최대값의 위치를 기록
- 최대값 위치는 최대값으로 채우고 나머지는 0으로 채움

### 3-3. Rectification
- ReLU의 역연산
- 음수값 복원이 안되지만, 큰 영향 X

### 3-4. Filtering
- Transposed convolution

