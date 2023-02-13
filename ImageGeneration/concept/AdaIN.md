# 구조

![image](https://user-images.githubusercontent.com/80622859/218445336-46ededf3-ae9e-48ab-9a2c-5fdb320be774.png)

- VGG pretrained model을 통해 encoding
- Decoder만 학습
- AdaIN으로 생성된 feature들이 decoder를 통해서 image space로 전환하는 법을 학습
- Learnable parameter X

# AdaIN layer

- Style Transfer : 특정 image에서 style을 뽑고, 다른 image에서 contents를 뽑아서 이를 합성
- Ex) 나무의자 : (의자, content), (나무, style)
- Feature space 상의 여러 통계량(평균, 분산)이 style을 표현하는데 유용

![image](https://user-images.githubusercontent.com/80622859/218445833-93b7f8aa-417a-4870-a1fd-42df69a8f50c.png)

- 원하는 contents를 담고 있는 image의 feature x에서, image의 style을 빼주고, 내가 입히고 싶은 style을 더해주는 방식

![image](https://user-images.githubusercontent.com/80622859/218446016-2ce68b8e-8a6f-4f56-9f1e-a95f226d36b0.png)

- Contents image에서 style을 빼줌
- 그 후 image y의 style을 입혀줌
- Feature space에서 
