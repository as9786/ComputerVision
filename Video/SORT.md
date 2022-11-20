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
