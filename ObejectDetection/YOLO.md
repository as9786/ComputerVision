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
- Grid cell에 몇 개의 bounding box가 있는지와는 무관하게 grid cell에는 오직 하나의 class에 대한 확률 값만을 구함
- 하나의 grid cell은 B개의 bounding box를 예측하지만 B의 개수와는 무관하게 하나의 grid cell에서는 class 하나만 예측

- Test 단계에서는 C와 개별 bounding box의 confidence score를 곱해줌, 이를 각 bounding box에 대한 class-specific confidence score라고 부름

![다운로드 (3)](https://user-images.githubusercontent.com/80622859/193464514-78ef6d7c-378c-4394-9673-f76bb5ade232.png)

- 이 점수는 bounding box에 특정 class 객체가 나타날 확률과 예측된 bounding box가 그 class 객체에 얼마나 잘 들어맞는지를 나타냄

![다운로드 (4)](https://user-images.githubusercontent.com/80622859/193464552-deee2169-2e16-41a0-94ff-9e880780e34c.png)

### 2.1 Network Design
- 하나의 CNN 구조로 design
- GoogleNet 기반

![다운로드 (5)](https://user-images.githubusercontent.com/80622859/193464575-d040f686-1d94-4080-a750-b6f44d99cb9e.png)

### 2.2 Training
- Imagenet dataset으로 사전훈련
- 신경망에서의 최종 예측값은 class probabilities와 bounding box coordinates
- Bounding box coordinates에는 x,y,h,w => 모두 0~1 사이로 정규화
- 마지막 계층에는 선형 활성화 함수를 적용했고, 나머지 모든 계층에는 leakyReLU 적용
- 손실은 SSE(Sum-Squared Error) 기반 (최적화가 쉬움, 하지만 mAP를 높이는 것에는 효과 x)
- Bounding box의 위치를 얼마나 잘 예측했는지에 대한 손실인 localization loss와 class를 얼마나 잘 예측했는지에 대한 classification loss가 있음

- Image 내 대부분의 grid cell에는 객체가 없음 -> 대부분의 grid cell의 confidence score = 0이 되도록 학습 => Model의 불균형
- 이를 개선하기 위해 객체가 존재하는 bounding box 좌표에 대한 loss의 가중치를 증가시키고, 객체가 존재하지 않는 bounding box의 confidence loss에 대한 가중치는 감소
- Localization loss의 가중치는 증가시키고, 객체가 없는 grid cell의 confidence loss보다 객체가 존재하는 grid cell의 confidence loss의 가중치를 증가
- $\lambda_{coord}=5, \lambda_{noobj} = 0.5$

- 큰 bounding box와 작은 bounding box에 대해 모두 동일한 가중치로 손실 계산
- 하지만 작은 것이 큰 것보다 위치 변화에 더 민감
- Bounding box의 너비와 높이에 제곱근을 취해줌
- 너비와 높이가 커짐에 따라 그 증가율이 감소해 손실에 대한 가중치를 감소시키는 효과

- 예측된 여러 bounding box 중 실체 객체를 감싸는 ground-trutg bounding box와의 IOU가 가장 큰 것을 선택
- 손실 함수

![다운로드 (6)](https://user-images.githubusercontent.com/80622859/193464906-4b5769bb-9803-4b86-a018-2c1f0367e94b.png)

### 2.3 Inference
- 하나의 객체를 여러 grid cell이 동시에 검출하는 경우 문제 발생
- 객체의 크기가 크거나 객체가 grid cell 경계에 인접해 있는 경우, 그 객체에 대한 bounding box가 여러 개 생김
- 이를 다중 검출(multiple detections) 문제라고 함
- 이는 비 최대 억제(non-maximal suppression)을 통해 개선

#### 비 최대 억제

![다운로드 (7)](https://user-images.githubusercontent.com/80622859/193465089-f30af544-d3b4-4ede-b724-79d2fb1d69d0.png)

1. 하나의 class에 대한 bounding boxes 목록에서 가장 높은 점수를 갖고 있는 bounding box를 선택하고 목록에서 제거, 그리고 final box에 추가
2. 선택된 bounding box를 bounding boxes 목록에 있는 모든 bounding box와 IoU를 계산하여 비교. IoU가 threshold보다 높으면 bounding boxes 목록에서 제거
3. bounding boxes 목록에 남아있는 bounding box에서 가장 높은 점수를 갖고 있는 것을 선택하고 목록에서 제거. 그리고 final box에 추가
4. 다시 선택된 bounding box를 목록에 있는 box들과 IoU 비교. Threshold보다 높으면 목록에서 제거
5. Bounding boxes에 아무것도 남아 있지 않을 때까지 반복

### 2.4 Limitations of YOLO
- 하나의 grid cell마다 두 개의 bounding box를 예측, 그리고 하나의 grid cell은 오직 하나의 객체만을 검출 => 공간적 제약
- 공간적 제약(Spatial constraints) : 하나의 grid cell은 오직 하나의 객체만을 검출하므로 하나의 grid cell에 두 개 이상의 객체가 붙어 있다면 이를 잘 검출하지 못하는 문제
- 훈련 단게에서 학습하지 못했던 새로운 종횡비를 마주하면 성능이 안 좋음
