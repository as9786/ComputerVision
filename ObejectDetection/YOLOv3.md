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
- 예측값이 실제값과 같으면 1
- 예측을 무시하는 임계점보다 높은 
