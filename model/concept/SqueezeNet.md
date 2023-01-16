# SqueezeNet, AlexNet-Leval Accuracy with 50x fewer parameters and <0.5MB Model size

- AlexNet보다 50배 적은 parameter 수로 AlexNet과 동일한 정확도를 지닌 모형
- 용량도 0.5MB보다 적음
1. 연산량이 적고, 학습이 빠름
2. 실시간으로 정보를 전송해야 하는 업무에 적용 가능
3. FPGA(10MB로 용량이 제한되어 있는 memory)와 embedded system에 적용 가능

- embedded system : 기계나 기타 제어가 필요한 시스템에 대해 제어를 위한 특정 기능을 수행하는 컴퓨터 시스템으로 장치 내에 존재하는 전자 시스템

- Parameter의 수를 낮추고 정확도를 유지시키는 방법에 집중
- 8개의 fire module로 구성된 신경망
- Fire module이 model parameter를 감소시키는 역할

## Architetural design strategies
- 3가지 전략을 사용하여 fire module 만듦

1. 3x3 filter를 1x1 filter로 대체.(연산량이 9배 적음)
2. 3x3 filter로 입력되는 input channel의 수를 감소(합성곱층 연산량 : (input channel) x (Num of filter) x (filter size)
3. Pooling layer를 최대한 늦춤. 합성곱층의 출력이 고해상도를 지니게 함. 큰 크기의 feature map은 정확도를 높임

- 1, 2번은 정확도를 보존하면서 parameter 수를 감소시키는 전략
- 3번은 제한된 parameter 수에서 정확도를 높이는 방법

## The fire module

![image](https://user-images.githubusercontent.com/80622859/212581732-de7b7bd3-8bd9-45d7-8c49-c858c6229595.png)

- 두 개의 층으로 구성(Squeeze layer와 expand layer)
- Squeeze layer : 1x1 filter로만 구성
- Expand layer : 1x1 filter와 3x3 filter
- Squueze layer 내에 있는 1x1 filter들의 출력값은 하나로 합쳐져서 expand layer로 전달
- 초매개변수 : $s_{1x1}, e_{1x1}, e_{3x3}$
- $s_{1x1}$ : Squeeze layer에서 1x1 filter의 수
- $e_{1x1}$ : Expand layer에서 1x1 filter의 수
- $e_{3x3}$ : Expand layer에서 3x3 filter의 수
- $s_{1x1} < (e_{1x1} + e_{3x3})$, squeeze layer의 channel 수가 expand layer의 channel수보다 작게 설정 => 2번 전략

## The squeezenet architecture

![image](https://user-images.githubusercontent.com/80622859/212582134-47a0af73-267e-4909-8d76-657fe26b7d21.png)

- 3가지의 구조가 존재
- 첫 번째는 기본 구조, 두 번째는 simple bypass 추가, 세 번째는 complex bypass를 추가
- Bypass는 skip connection과 같은 개념
- Bypass를 이용하기 위해서는 input channel 수와 output channel 수가 같아야 함
- Complex bypass는 위의 문제점을 해결하기 위해 사용
- 성능은 두 번째 구조가 제일 좋음

![image](https://user-images.githubusercontent.com/80622859/212582530-bf71a5dc-4976-42eb-8212-4efe184ea7e2.png)

- Bypass를 추가한 이유는 fire module 내에서 bottleneck 문제가 발생 => 정보 손실 방지

## Evaluation of squeezenet

![image](https://user-images.githubusercontent.com/80622859/212582689-4fce323b-082a-40da-a13d-6459cf7764e8.png)

- AlexNet보다 parameter 수가 3배 감소

![image](https://user-images.githubusercontent.com/80622859/212582717-7434650f-5264-4b42-b32a-895699e596da.png)

- SqueezeNet을 적용했을 때, parameter 감소가 제일 컸고, AlexNet보다 성능 향상
- Deep compression을 적용시키면 더 압축시킬 수 있음
- Deep compression도 AlexNet에 parameter 수를 낮추기 위해 사용된 하나의 기법
- (Deep Compression: Compressing Deep Neural Networks with Pruning, Trained Quantization and Huffman Coding) 참조
