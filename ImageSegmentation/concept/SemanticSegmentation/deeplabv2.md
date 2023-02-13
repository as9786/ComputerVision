- Atrous convolution을 사용한 DCNN 부분에 다양한 dilation rate를 사용한 atrous convolution을 하는 ASPP module 사용하여 multi-scale object를 segment할 수 있음을 강조
- VGG16, ResNet101에 일반적인 합성곱을 ASPP(Atrous spatial pyramid pooling)으로 대체 => 연산량은 적지만 큰 범위의 receptive field를 cover

# Multiscale Image Representations using Atrous Spatial Pyramid Pooling(ASPP)

![image](https://user-images.githubusercontent.com/80622859/218460382-4fb2b50f-1737-46e7-8da3-f9815465e984.png)

- Feature map의 한 pixel 값을 얻기 위해 4개의 atrous filter를 사용
- 각 합성곱을 적용한 뒤에 얻은 값을 더해 마지막 결과를 생성
- 1개의 filter를 사용할 때보다 성능이 증가하지만 계산량도 증가

![image](https://user-images.githubusercontent.com/80622859/218460613-bc4b7aeb-5fb1-4756-87e9-e007c0695797.png)

![image](https://user-images.githubusercontent.com/80622859/218460983-551ecc49-9958-4f7e-a343-33d73187479a.png)
