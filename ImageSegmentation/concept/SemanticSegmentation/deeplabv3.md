# Encoder-Decoder with Atrous Separable Convolution for Semantic Image Segmentation

## ASPP

- 하나의 image를 다양한 크기의 조각으로 바라봄
- 풍부한 문맥적인 정보 추출

## Encoder-decoder structure

- 물체의 경계가 모호하지 않도록 공간적인 정보를 최대한 유지
- 기본적으로 encoder의 출력값들은 pooling과 stride를 적용한 합성곱으로 인해 물체 경계와 관련된 정교한 정보를 잃음

- ASPP + encoder-decoder

![image](https://user-images.githubusercontent.com/80622859/218962069-ea2e930b-257c-425a-a2a2-dac4e900c9cc.png)

## Depthwise separable convolution

- 정확도와 속도의 trade-off 해결 => 속도와 정확도에 모두 이점
- 일반적인 합성곱을 두 가지 과정을 통해 진행
- 1. Depthwise convolution 2. Pointwise convolution(1 x 1 convolution)
- 연산 복잡도를 크게 감소

![image](https://user-images.githubusercontent.com/80622859/218962556-63097510-5628-49c0-8892-d67add2947b8.png)

- 각 channel 마다 특정 kernel이 존재. 이 kernel을 통해 해당 channel에 대해서만 합성곱 연산 진행
- Pointwise convolution에서는 1 x 1 convolution 진행
- Astrous convolution에 depthwise separable convolution 적용

## Encoder

- Deeplab v3

![image](https://user-images.githubusercontent.com/80622859/218963335-2bcd36ca-87fa-431c-ab1a-c0269b9d3641.png)



