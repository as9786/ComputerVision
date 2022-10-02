# You Only Look Once: Unified, Real-Time Object Dectection

## Abstract
- 기존의 multi-task 문제를 하나의 회귀 문제로 정의
- Image 전체에 대해서 하나의 신경망이 한 번의 계산만으로 bounding box와 class 확률을 예측

## 1. Introduction
- 기존의 검출(detection) model은 분류기를 재정의하여 검출기(detector)로 사용
- 객체 검출은 하나의 image 내에서 개는 어디에 위치해 있고, 고양이는 어디에 위치해 있는지 판단
- 객체 검출은 분류뿐만 아니라 위치 정보도 판단해야 함
- Image pixel로부터 bounding box의 위치, class probabilities를 구하기까지 일련의 절차를 하나의 회귀 문제로 재정의

![다운로드](https://user-images.githubusercontent.com/80622859/193463274-1d619eb4-a033-42d4-98f3-0f1281a0a081.png)

- 하나의 합성곱 신경망이 여러 bounding box와 그 bounding box의 class probabilities를 동시에 계산
- Image 전체를 학습하여 곧바로 검출 성능을 최적화
- 굉장히 빠름
- 예측할 때 Image 전체를 봄(Sliding window or region proposal X)
- Class의 모양에 대한 정보뿐만 아니라 주변 정보까지 학습하여 처리 => Background error가 적음
- Background error : 아무 물체가 없는 배경에 반점이나 noise가 있으면 그것을 물체로 인식하는 것
- 물체의 일반적인 부분을 학습
- 빠르게 객체를 검출할 수 있으나 정확성이 다소 떨어짐(특히 작은 물체에 대한 정확도가 떨어짐)

## 2. Unified Detection
- 객체 검출의 개별 요소를 단일 신경망으로 통합
- Input images를 S x S grid로 나눔
- 어떤 객체의 중심이 특정 grid cell 안에 위치한다면, 그 grid cell이 해당 객체를 검출
- 각각의 grid cell은 B개의 bouding box와 그 bounding box에 대한 confidence score를 예측
- Confidence score : Bounding box가 객체를 포함한다는 것을 얼마나 믿을만한지, 그리고 예측한 bounding box가 얼마나 정확한지

![다운로드 (1)](https://user-images.githubusercontent.com/80622859/193463556-1e178c86-eb98-4ab3-93df-adae0321aadf.png)

- IOU(Intersection over Union) : 객체의 실제 bounding box와 예측 bounding box의 합집합 면적 대비 교집합 면적의 비율
- IOU = (실제 bounding box와 예측 bounding box의 교집합) / (실제 bounding box와 예측 bounding box의 합집합)
- Grid cell에 아무 객체가 없다면 Pr(Object) = 0 -> confidence score = 0
- Pr(Object) = 1이 가장 이상적. 
- Confidence score = IOU일 경우 가장 이상적인 score 
- 각각의 bounding box는 5개의 예측치로 구성(x,y,w,h,confidence)
- (x,y)좌표 쌍은 bounding box 중심의 grid cell 내 상대 위치(0~1 사이의 값)
- 만약 bounding box의 중심인 (x,y)가 정확히 grid cell 중앙에 위치한다면 (0.5,0.5)
- (w,h) 쌍은 bounding box의 상대 너비와 상대 높이
- (w,h)는 image 전체의 너비와 높이를 1이라고 했을 때, bounding box의 너비와 높이가 몇인지를 상대적인 값으로 나타냄(0~1 사이의 값)
- confidence = confidence score
- 각각의 grid cell은 conditional class probabilities(C)를 계산

![다운로드 (2)](https://user-images.githubusercontent.com/80622859/193463873-d3efe12a-c261-4814-bc5b-3ba1157af16c.png)

- Grid cell 안에 객체가 있다는 조건 하에 그 객체가 어떤 class인지에 대한 조건부 확률
- Grid cell에 몇 개의 bounding box가 있는지와는 

