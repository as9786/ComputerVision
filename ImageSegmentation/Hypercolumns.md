# Hypercolumns for Object Segmentation and Fine-grained Localization

## Abstract

- 합성곱 신경망의 마지막 층은 너무 coarse해서 정확한 영역을 잡기 힘듦
- 한편에, 앞 쪽 신경망은 지역은 잘 잡지만 의미적인 부분을 잘 잡지 못함
- 두 개의 특징을 모두 포착하기 위해, 한 pixel의 hypercolumn을 그 pixel 위에 있는 모든 합성곱 신경망 단위의 activation vector로 정의
- Hypercolumn을 pixel descriptor로 사용. 세 가지의 fine-grained localization 작업
- Simultaneous detection, segmentation, part labeling

## 1. 서론
- 합성곱 신경망의 마지막 층은 우리가 알고자 하는 객체의 가장 많은 정보를 지니고 있다고 알려져 있음
- 하지만 항상 그 층이 최적의 표현이 아닐 수도 있음
- 

- 
