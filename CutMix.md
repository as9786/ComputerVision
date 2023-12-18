# CutMix : Regularization Strategy to Train Strong Classifiers with Localizable Features

- Cutout, mixup과 같은 여러 사진을 합치거나 사진의 부분을 제거하여 학습하는 방식들은 모형의 일반화에서 조금 더 좋은 성능을 내게 함

![image](https://github.com/as9786/ComputerVision/assets/80622859/4e289b30-ae03-43be-8da2-350248842502)

## 초록

- Image data에서  부분적으로 정보를 dropout하는 방법들은 합성곱 신경망의 정확성 향상에 기여
- 하지만 이와 같은 방법들은 train image의 손실을 야기 => 모형 학습 과정에서 비효율적이거나 바람직하지 못함
- CutMix는 train image의 부분들을 합쳐서 하나의 image data로 만드는 방법 -> 만들어진 data label은 합쳐진 data의 선택 확률들로 구성

## 서론
- 합성곱 신경망의 과적합을 방지하기 위해서 입력 사진에 대해서 임의로 특징을 제거하는  정규화 방법들 제시
- Generalization and localization
- 그 동안의 방법들은 지워진 부분을 0으로 채워 넣거나 random noise로 채워넣었는데 이는 훈련 사진의 pixel 정보의 비율을 줄이게 됨
- 합성곱 신경망 기반 모형을 학습할 때는 보통 dataset이 부족하기 때문에 개념적 한계
- CutMix는 사진의 pixel 정보를 제거하기보다 제거된 부분에 다른 사진의 부분을 가져와 대체
- 위와 같이 만들어진 data label은 가져온 pixel의 비율만큼 구성
- 모형의 학습 과정 도중 data가 없는 경우가 없게 되고 이는 학습의 효율성을 증대시키면서 dropout 효과도 가져옴
- 추가된 부분은 모형의 인식 능력을 더욱 더 향상시키고 이는 모형 학습 및 추론 과정에서 기존의 방식들과 같은 연산량
- Mixup은 자연스럽지 않음
- Mixup은 분류에서는 좋은 성능을 내지만 다른 작업에서는 약함
- CutMix는 다양한 작업에 대해서 좋은 성능

## CutMix

![image](https://github.com/as9786/ComputerVision/assets/80622859/13d139bd-91b6-4060-9817-a8eb61beebf2)

- $x_1$을 $x_2$에 합침
- 합쳐진 data는 선택된 pixel의 비율만큼 label을 구성

![image](https://github.com/as9786/ComputerVision/assets/80622859/82262aa8-bf72-4b0e-9987-c576f699021c)

- 두 개의 사진을 선택
- 균일분포 (0,1)에서 $\lambda$를 추출
- $\lambda$는 부분 영역과 전체 영역의 비율을 조정하는 parameter

![image](https://github.com/as9786/ComputerVision/assets/80622859/5921a0df-5ee6-4af2-8a08-d8f98614d397)

- 사진의 부분을 선택하기 위해서 $r_x$와 $r_y$는 (0, W), (0, H)에서 추출
- 계산된 부분 영역은 제거되고 제거된 부분에 다른 사진에서 영역이 선택되어 채워지게 됨. $\lambda$를 활용해서 label 값을 생성

![image](https://github.com/as9786/ComputerVision/assets/80622859/0b5913f2-a16c-4fc5-b63e-69b06f6ad672)



