# EAST : An Efficient and Accurate Scene Text Detector

## Basic of scene text detection

- 기본적인 text detection 목표는 글자가 위차한 경계 상자 좌표를 최대한 정확히 맞추는 것
- 회귀 문제로 접근
- 합성곱 신경망으로 사진의 특징을 추출 후, decoder로 단어 영역을 생성
- Pixel마다 단어 영역이 될만한 여러 후보를 만든 뒤 그 중에서 학습을 통해 RoI를 추려냄
- 글자와 글자, 단어와 단어 사이 여백 등을 모두 탐지하여 정해진 규칙에 따라 단어 영역으로 합치는 algorithm도 존재

## Basic concept

- 기존 text detection model들이 3~5 차례 convolution block을 사용한 것과 달리 하나의 합성곱층을 사용 => 연산 시간 향상
- FCN을 활용해 단어가 포함된 rotated rectangle 또는 quadrilateral box를 에측(회전 또는 다각형 모형)

## 기본 구조

- 입력 : 사진
- 출력 : Rotated rectangle bounding box의 5개 정보(x1, y1, w, h, 각도)
- U자 모양의 FCN 구조를 사용해 더욱 정확한 localization

![image](https://github.com/as9786/ComputerVision/assets/80622859/33e70c29-9e85-435c-96e3-ed81d64a10e7)

- 합성곱 층을 지난 feature map은 decoder 영역에서 크기를 첫 입력과 가깝게 복원
- U-Net처럼 입력과 가까운 feature map끼리 결합하여 위치 정보를 살림
- 최종적으로 입력 크기의 1/4의 score map 생성
- 출력한 score map을 활용하여 최종적으로 구하고자 하는 상자를 출력

![image](https://github.com/as9786/ComputerVision/assets/80622859/148466cd-585d-4764-9169-b6e14ea00604)

![image](https://github.com/as9786/ComputerVision/assets/80622859/438c879e-25ab-4bff-b10d-eb742792f34e)

- 각 단어 영역을 어느정도 추정한 후, 각 pixel이 단어 영역 내에 있을 확률을 부과
- 단어 상자를 추정 한 후, 안의 pixel을 대상으로 상자 4개의 변과의 거리를 계산(4개의 channel 사용)
- 거리가 높게 나온다는 것은 4개의 변과 모두 거리가 멀다는 것이기에, 4가지 값이 모두 높게 나타나면 단어 영역의 중심일 확률이 높음
- 중심인 정보를 가지고 상자가 수평 기준 얼마나 회전했는지 각도 값을 저장
- 최종적으로 한 가지 score map + 다섯 가지 추가 정보가 담김
- 출력한 score map을 취합하여 임계값을 기준으로 최종적으로 구하고자 하는 상자를 출력

## 손실
- L = Ls(score map 간 차이) + $\lambda$Lg(5가지 정보 간 손실)

