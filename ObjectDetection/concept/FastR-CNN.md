- 기존 R-CNN model 학습 시간이 오래 걸림
- 이러한 문제점을 해결

# Fast R-CNN model

## Preview

![image](https://user-images.githubusercontent.com/80622859/216759445-4bd5c631-901f-44ec-b714-ac648d59b5b2.png)

- R-CNN은 2000장의 영역 제안들을 합성곱 신경망에 입력시켜 각각에 대하여 독립적으로 학습
- Fast R-CNN은 단 1장의 image를 입력받으며, warp하지 않고 RoI(Region of Interest) pooling을 통해 고정된 크기의 feature vector를 전결합 계층에 전달
- Multi-task loss를 사용하여 모형을 개별적으로 학습시킬 필요 없이 한 번에 학습

## Main Ideas

### 1. RoI pooling

- Feature map에서 region proposals에 해당하는 관심 영역(Region of Interest)을 지정한 크기의 gird로 나눈 후 max pooling을 수행
- 각 channel 별로 독립적으로 수행 => 고정된 크기의 feature map을 출력

![image](https://user-images.githubusercontent.com/80622859/216759601-251d5207-48dd-4aee-b709-81150a350a82.png)

1. 원본 image를 합성곱 신경망에 통과시켜 feature map을 얻음
- 위의 그림에서는 VGG model 넣어 8 x 8 feature map을 얻음
- Sub-sampling ratio : Image size가 줄어드는 비율

2. 동시에 원본 image에 대하여 선택적 탐색을 적용하여 후보 영역들을 얻음

3. Feature map에서 각 후보 영역에 해당하는 영역을 추출(RoI projection)
- SS를 통해 얻은 후보 영역들은 sub-sampling을 거치지 않은 반면, 원본 image의 feature map은 sub-sampling 과정을 여러 번 거쳐 크기가 작아짐
- 작아진 feature map에서 후보 영역이 표현하고 있는 부분을 찾기 위해 작아진 feature map에 맞게 후보 영역을 투영해주는 과정이 필요
- 후보 영역의 크기와 중심 좌표를 sub sampling ratio에 맞게 변경시켜줌
- 후보 영역의 중심점 좌표, 너비, 높이와 sub-sampling ratio를 활용하여 feature map으로 투영
- Feature map에서 후보 영역에 해당하는 5 x 7 영역을 추출

4. 추출한 RoI feature map을 지정한 sub-window 크기에 맞게 grid로 나눠줌
- 추출한 5 x 7 영역을 지정한 2 x 2 크기에 맞게 grid를 나눠줌

5. Grid의 각 cell에 대하여 max pooling을 수행하여 고정된 크기의 feature map을 얻음

- 이처럼 미리 지정한 크기의 sub-window에서 max-pooling을 수행하여 고정된 크기의 feature map을 얻음

### 2. Multi-task loss

- Classifier와 box regressor를 동시에 학습
- 각각의 RoI에 대하여 mulit task loss를 사용하여 학습

![image](https://user-images.githubusercontent.com/80622859/216760294-9126e45e-fe2a-4ea8-a9f1-6e34491a0be8.png)

- K개의 class를 분류한다고 할 때, 배경을 포함한 (K+1) 개의 class에 대하여 분류기를 학습
- u는 positive sample인 경우 1, negative sample인 경우 0으로 설정(Index parameter)
- L1 loss는 R-CNN, SPPnets에서 사용한 L2 loss에 비해 이상치에 덜 민감
- $\lambda = 1$ 
- mAP를 상승

### 3. Hierarchical Sampling

- R-CNN model은 학습 시 후보 영역이 서로 다른 image에서 추출되고, 이로 인해 학습 시 연산을 공유할 수 없음
- SGD mini-batch를 구성할 때 N개의 image를 sampling하고, 총 R개의 region proposal을 사용한다고 할 때, 각 image로부터 R/N개의 region proposals를 sampling하는 방식
- 연산과 memory를 공유
- N = 2, R = 128
- 서로 다른 2장의 images에서 각각 64개의 후보 영역을 추출하여 sampling하여 mini-batch를 구상
- 16장은 ground truth와 IoU의 값이 0.5 이상인 sample을 추출, 나머지는 negatvie sample 추출
- 전자의 경우에는 u = 1, 후자인 경우에는 u = 0

### 4. Truncated SVD

- RoI를 처리할 때 전결합 계층에서 시간이 오래 걸림
- 이러한 문제를 해결하기 위해 truncated SVD를 통해 전결합 계층을 압축

![image](https://user-images.githubusercontent.com/80622859/216760648-c71f0c7e-1d3b-487c-8f52-4d1c67097c6b.png)

![image](https://user-images.githubusercontent.com/80622859/216760688-dc755f26-40ed-458c-918f-8bdd98438349.png)

- 전결합 계층의 가중치 행렬이 W(u x v)이라고 할 때, truncated SVD를 통해 위와 같이 근사
- Parameter의 수를 t(u + v)로 감소
- 전결합 계층이 두 개로 나누어 짐
- 첫 번째 전결합 계층은 $\sum_t V^T$, 두 번째 전결합 계층은 U 가중치 행렬
- 시간이 30% 감소

# 



