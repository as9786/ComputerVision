# Computer Vision with Python

- 각각의 이미지는 하나의 배열로 나타낼 수 있음
- 더욱더 많은 픽셀이 있을 수록 높은 해상도

## 흑백 사진
- 기본 이미지는 배열로 불러왔을 때 0과 255 사이의 값을 가짐
- 255는 가장 밝은 값, 0은 가장 어두운 값
- 0~1 사이로 정규화시키는 경우가 많음

## Color Image
- RGB는 다양한 색을 만들수 있도록 도와줌
- RGB로 구현 못하는 값은 회색으로 처리 -> 하지만 RGB로 충분
- Image를 읽을 때 3가지 차원을 가지게 됨 => 높이 차원, 너비 차원, color channel(RGB)
- ex) (1280,720,3) = 1280 pixel width, 720 pixel height, 3 color channels
- 3차원 배열
- 사용하는 software에 따라 색깔 다르게도 나올 수 있음
- 각각의 channel은 하나의 회색조 그림
