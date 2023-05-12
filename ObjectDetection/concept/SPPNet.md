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

- Spatial bins 설정
- 50 bin = [6x6, 3x3, 2x2, 1x1], 30 bin = [4x4, 3x3, 2x2, 1x1]
- Spatial bin은 conv5의 feature map에 pooling을 적용하여 생성되는 출력 크기
- 위의 그림에서는 21 bin = [4x3, 2x2, 1x1]인 경우
- Pooling이 적용된 feature map을 평탄화
- 하지만 압력 크기가 다양하므로 conv5의 feature map의 크기도 다양
- 다양한 feature map에서 pooling의 결과값이 같게 나오기 위해 window size와 strdie를 조절
- Window size(Pool size) = ceiling(feature map size / pooling size)
- Strdie = floor(feature map size / pooling size)
- 위의 공식을 사용하면 어떠한 크기의 feature map이 오더라도 고정된 pyramid size를 얻을 수 있음

![image](https://github.com/as9786/ComputerVision/assets/80622859/49faa692-67e8-423e-bad2-2aa2b447cdec)

- 위의 예시의 경우 14 bin = [3x3, 2x2, 1x1]
- Conv5 feature map size = 13 x 13
- Window size = ceiling(13 / 3) = 5, stride = floor(13 / 3) = 4
- SPP layer의 출력 차원은 k x M(고정된 차원)
- k : conv5 layer에서 출력한 feature map의 filter 수
- M : 사전에 설정한 bin

## SPPNet 동작 과정

![image](https://github.com/as9786/ComputerVision/assets/80622859/ed6cf598-cb20-46cd-8c95-91511afc37f3)

1. Selective search를 사용하여 약 2000 개의 region proposals 생성
2. 영상을 CNN에 통과시켜 feature map 얻기
3. 각 영역 제안으로 경계까 제한된 feature map을 SPP layer에 전달
4. SPP layer를 적용하여 얻은 고정된 vector representation을 전결합 계층에 전달
5. SVM으로 분류
6. 경계 상자 추정으로 경계 상자의 크기를 조정하고 비 최대 억제를 사용하여 최종 경계 상자를 선별

