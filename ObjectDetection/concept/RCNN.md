# Rich featue hierarchies for accurate object detection and semantic segmentation

## Abstract

- mAP(mean Average Precision) : 객체 탐지의 성능을 측정하는 지표
1. 객체 탐지를 위한 영역 제안(region proposal)에 합성곱 신경망 적용
2. 사전 훈련과 미세 조정을 적용해서 train data가 적은 상황에서도 성능을 올림
- 영역 제안과 합성곱 신경망을 결합 => R-CNN(Regions with CNN)
- 영역 제안 : Image 안에서 객체가 있을 만한 후보 영역을 먼저 찾아주는 방법. ex) 선택적 탐색(Selective Search)

## 1. Introduction

- 두 단계(2-stage) 절차를 갖는 구조화된 모형(2-stage detector)
1. 객체 분류(classification)
2. 경계 박스 추정(Bounding-box regression)
- 경계 박스(Bouding-box,bbox) : 객체 위를 표시하는 사각형 box  
- 분류 + 회귀
- 두 가지 문제
1. 합성곱 신경망으로 object localization(객체 위치를 찾는 일)
2. Annotation된 data가 부족한 상태에서 모형을 학습해야 하는 문제

### 1. CNN으로 object localization하는 문제

- 객체 탐지는 객체를 분류하는 일뿐만 아니라 객체의 위치 좌표까지를 찾아야 함
- Object localization을 위한 세 가지 접근
1. Localization은 일종의 회귀 문제 => 실효성이 떨어짐
2. Sliding-Window Detector 사용 => 합성곱 신경망을 사용하기 때문에 window와 strdie의 크기가 커지게 되는데 이는 localization을 오히려 어렵게 함
3. 영역 제안(Region proposals) => 객체 탐지와 분할에서 모두 효과
- 영역 제안 절차

![image](https://user-images.githubusercontent.com/80622859/216748762-8cc4b053-6a39-4660-8ca4-bdf269c7d42d.png)
