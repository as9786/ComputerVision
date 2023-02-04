# Main idea

- Region Proposal Network(RPN)
- 기존 Fast RCNN 구조를 그대로 계승하면서 selective search를 제거하고 RPN을 통해 RoI를 게산
- 이를 통해 GPU를 통한 RoI 계산이 가능
- Selective search는 2000rodml RoI를 계산하는데 반해 RPN은 800개 정도의 RoI를 계산

![image](https://user-images.githubusercontent.com/80622859/216763917-699919e6-2306-4e28-b578-108621a24f90.png)

- Feature map을 추출한 다음 RPN에 전달하여 RoI를 계산
- 얻은 RoI로 RoI pooling을 진행한 다음 분류를 진행하여 객체 탐지를 수행

# Region Proposal Network

![image](https://user-images.githubusercontent.com/80622859/216763942-d0dd0c73-8825-48b9-b63d-3eb522c7b735.png)

![image](https://user-images.githubusercontent.com/80622859/216763945-2f691be9-511b-42ce-af55-5a6579a17575.png)

1. CNN을 통해 뽑아낸 feature map을 입력으로 받음(feature map의 크기는 H x W x C)
2. Feature map에 3 x 3 합성곱층을 256 또는 512 channels 만큼 수행(Intermediate layer). Padding은 1로 설정하여서 H x W가 보존도록
- 수행 결과 : H x W x 512 or H x W x 256
3. 1 x 1 합성곱층을 이용하여서 분류기와 bbox regression 입력으로 넣어줌(size에 상관없이 동작 가능)
4. 분류를 수행하기 위해 1 x 1 합성곱층을 2 x 9 channel 수 만큼 진행
- H x W x 18 size
- Reshape을 수행한 후 softmax를 적용하여 object일 확률을 계산
5. Bounding box regression 예측 값을 얻기 위한 1 x 1 합성곱층을 4 x 9 만큼 수행
6. RoI 계산
- 분류를 통해 얻은 물체일 확률 값들을 정렬한 다음, 높은 순으로 K개의 anchor box만 추려냄
- K개의 anchor box에 각각 bbox regression을 적용
- 비 최대 억제를 적용하여 RoI 구함

- 위의 과정을 얻은 RoI를 첫 번째 feature map에 투영하고 RoI pooling을 적용

# Loss function

![image](https://user-images.githubusercontent.com/80622859/216764168-fa695e63-6762-4604-ba23-f8f45feb8b80.png)

- 분류와 bbox regression에서 사용된 손실 두 가지를 더해줌
- i는 하나의 anchor, $p_i$ : 해당 anchor가 객체일 확률, $t_i$ : bbox regression을 통해서 얻은 box 조정 값 vector
- $p_i ^*, t_i ^*$ : ground truth
- Fast R-CNN과 똑같은 손실 함수

# Trainging 

1. ImageNet pretrained model을 불러온 다음, RPN 학습
2. 학습시킨 RPN에서 기본 합성곱 신경망을 제외한 region proposal layer만 활용하여 Fast RCNN을 학습
3. RPN과 Fast RCNN을 합친 후, RPN에 해당하는 층들만 미세 조정
4. Fast R-CNN에 해당하는 층들만 미세 조정
