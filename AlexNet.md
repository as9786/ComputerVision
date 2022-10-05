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
- 5개의 합성곱층과 3개의 완전연결층 = 총 8개의 층

### 3.1 ReLU Nonlinearity
- 경사하강법 관점에서 기존의 포화 비선형 함수(ex tanh)는 비포화 비선형성 함수인 max(0,x)보다 느림
- ReLU를 사용하는 깊은 CNN은 tanh를 사용하는 것보다 몇 배는 빠름

![캡처](https://user-images.githubusercontent.com/80622859/194093170-3a2268a8-2f4e-4792-ab15-e224d0807b81.PNG)

### 3.2 Training on Multiple GPUs
- Network를 2개의 GPU에 나눔
- 최신 GPU들은 다른 GPU의 memory에서 직접 읽고 쓸 수 있기 때문에 병렬 처리에 적합
- Node를 절반으로 나누어 각 GPU에 넣어 병렬 처리
- 하나의 트릭 : GPU가 특정 계층에만 통신 ex) 3층의 kernel은 2층의 모든 kernel들의 입력을 받지만, 4층의 kernel은 같은 kernel map의 3층 kernel에서만 입력을 받음

![캡처](https://user-images.githubusercontent.com/80622859/194093943-249ce214-e4c8-4e86-99a2-0d99acb473d6.PNG)

- 연결 패턴을 선택하는 것은 교차 선택의 문제지만, 계산량이 허용하는 부분까지 통신량을 정밀하게 조정 가능

### 3.3 Local Response Normalization
- ReLU는 포화 상태를 방지하기 위해 입력 정규화가 필요 X
- 하지만 국소 정규화 계획은 일반화에 도움 X
- 특정 filter의 한 pixel의 가중치가 높으면 영향을 받은 feature map은 자연스럽게 그 수치가 높아짐 => filter 정규화
- 첫 번째, 두 번째 합성곱의 결과에 ReLU 수행(response normalization)
- 특정 계층에서 ReLU 비선형성을 적용한 후 이 정규화를 적용

### 3.4 Overlapping Pooling
- 기존의 pooling layer는 중복된 이웃의 정보를 저장 X
- s = z가 아닌 s<z를 사용(z : pooling size, s : stride) => overlapping pooling
- 일반적으로 overlapping pooling을 한 것이 과적합 방지에 도움

### 3.5 Overall Architecture

![캡처](https://user-images.githubusercontent.com/80622859/194097887-e62fd463-63f4-42e0-a867-1e9dcdd6ab17.PNG)

- 8개의 층(5개의 합성곱층 + 3개의 완전연결층)
- 마지막 완전연결층은 softmax 함수 적용
- 2, 4, 5층의 합성곱은 동일한 GPU 내의 이전 계층에 kernel map에만 연결
- 3층의 합성곱층은 2층의 모든 kernel map에 연결
- 반응 정규화는 1, 2 합성곱층 뒤에 있음
- Max pooling layer는 다섯 번째 합성곱층과 반응 정규화층 이후에 존재
- ReLU 함수는 모든 합성곱 및 완전연결 계층의 출력에 적용
- 첫 번째 합성곱층 : 224x224x3 입력을 받아 11x11x3 크기의 96개의 kernel을 4 pixel의 보폭으로 움직여 filtering
- 두 번째 합성곱층 : 5x5x48의 256 kernel로 filtering
- 세 번째 합성곱층 : 두 번째 합성곱층들의 출력을 받아 3x3x256의 384 kernel 적용
- 네 번째 합성곱층 : 3x3x192 크기의 384개의 kernel을 가짐
- 다섯 번째 합성곱층 : 3x3x192 크기의 256 kernel을 가짐
- 3,4,5 합성곱층 : 어떠한 pooling이나 표준화 층 없이 연결

![1_bD_DMBtKwveuzIkQTwjKQQ](https://user-images.githubusercontent.com/80622859/194098903-3ba6f37b-2c2d-414d-ad20-3e793b4fc054.png)

## 4. Reducing Overfitting
- 6천만 개의 매개 변수
- 과적합 없이 학습하는 것은 힘듦

### 4.1 Data Augmentation
- 과적합을 방지하기 위해 dataset을 인위적으로 확장
- 원본 image에서 생산할 수 있는 방식
1. Image 변환과 수평 반사
- 256x256 image에 무작위로 224x224 patch와 이들의 수평 반사를 추출해 학습에 사용
- 훈련 설정의 크기를 2048배 증가
2. RGB 채널의 강도를변경
- ImageNet dataset 전체에 RGB pixel 값 집합에 대한 PCA 수행
- 평균이 0이고, 표준편차가 0.1인 가우시안 분포에서 얻은 무작위 변수와 PCA 결과를 곱해 각 image에 추가

### 4.2 Dropout
- 은닉층의 출력을 0.5 확률로 영점화
- Test에는 모든 신경망을 사용하지만 출력에 0.5를 곱합(지수적으로 많은 dropout network에 의해 생성된 예측 분포의 기하학적 평균을 내는데 합리적인 근사치)
- 처음 두 개의 완전연결층에서 dropout 사용

## 5. Details of learning
- Batch size = 127, momentum = 0.9, weight decay = 0.0005
- 적은 양의 weight decay가 model의 학습에 중요 => 정규화뿐만 아니라 model의 오류를 감소
- 표준 편차가 0.01인 제로 가우시안 분포에서 각 계층의 가중치를 초기화
- 두 번째, 네 번째, 다섯 번째 합성곱층과 완전연결층에서 뉴런 편향을 상수 1로 초기화 => ReLU에 양의 입력을 제공해 학습 초기 단계 가속화
- 상수 0으로 나머지 층에서 뉴런 편향 초기화
