# Semantic Image Segmentation with Deep Convolutional Nets and Fully connected CRFs

# 1. Introduction

- Deep Convolutional Nerual Networks(DCNNs)는 분류, 객체 탐지 등의 전반적인 CV 분야에서 좋은 영향
- 하지만 segmentation에서는 성능이 좋지 않았음
- DCNN을 

- Semantic segmentation에서 높은 성능을 내기 위해서는 합성곱 신경망의 마지막에 존재하는 한 pixel이 입력값에서 어느 크기의 영역을 cover할 수 있는지에 대한 receptive field 크기가 중요하게 작용
- Pooling을 dilated convolution으로 parameter의 수를 유지하며 해상도가 줄어드는 것을 막음
- 기존 합성곱과 동일한 양의 parameter와 계산량을 유지하면서도, field of view(한 pixel이 볼 수 있는 영역)를 크게 가져감
- 
