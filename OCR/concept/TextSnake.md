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


