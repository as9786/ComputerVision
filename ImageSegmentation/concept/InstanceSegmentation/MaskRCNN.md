# Mask R-CNN

![image](https://user-images.githubusercontent.com/80622859/217188053-da182ff7-3cb4-4b4a-a31f-63b8156fa37b.png)

- Faster R-CNN의 RPN에서 얻은 RoI에 대하여 객체의 class를 예측하는 분류기, bbox regressor와 평행으로 segmentation mask를 예측하는 mask branch를 추가한 구조
- Mask branch는 각각의 RoI에 작은 크기의 FCN이 추가된 형태
- Segmentation task를 보다 효과적으로 수행하기 위해서 객체의 spatial location을 보존하는 RoIAlign layer 추가

# Main ideas

## Mask branch

- Faster R-CNN 구조

![image](https://user-images.githubusercontent.com/80622859/217403761-58db4533-8cba-4e30-95aa-dc79924e9e32.png)

- Backbone network를 통해 얻은 feature map을 RPN에 입력하여 RoIs를 얻음
- RoI pooling을 통해 고정된 크기의 feature map을 얻고 이를 전결합 계층에 입력한 후 분류와 bbox regressor에 입력하여 class label과 bbox offset이라는 두 가지 결과 예측

- Mask R-CNN 구조

https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fcx1zeb%2FbtqWX5EbBpp%2FSDi2o1RDnpCCs2ckVpA8d0%2Fimg.png

- 분류기와 bbox regressor와 평행으로 segmentation mask를 예측하는 mask branch가 추가된 구조
- RoI pooling을 통해 얻은 고정된 크기의 feature map을 mask branch에 입력하여 segmentation mask를 얻음
- Segmentation task는 detection task보다 더 정교한 spatial layout(공간에 대한 배치 정보)를 필요
- Mask branch는 여러 개의 합성곱층으로 구성된 FCN 구조
- Image 내 객체에 대한 공간 정보를 효과적으로 encode 가능

![image](https://user-images.githubusercontent.com/80622859/217405803-02b32abc-170a-43d9-94e5-68f97cbb1253.png)

- 각각의 RoI에 대하여 class별로 binary mask를 출력
- Pixel이 해당 class에 해당하는지 여부를 표시
- $K^2 m$ 크기의 feature map 출력
- K = class 수, m = feature map 크기

## RoIAlign

- RoI pooling으로 인해 얻은 feature와 RoI 사이가 어긋나는 misalignment가 발생할 수 있음
- 이는 pixel mask를 예측하는데 안 좋은 영향을 줌

![image](https://user-images.githubusercontent.com/80622859/217406579-a7eaf22e-ce11-4682-94ae-789a260e3f2c.png)

- RPN을 통해 얻은 RoI를 추출한 feature map의 크기 맞게 투영하는 과정이 있음
- 위의 그림의 경우 제안된 영역의 크기는 (145, 200), feature map의 크기는 (16, 16) => Sub-sampling을 통해 (4,6)으로 RoI 정해짐(실제 값은 (4.53,6.25))
- 3 x 3의 고정된 크기를 얻기 위해 RoI pooling 진행(Stride=(1,2))

![image](https://user-images.githubusercontent.com/80622859/217407133-d0e664e4-5163-426f-8298-59e9ca27d410.png)

- Sub-sampling 및 RoI pooling 과정에서 실수값을 이산 수치로 제한(Quantization)
- 이는 불일치 문제 유도
- 위의 그림에서 초록색과 파란색 영역의 정보 손실
- RoI pooling 시 feature map의 마지막 row에 대한 정보 손실
- 이러한 문제를 해결하기 위해 RoIAlign 사용

### RoIAlign

![image](https://user-images.githubusercontent.com/80622859/217408161-366f01a5-a54a-4d02-8a7b-8cc83f4edd89.png)

1. RoI projection을 통해 얻은 feature map의 크기를 quantization 과정 없이 그대로 사용. RoI pooling도 마찬가지
2. 분할된 하나의 cell에서 4개의 sampling point를 찾음(cell의 높이, 너비를 3등분하는 점)
3. Bilinear interpolation 적용

![image](https://user-images.githubusercontent.com/80622859/217407668-74f8231f-f40f-48e1-89cd-376ec4bfeee2.png)

4. 2~3 과정을 모든 cell에 대하여 반복

![image](https://user-images.githubusercontent.com/80622859/217409993-ad600eeb-60d8-4736-a453-fcc72386e7a4.png)




