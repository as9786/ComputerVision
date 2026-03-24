# A ConvNet for the 2020s

## 초록
- Transformer and CNN are helping each other

## 서론
- The sliding window mechanism in swin transformer is ultimately a method derived from CNN. 모형 설계 시, 더 많은 비용

## 방법

### 1. Macro design
- Swin T uses hierarchical design so feature maps' resolution are different at each stage
- Stage compute ratio : 각 단계가 전체 연산량에서 차지하는 비중
- Stem cell : The beginning part of the network. 입력 영상을 어떻게 처리할 것인지
- Replace the stem of the CNN with a patchify layer

### 2. ResNeXt-ify
- Apply ResNeXt grouped convolution to pure ResNet
- Depthwise convolution

### 3. Inverted Bottleneck

<img width="696" height="229" alt="image" src="https://github.com/user-attachments/assets/ba449cf9-9ade-4c74-a511-142b9d5e4f82" />

### 4. Micro design
- ReLU -> GELU
- 배치 정규화 -> 층 정규화
