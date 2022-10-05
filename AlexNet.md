# ImageNet Classification with Deep Convolutional Neural Networks

# 1. Introduction
- 객체 탐지를 위해서는 많은 dataset, 더 강력한 model 그리고 과적합을 피하기 위한 발달된 기법이 필요
- 최근까지 dataset의 경우 수 만개의 image로 상대적으로 적은 수
- 위와 같은 dataset들은 간단한 인식 작업을 사용할 수 있지만, 실제 dataset은 변수가 많기 때문에 이들을 인식하기 위해서는 더 큰 dataset 필요
- LabelMe, ImageNet과 같은 방대한 datasets 제공
- 강력한 GPU 등장하면서 CNN을 image에 사용하는 것 가능
- 5개의 합성곱층과 3개의 완전연결층을 포함

## 2. The Dataset
- ImageNet은 약 22,000개의 label에 1,500만 개 이상의 고해상도 image dataset
- ImageNet은 해상도가 고정되어 있지 않음
- 하지만 model은 일정한 입력 크기를 요구 -> 256 x 256의 해상도로 고정
- 직사각형이 주어질 경우 짦은 면의 길이를 256이 되도록 image의 scale을 조정한 후 중앙을 기준으로 256 x 256이 되도록 사진을 자름
- 이외의 전처리 작업을 하지는 않았지만, 학습 set의 각 pixel에서 평균 값을 빼주는 방법으로 RGB pixcel을 학습

## 3. The Atchitecures
- 5개의 합성곱층과 3개의 완전연결층 = 총 9개의 층

### 3.1 ReLU Nonlinearity
- 경사하강법 관점에서 기존의 포화 비선형 함수(ex tanh)는 비포화 비선형성 함수인 max(0,x)보다 느림
- ReLU를 사용하는 깊은 CNN은 tanh를 사용하는 것보다 몇 배는 빠름

![캡처](https://user-images.githubusercontent.com/80622859/194093170-3a2268a8-2f4e-4792-ab15-e224d0807b81.PNG)

### 3.2 Training on Multiple GPUs
- Network를 2개의 GPU에 나눔
- 최신 GPU들은 다른 GPU의 memory에서 직접 읽고 쓸 수 있기 때문에 병렬 처리에 적합
