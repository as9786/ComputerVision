# Cascade R-CNN : Delving into High Quality Object Detection

- 일반적으로 낮은 IoU threshold 값을 지정하면 bbox 결과값이 부정확하고, IoU의 값을 높게 설정하면 bbox의 결과값이 정확한 대신 탐지의 전체 성능이 감소
- 많은 영역을 검출하지 못하기 때문에 recall이 감소해 AP가 감소
1. IoU가 높으면 positive sample이 많이 줄기 때문에 과적합 발생
2. 학습과 추론 시 작용하는 IoU가 다름 ex) 0.5 IoU로 학습한 모형은 COCO metric에 따라 0.5~0.9 IoU 범위로 test 진행

- Cascade R-CNN은 위의 두 문제점을 해결하기 위해 IoU를 증가시키면서 연속적으로 탐지기를 학습
- 낮은 IoU로 학습된 탐지기의 출력값으로 좀 더 높은 IoU를 설정해 탐지기를 학습
- 단계가 진행될수록 좀 더 정확한 영역을 학습 
- IoU가 높게 설정된 탐지기들은 대부분의 positive sample을 무시하지만, 이 논문에서 제시한 방법으로 학습을 진행 시 매 단계를 거치면서 좀 더 정확한 영역이 생성되면서 positive sample이 무시되는 비율 감소

![image](https://user-images.githubusercontent.com/80622859/226254579-56618d3e-287b-4d63-9ebf-db516a5c03b0.png)

- (a)와 (b)를 보면 IoU 기준이 더 낮은 (a)의 경우 false positive가 더 많이 나옴(실제로 false인데 postive라 예측)
- (d)를 보면 IoU가 높다고 성능이 좋은 것은 아님
- (c)는 입력으로 주어지는 bbox의 IoU가 서로 다를 때 각각의 IoU를 기준으로 학습시킨 분류기가 만들어낸 경계 상자의 정확도를 표현
- 입력 IoU가 높아질수록 출력 IoU도 높아짐
- 후보 영역의 정확도가 높이지면 출력값도 정확
- Cascade R-CNN은 좀 더 정확한 영역을 생성하기 위해 낮은 IoU로 학습된 탐지기들이 생성한 후보 영역으로 다음 탐지기를 학습
- 매 단계가 지날 수록 후보 영역의 정확도는 높아지고, 설정한 IoU도 높아지므로 탐지기의 성능이 향상

## Cascade R-CNN

![image](https://user-images.githubusercontent.com/80622859/226253782-bd30e9f7-62ab-476e-959a-643b072d96a0.png)

- 기존의 faster R-CNN은 1개의 분류기만 사용. Cascade R-CNN은 추가적인 n개의 분류기 사용
- 해당 분류기는 순차적으로 이전의 분류기가 만들어낸 경계 상자를 받아서 새로운 분류 작업을 수행하고 거기서 만들어지는 경계 상자를 다음 분류기에 전달
- 각각의 단계에서 만들어내는 경계 상자는 점점 더 정확할 것이라는 가정. 그 다음 단계의 분류기는 이전 단계보다 어 높은 IoU를 기준으로 학습

### Iterative BBox at inference

- Faster R-CNN처럼 하나의 분류기만 학습시켜 두고, test 시에 반복적으로 활용
- 입력이 들어가고 RPN을 거쳐 분류기가 bounding box를 생성해내면 이 경계 상자는 RPN이 만들어낸 경계 상자보다 더 정확
- 동일한 분류기에 이전에 본인이 예측한 경계 상자를 다시 수행
- 성능 향상, 그러나 극적인 효과 X
- 2번 이상의 반복은 성능 향상 X

### Integral Loss

- 서로 다른 IoU를 기준으로 각각의 분류기를 학습시키고, ensemble
- 성능 향상은 있지만 후보 영역이 정확하지 않다는 문제

### Cascade RC-NN
- 0.5 IoU로 학습한 탐지기로 후보 영역을 생성하고, 생성된 후보 영역으로 0.6 IoU인 탐지기를 학습
- 이 탐지기의 결과값으로 0.7 IoU인 탐지기를 학습하여 최종 출력값을 도출
- 3 단계로 구성. 이보다 많은 단계는 학습 성능 하락
- 추론 시에도 cascade 구조 사용

## 성능

![image](https://user-images.githubusercontent.com/80622859/226253931-5b10dede-fcc4-45b5-8484-8169ce7852e1.png)
