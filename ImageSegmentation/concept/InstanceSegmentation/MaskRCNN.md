# Mask R-CNN

![image](https://user-images.githubusercontent.com/80622859/217188053-da182ff7-3cb4-4b4a-a31f-63b8156fa37b.png)

- Faster R-CNN의 RPN에서 얻은 RoI에 대하여 객체의 class를 예측하는 분류기, bbox regressor와 평행으로 segmentation mask를 예측하는 mask branch를 추가한 구조
- Mask branch는 각각의 RoI에 작은 크기의 FCN이 추가된 형태
- Segmentation task를 보다 효과적으로 수행하기 위해서 객체의 spatial location을 보존하는 RoIAlign layer 추가
