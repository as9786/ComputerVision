# Gradient-Based Learning Applied to Document Recognition

## 1. Introduction
- 사람이 일일이 설계한 특징들보다 자동화된 학습에 의존하는 것이 pattern recognition에 더욱 효과적
- 두 가지 인식 방법
1. Character recognition : 독립된 하나의 글자를 인식. ex) CNN
2. Document understanding : 여러 개의 글자가 모인 문장, 여러 문장이 모인 문서를 이해하는 과정 ex) Graph Transformer Networks
- Existing pattern recognition system

![캡처](https://user-images.githubusercontent.com/80622859/192315428-85fc105a-b92e-44c8-b153-771060688eee.PNG)

- Feature extractor : 입력값을 저차원의 vector로 변환. 이러한 형태는 쉽게 matching되고, class가 바뀌지 않는 선에서 변형이 강함
- Feature extractor는 사전 지식이 어느 정도 필요하며 수작업을 설계되기 때문에 시간 소요가 높음
- Trainable classifier : 보편적이고 학습 가능
- 다른 문제마다 새로운 feature extractor를 설계해야 하기 때문에 비효율적

- 아래의 3가지 요인으로 학습기의 성능 개선이 가능
1. 컴퓨터 성능의 향상으로 brute-force 계산 방법이 가능
2. Data의 크기 증가
3. 고차원의 입력을 다룰 수 있고 복잡한 결정을 내릴 수 있는 기계학습 등장. ex) 역전 오차파로 학습된 multi-layered neural networks
4

