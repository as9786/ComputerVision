# Spatial Pyramid Pooling in Deep Convolution Networks for Visual Recognition

## 등장 배경
- CNN은 고정된 입력 영상 크기를 취함
- 고정된 입력 크기를 맞추기 위해서 crop, warp 등을 적용

![image](https://github.com/as9786/ComputerVision/assets/80622859/5754e483-2149-4cbc-b7b7-2c12e6e6b7ca)

- Crop : 영상의 일부를 자름
- Warp : 영상의 크기를 조절(Resize)
- Crop을 적용 시 잘린 부분만 CNN을 통과 => 전체 영상 정보 손실
- Warp를 적용하면 영상에 변형 발생. 위의 사진을 보면 등대가 가로세로비를 유지하지 못하고 CNN 통과
- CNN의 입력 크기가 고정되어야 하는 이유 : 전결합계층(Fully Connected layer)의 존재
- Convolution filter는 sliding window 방식을 이용하기 때문에 고정된 크기를 필요로 하지 않음
- SPPNet은 FC layer 이전에 spatial pyramid pooling layer를 추가하여 합성곱층이 임의의 크기로 입력을 취할 수 있게 함

![image](https://github.com/as9786/ComputerVision/assets/80622859/1e608322-1bd2-4abb-92de-538d31e0a2ba)

## SPP layer
- 5개의 합성곱층과 3개의 전결합층을 활용
- SPP layer 위치는 마지막 합성곱 층 이후에 위치

![image](https://github.com/as9786/ComputerVision/assets/80622859/c5a7db9d-9d4c-4039-9a56-d6351d6b36c1)

