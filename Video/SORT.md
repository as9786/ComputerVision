# Simple Online and Realtime Tracking

## 1. Multiple Object Tracking(MOT)
- 다중 객체 추적
- 다수의 객체들을 추적하기 위해 탐지 결과 관 연관을 수행하는 과정
- 즉, 탐지된 객체 정보를 기반으로 각 frame 간의 동일 객체에 대한 탐지 반응을 연관하여 각 객체에 대한 전체 궤도를 완성
- Robust한 MOT를 위해 다양한 data association algorithm 개발
- 객체 탐지 결과와의 결합 유무에 따라 크게 **detection-free-tracking 방식** 과 **tracking-by-detection 방식**으로 구분
- 최근에는 **tracking-by-detection 방식**으로 대부분의 연구가 진행

![image](https://user-images.githubusercontent.com/80622859/202890257-7b24c01c-bb46-4b10-8aa7-86e822cb772b.png)

### Tracking-by-detection의 과정

![image](https://user-images.githubusercontent.com/80622859/202890281-9bd99c75-f5ce-4ed7-897b-7b1f9452da94.png)

- Batch tracking 방식과 Online tracking 방식으로 구분

#### Batch tracking
- 전체 tracking 궤도를 형성하기 위해 전체 frame에서 탐지된 모든 객체 정보에 대해 반복적인 객체 반응 연관을 수행
- 전체 frame에 대한 객체 탐지 정보를 사용하여 tracking 궤도를 형성하기 때문에 online tracking 보다 좋은 성능을 보임
- 그러나, 사전에 전체 frame에 대한 객체 탐지 정보를 가지고 있어야 하기 때문에 실시간 기능에 적용하기는 어려움

#### Online tracking
- 미래 frame에 대한 정보 없이 과거와 현재 frame object detection 정보만을 사용하여 tracking orbit 형성을 위한 탐지 반응 연관을 수행하는 방식
- 실시간 기능에 더 적합
- Future frame infomation의 부재로 인하여, 긴 기간이나 객체 외형 변화에 취약
- Tracking orbit 형성을 위한 탐지 반응 연관이 어려움
- Track fragment 및 identity switched 현상을 발생 시켜 성능 저하

![image](https://user-images.githubusercontent.com/80622859/202890467-85efbf50-3d9c-4ef4-b096-fc9f24dabec3.png)

## 2. Methodology

![image](https://user-images.githubusercontent.com/80622859/202890477-9bc52b2b-2f3d-42ca-b0fd-bc22a0f78c64.png)

### (1) Detection
- Faster RCNN detection framework를 이용

#### Faster RCNN

![image](https://user-images.githubusercontent.com/80622859/202890562-c7cf7773-1046-4391-87b9-44fb1a430782.png)

- 두 단계로 구성된 end-to-end framework
- 첫 번째 단계에서 특징을 추출
- 두 번째 단계에서 영역을 정해서, 각 후보 영역에 대해 합성곱 신경망을 사용하여 해당 영상에 대해 분류
- R-CNN family의 객체 탐지 신경망은 높은 성능을 보이지만, 처리 속도가 매우 느림
- 다른 구조로 교체 가능. ex) SSD, YOLO
- 탐지 품질이 tracking performance에 상당한 영향을 미침

### (2) Estimation Model
- Object tracking의 작업은 객체의 위치를 예측하는 것
- Motion estimation 방법으로 이전 순간의 target state에서 현재 순간의 target state를 예측하는 Kalman filter 방법을 사용
- Kalman filter는 초창기 방법이고, 현재는 순환신경망 기반의 motion model을 사용

#### Kalma filter

![image](https://user-images.githubusercontent.com/80622859/202890808-a81dc52c-17e7-4932-b581-73f47eab229d.png)

- Noise가 선형적 움직임을 가지는 target state를 추적하는 recursive filter
- 확률 이론에 기반
- Noise를 포함한 data가 입력되었을 때, noise를 고려하여 정확한 추정이 가능
- 시간에 따라 진행한 측정을 기반으로 하기 때문에 해당 순간에만 측정한 결과만 사용하는 것보다는 좀 더 정확한 추정이 가능
- 바로 이전 시간 외의 측정값은 사용 X
- 각 추정 계산은 예측과 보정 두 단계로 나눔
- 예측 : 이전 시간에 추정된 상태에 대해, 그 상태에서 입력이 들어왔을 때 예상되는 상태를 계산하는 단계
- 보정 : 앞서 계산된 예측 상태와 실제로 측정된 상태를 토대로 정확한 상태를 계산하는 단계
- 동영상의 이전 frame에서 객체 탐지기를 통해 얻어진 target state(bbox 좌표)를 통해, 이후 frame의 target state를 예측

![image](https://user-images.githubusercontent.com/80622859/202890958-45897429-4b95-44d1-af9b-a235f796d548.png)

### (3) Data Association
- MOT 방법을 기반으로 한 tracking-by-detection
- Hungraian problem : Data association optimization method
- Kalman filter를 이용해 확보한 예측값은 이후 frame에서 새롭게 탐지한 객체와의 연관에 적용
- 기존 target들의 각 탐지와 모든 예측되는 bbox들 사이의 IoU distance로 assignment cost matrix를 계산
- 그리고 hungarian algorithm을 사용하여 최적으로 해결

![image](https://user-images.githubusercontent.com/80622859/202891109-5c942e49-e230-4e42-8936-94b5a7d78bcd.png)

- (a) : Kalman filter에서 나온 결과
- (b)의 초록색 : 현재 탐지기에서 나온 bbox
- 위의 둘을 IoU 시킨 후 hungarian에서 짝을 찾아 주어 (c)처럼 ID가 할당

## 3. Experiments

### (1) Metrics
- 하나의 단일 점수를 사용하여 성능을 평가하기가 어려움
- MOTA : MOT accuracy
- MOTP : MOT 정밀도
- FAF : Frame 당 오경보 수
- MT : 주로 추적되는 궤적의 수
- ML : 대부분 손실된 궤적의 수
- FP : 잘못된 탐지 수
- FN : 놓친 탐지 수
- ID SW : ID가 이전에 추적된 다른 객체로 전환된 횟수
