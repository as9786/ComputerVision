# 1. Segmentation?

- Pixel 수준에서 각 영역이 어떤 의미를 갖는지 분리하는 방법
- Image 내의 영역 분리가 필요한 분야에서 많이 사용



## Semantic segmentation

![image](https://user-images.githubusercontent.com/80622859/211724988-93579048-127f-4dfb-90e6-5d83ade5585a.png)

- Grass, cat, tree, sky 라는 4개의 class의 위치를 인식(localization)하고, 판별(classification)하는 접근법

![image](https://user-images.githubusercontent.com/80622859/211725733-d0e244d8-7121-49c5-b4e9-76260a4f051f.png)

- Localization : 해당 사진 중 우리가 집중하고자 하는 부분을 골라냄
- Classification : 해당 사진이 특정 object를 나타내는지 판별
- Object detection : 사진에 보이는 해당 객체들을 각각 골라냄
- Semantic segmentation : 의미 대로 image 분할(pixel 분류)
- Instance segmentation : 객체대로 사진 분할(pixel 분류)
