# SENet(Squeeze and Excitation Network)

## Squeeze and Excitation Network
- Channel-wise feature response를 조절

## 서론
- 합성곱 신경망은 영상 또는 feature map의 지역을 학습
- 지역은 수용 영역에 있는 정보들의 조합
- 조합들을 활성화 함수를 적용시켜 비선형 관계를 파악하고 pooling layer 등을 통해 해상도를 낮춤
- 합성곱 신경망은 전역적인 수용 영역의 관계를 효율적으로 다룸
- Goal : Improve the representational power of a network by explicitly modeling the interdependencies between the channels of its convolutional features
- 기존 신경망을 거친 feature map을 재조정(Feature recalibration)
- Squeeze operation : 각 feature map에 대한 전체 정보 요약
- Excitation operation : Squeeze operation을 이용해 각 feature map의 중요도를 scaling
-  SE block = Squeeze + Excitation operation
-  장점
1. 어떠한 곳이라도 바로 적용 가능
2. 가중치의 증가량에 비해 성능 향상이 큼 = 모형 복잡도와 계산 복잡도가 크게 증가 X

## Squeeze-and-Excitation Blocks

![image](https://github.com/as9786/ComputerVision/assets/80622859/825a4967-e0e3-45fe-9e51-6e6a99442809)

### Squeeze operation

- $F_{tr}$ 함수에 받아온 feature map U를 압축
- U는 각각 학습된 filter로부터 생성된 특징. 각 feature map channel들은 그 지역 밖에서는 맥락적인 정보로는 이용할 수 없음
- H x W x 6 size feature map에서 6 개의 channel은 서로 바라보는 관점이 다름
- 위와 같이 각각 다른 시선을 가지고 있기 때문에 전체 맥락적으로는 이용 X. 정보 활용이 제한
- U를 global average pooling을 통해 1 x 1 x C로 압축
- 압축된 feature map을 channel descriptor라고 함
- H x W x C를 대표하는 feature map

### Excitation operation

- Squeeze operation 결과로 1 x 1 x C가 나옴
- 선형 변환을 통해서 C/r로 node 수를 줄인 후, ReLU 통과
- 다시 선형 변환을 통해서 최종적으로 C만큼 값을 출력하여 sigmoid 함수를 통해 0~1 사이의 값을 지닌 C차원 vector 생성
- 차원을 줄이고 ReLU를 적용한 이유는 channel 간에도 비선형성을 가해주기 위함(Channel relationship)
- 최종적으로 해당 vector들을 U에 곱해줌
- SE block을 통해 U에서 어떤 channel에 집중해줄지 골라줌
