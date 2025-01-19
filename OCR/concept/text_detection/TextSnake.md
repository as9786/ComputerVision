# A Flexible Representation for Detecting Text of Arbitrary Shapes

## 요약

- 그 동안의 STR(Scene Text Recognition)은 경계 상자와 같은 정형화된 방식 사용.
- 실제로 표현되는 곡선, 자유로운 형식을 처리할 때 한계가 있음
- 수평, 방향 및 곡선 형태를 탐지하는 모형 필요
- TextSnake는 기하학적 속성을 예측(FCN module)

## 소개

- 정밀도, 재현율, F1-score는 영상에서 물체를 찾아냈는지의 여부는 확인할 수 있으나, 물체의 위치를 정확하게 판단함에 있어서는 모호함
- 경계 상자 내에서 물체의 비중은 천차만별

![image](https://github.com/as9786/ComputerVision/assets/80622859/16e96169-997e-4853-ba0f-9210a38eefdb)

- (a)는 일반적인 경계 상자. Text의 비중은 절반이고, 나머지는 text 영역이 아님
- (b)의 경우에는 경계 상자를 기울이며 영역을 높임. 그럼에도 상자의 영역을 벗어나는 부분 존재
- (c)도 영역의 비중이 높지 않음
- (d)는 문자 영역에 최대한 비중을 두어 글자 외의 배경을 최소화

## 방법

### 표현

![image](https://github.com/as9786/ComputerVision/assets/80622859/1ffd9532-98dc-4f82-a50e-2ffa5e5c3038)

- Disk로 영상을 탐지
- 글자 중심을 기준으로 disk의 위치 c, 반지름 r, tangent 방향 $\theta$ 값으로 영상 내에서 글자를 표시

### Pipeline 

![image](https://github.com/as9786/ComputerVision/assets/80622859/09d9a663-4141-405d-a46c-75adaa14d1a8)

- 규칙적이지 않은 글자 모양을 감지하기 위해, 저자들은 FCN 모형을 사용하여 글자 instance 위치를 예측
- FCN 기반의 신경망은 글자 중심선(text center line)과 글자 위치(text regions)의 score map을 예측
- Instance segmentation을 수행할 때, 글자 중심선이 겹치지 않도록 분리하는 작업(disjoint set)을 수행
- Striding algorithm은 중심축의 point list를 추출하고 text instance reconstruction 작업을 수행하여 그림에서 문자들을 모두 인식할 수 있도록 함

### 신경망 구조

![image](https://github.com/as9786/ComputerVision/assets/80622859/cd884a2e-9f1d-45f7-9b91-1b8bf9007cfe)

- FPN과 U-Net의 구조를 참조
- 하나의 영상을 여러 개의 크기로 나누어 작은 크기에서는 전체적인 관점, 큰 크기에서는 좀 더 세부적인 관점에서 글자를 감지

 ### 추론

 - 모형의 출력으로 글자의 중심선과 글자 위치
 - Disjoint-Set을 사용하여 글자 중심선을 서로 다른 text instance로 분리
 - Striding algorithm을 통해 text area 내 점들을 추출하고 이 점들을 통해 text instance의 영역을 재구성하여 글자의 중심점 data 수집



#### Striding algorithm

![image](https://github.com/as9786/ComputerVision/assets/80622859/95345d20-1eb5-4878-a4d9-e0ed8ba711cf)

![image](https://github.com/as9786/ComputerVision/assets/80622859/d0af439e-ab09-4ea5-8ac1-d7e6bfc45075)

1. 사진에서 문자를 분할한 부분에서 임의의 pixel을 하나 선택한 후 글자영역의 중심점을 찾음(해당 점은 글자 중심선의 일부)
2. 중심점 주변으로 두 개의 점을 찍어 뻗어 나감. 새롭게 찍은 두 개의 점 또한 해당 위치에서 글자 영역의 중심점을 설정(글자 영역 바깥일 경우 제외)
3. 중심점으로부터 원을 그리면서 글자 영역 표시

### Label generation

- 오각형 이상의 모양에서는 글자 영역을 모두 표시하는 것이 어려움
- 뱀 모양의 text instance를 찾는 algorithm 제안

![image](https://github.com/as9786/ComputerVision/assets/80622859/cec175df-24c5-44d2-98c3-65b8796e2e6f)

- 다각형의 글자 범위 내에서 뱀의 머리와 꼬리 역할을 하는 부분을 찾아낸 다음, text instance의 중심점을 계산한 다음, 중심점에서부터 원을 그려나감으로서 글자의 label 생성

### 학습

- $L = L_{cls} + L_{reg}$
- $L_{cls} = \lambda_1 L_{tr} + 2\lambda  L_{tcl}$ -> 글자 중심선과 글자 영역의 분류 오차
- $L_{reg} = \lambda_3 L_r + \lambda_4 L_{sin} + \lambda_5 L_{cos}$ -> r, sin, cos의 회귀 오차

![image](https://github.com/as9786/ComputerVision/assets/80622859/b352a39f-f93b-4349-88d6-dbbe8d6c07b0)


- 

