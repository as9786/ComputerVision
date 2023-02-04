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
