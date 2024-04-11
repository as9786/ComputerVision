# EAST : An Efficient and Accurate Scene Text Detector

## Basic of scene text detection

- 기본적인 text detection 목표는 글자가 위차한 경계 상자 좌표를 최대한 정확히 맞추는 것
- 회귀 문제로 접근
- 합성곱 신경망으로 사진의 특징을 추출 후, decoder로 단어 영역을 생성
- Pixel마다 단어 영역이 될만한 여러 후보를 만든 뒤 그 중에서 학습을 통해 RoI를 추려냄
- 글자와 글자, 단어와 단어 사이 여백 등을 모두 탐지하여 정해진 규칙에 따라 단어 영역으로 합치는 algorithm도 존재

## Basic concept

- 기존 text detection model들이 3~5 차례 convolution block을 사용한 것과 달리 하나의 합성곱층을 사용 => 연산 시간 향상
- FCN을 활용해 단어가 포함된 rotated rectangle 또는 quadrilateral box를 에측(회전 또는 다각형 모형)
- 
