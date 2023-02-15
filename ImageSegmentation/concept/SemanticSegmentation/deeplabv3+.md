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

- 일반적인 합성곱의 경우 입력 이미지가 8 x 8 x 3이고, convolution filter가 3 x 3이라 할 때, filter 한 개가 가지는 paramter의 수는 3 x 3 x 3 = 27
- Filter를 16개 적용 시 27 * 16 = 432

![image](https://user-images.githubusercontent.com/80622859/218966015-aa108279-0857-4188-be16-1b021350529e.png)

- Deptwise convolution

![image](https://user-images.githubusercontent.com/80622859/218966069-b4ed5945-f759-452a-9bd2-4df67aabd8d9.png)

- Channel 축을 모두 분리시킨 후 channel을 항상 1로 가지는 여러 개의 convolution filter로 대체시켜 연산
- 그 후 pointwise 연산(Deptwise separable convolution)

![image](https://user-images.githubusercontent.com/80622859/218966340-b1cfa841-912c-4da5-aed1-c4c96c04a1d4.png)

- 3 x 3 x 3 + 3 x 16 = 75


## Encoder

- Deeplab v3

![image](https://user-images.githubusercontent.com/80622859/218963335-2bcd36ca-87fa-431c-ab1a-c0269b9d3641.png)



