# YOLOv3: An Incremental Improvement

## Abstract
- 이전 model보다 몇 가지 update한 model
- 시간이 조금 걸리지만 더 좋은 정확도를 가짐
- SSD와 성능이 비슷하지만 속도는 3배 빠름


## 1.Introduction
- TECH REPORT

## 2.The Deal

### 2.1 Bounding Box Prediction
- 신경망은 각각의 bounding box의 4가지 위치를 예측 $(t_x,t_y,t_w,t_h)$

![캡처](https://user-images.githubusercontent.com/80622859/194057593-b088371f-307b-428b-9010-036519a89908.PNG)

- 학습동안 SSE 손실함수 사용
- Logistic regression을 사용하여 각각의 bbox에 대해 objectness score 계산
- Bbox 안에 물체의 유무 판단
- 여러 개의 anchor box 중에서 정답 box의 IoU가 가장 높은 box를 1로 두어 matching
- 그 외 box는 무시
- IoU의 임계값으로 0.5 사용

### 2.2 Class Prediction
- 각 box는 multi-label classification을 사용하여 bounding box가 포함할 수 있는 class를 예측
- Softmax 대신 logistic classifiers(sigmoid, ReLU, tanh 등) 사용
- 손실 함수도 categorical crossentropy가 아니라 binary crossentropy 사용
- 이와 같은 과정은 좀 더 복잡한 dataset으로 YOLO를 학습하는 것에 도움을줌

### 2.3 Predictions Across Scales
- 세 가지 다른 scale에서 box를 예측
- 위의 세 가지 scale의 features를 추출
- 각 scale에 대해 3개의 box 생성
- 3개의 pyramid의 level에서 특징을 추출
- Darknet-53에 여러 합성곱층 추가
- 추가된 합성곱층은 feature pyramid를 생성하기 위한 용도로 이용(upsampling)
- 최종 feature map에 upsampling을 2번 함
- Anchor box를 생성할 때 K-means clustering 사용
- 3개의 scale에서 3개의 box를 사용하므로 9개의 anchor box 필요

## 4.Feature Extractor 
- Backbone network : Darknet-53
- 53개의 계층으로 구성된 합성곱 신경망
- Resnet에서 제안된 shortcut connection 사용

![다운로드](https://user-images.githubusercontent.com/80622859/194068473-56c32ec3-164d-40d7-848a-fec2bc682359.png)

## Result

![다운로드 (1)](https://user-images.githubusercontent.com/80622859/194068519-92b92837-42d5-4b8c-b7b0-2fd3bf04fe46.png)



