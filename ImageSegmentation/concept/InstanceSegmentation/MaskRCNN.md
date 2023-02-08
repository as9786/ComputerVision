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



