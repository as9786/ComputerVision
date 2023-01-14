# FCN(Fully Convolution Network)

![image](https://user-images.githubusercontent.com/80622859/212460633-394dbd92-faed-4a90-9c94-dcbf7ed1b2a3.png)

- Image classfication에서 우수한 성능을 보인 CNN 기반 모형을 목적에 맞춰 변형
- Image classification model to semantic segmentation model
1. Convolutionalization
2. Deconvolution(Upsampling)
3. Skip architecture

## Convolutionalization
- Image classfication model들은 마지막에 전결합계층이 존재
- Segmentation에서 전결합계층을 사용할 경우 image의 위치 정보가 사라짐
- Segmentation의 목적은 원본 image의 각 pixel에 대해 class를 구분하는 것이므로 위치 정보가 중요
- 전결합층의 한계를 보완하기 위해 모든 전결합층을 Conv-layer로 대체

![image](https://user-images.githubusercontent.com/80622859/212460763-178c2562-8d73-4d80-8eca-897dc3069eec.png)

![image](https://user-images.githubusercontent.com/80622859/212460769-7afa0842-571b-4d1c-8d4b-baa228103f8c.png)

- Dense -> Conv layer

![image](https://user-images.githubusercontent.com/80622859/212460793-d87b0908-f72d-42cb-b56d-c22fabc43138.png)

- 이러한 과정을 통해서 나오는 결과값을 coarse feature map이라고 함
- Coarse feature map의 경우에는 원본보다 작음
- 이를 해결하기 위해 deconvolution, interpolation, upsampling 등이 있음

## Upsampling
- 처음부터 pooling을 사용하지 않거나 stride를 줄임으로써 feature map의 크기가 작아지는 것을 피할 수 있지만 이는 image의 context를 놓치는 단점
- Pooling의 중요한 역할 중 하나는 parameter를 감소시키는 것
- 
### Deconvolution
- 합성곱 연산을 거꾸로 해줌

![image](https://user-images.githubusercontent.com/80622859/212461178-b86d71a8-a656-4efc-96c6-cc2dc035847e.png)

- 사용되는 filter의 가중치 값은 학습 parameter

### Bilinear interpolation
- Linear interpolation : 두 지점 사이의 값을 추정할 때 직관적으로 사용하는 방법

![image](https://user-images.githubusercontent.com/80622859/212461131-a6b1dea4-c7e4-48c8-bfe7-db49eaf67081.png)

- Bilinear interpolation : Linear interpolation을 2차원으로 확대

![image](https://user-images.githubusercontent.com/80622859/212461145-4a3f9345-8041-4c4e-993d-e82352c733cd.png)

![image](https://user-images.githubusercontent.com/80622859/212461162-1e51e348-fd37-40c2-8f63-ae1aee3dafc6.png)

- 초기 segmentation model들은 VGG model을 convolutionalization한 구조에 bilinear interpolation 작업을 더함으로써 얻을 수 있음

![image](https://user-images.githubusercontent.com/80622859/212461220-1921201e-0acc-4392-a781-e711ee5a8e4e.png)

- 근본적으로 feature map의 크기가 너무 작기 때문에 예측된 dense map(예상 그림)의 정보는 여전히 정교하지 않음

![image](https://user-images.githubusercontent.com/80622859/212461240-43dc8f3d-b327-40e5-8544-a7bf97b0884a.png)

### Skip Architecture

- 추상적인 층의 의미적 정보와 외관적 정보를 결합

![image](https://user-images.githubusercontent.com/80622859/212461313-5c44c0dc-4e0b-4787-9a2f-bc672af18863.png)

- 얕은 층에서는 주로 직선 및 곡선, 색상 등의 낮은 수준의 특징에 활성화
- 깊은 층에서는 보다 복잡하고 포괄적인 개체 정보에 활성화
- 얕은 층에서는 local feature, 깊은 층에서는 global feature를 감지
- Dense map에 얕은 층의 정보를 결합

![image](https://user-images.githubusercontent.com/80622859/212461372-4b737d93-4efb-4781-83da-449adf356d7f.png)

![image](https://user-images.githubusercontent.com/80622859/212461393-bc05286e-a8df-4d86-88b4-61b08f0bfaa6.png)


