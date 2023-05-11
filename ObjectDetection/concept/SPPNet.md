# Spatial Pyramid Pooling in Deep Convolution Networks for Visual Recognition

## 등장 배경
- CNN은 고정된 입력 영상 크기를 취함
- 고정된 입력 크기를 맞추기 위해서 crop, warp 등을 적용

![image](https://github.com/as9786/ComputerVision/assets/80622859/5754e483-2149-4cbc-b7b7-2c12e6e6b7ca)

- Crop : 영상의 일부를 자름
- Warp : 영상의 크기를 조절(Resize)
- Crop을 적용 시 잘린 부분만 CNN을 통과 => 전체 영상 정보 손실
- 
