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
