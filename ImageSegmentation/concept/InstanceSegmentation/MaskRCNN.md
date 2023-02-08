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

