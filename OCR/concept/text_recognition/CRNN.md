# An End-to-End Trainable Neural Network for Image-based Sequence Recognition and Its Application to Scene Text Recognition

## 초록

- 특징 추출과 sequence modeling을 통합시키고 하나의 통일된 framework인 새로운 인공 신경망 구조 제안
- 4개의 구조
1. End-to-End train
2. 임의의 길이의 sequence data를 다룰 수 있음
3. 사전에 정의된 단어 사전에 갇혀 있지 않음
4. 실제 생활에서 보다 유용하게 사용되면서도 작은 모형을 효과적으로 생성

## 1. 서론
- Image based sequence recognition
- Sequence를 인식하는 것은 object label을 series로 예측해야 함
- 이는 sequence recognition 문제
- Sequence length가 다 다를 수 있음

### DCNN
- 고정된 차원에서 입력과 출력이 작동 -> 다양한 길이의 label sequence 생성할 수 없음

### RNN
- 입력 객체의 영상을 영상 특징의 sequence로 전처리해야 함

### CRNN
- DCNN + RNN
1. 문자와 같은 세부적인 annotation을 필요로 하지 않고, 단어와 같은 sequence label에서 직접적으로 학습
2. Image data에서 유의미한 특징을 직접 학습하는 DCNN과 같은 특성을 가지고, 사전 처리 단계를 필요로 하지 않음
3. Label sequence를 생성할 수 있는 순환 신경망 특징을 지님
4. Sequence length에 구속받지 않음. 학습과 시험 단계에서의 높이의 정규화만 필요
5. 단어 인식에서 더 좋거나 경쟁력 있는 성과 달성 가능

## 2. 제안하는 신경망 구조

### 합성곱 층
- 입력 영상에서 자동으로 feature sequence를 추출

### Recurrent layers
- 합성곱층에서 출력된 각각의 feature sequence의 각 frame에 대해 예측을 수행하기 위해 순환신경망 생성

### Transcription layer
- 순환 신경망에 의한 각 frame에 대한 예측을 label sequence로 변환

- CRNN은 다른 종류의 신경망 구조들의 결합을 통해서, 하나의 손실함수로 학습 가능

![image](https://github.com/user-attachments/assets/74bb9e07-8eb3-48f7-a646-a0fde4cc6c65)

### 2.1 Feature Sequence Extraction

- 기존 합성곱 신경망으로부터 합성곱층과 max pooling layer를 가져옴으로써 구성
- 전결합계층은 제거
- 해당 요소는 입력 사진으로부터 순차적인 특징 표현을 추출하기 위해 사용
- 모든 영상들은 같은 높이를 가지도록 조정되어져야 함
- 그 다음에 feature vector들의 sequence는 합성곱층으로부터 생성된 feature map으로부터 추출
- 각각의 feature sequence의 vector들은 feature map에서 왼쪽에서 오른쪽 방향으로 생성
- i 번째 feature vector는 모든 map의 i 번째 열들의 연결임을 의미
- 각 열의 넓이는 single pixel로 고정
- 합성곱층, max pooling, 활성화 함수는 변환될 수 없음
- 그러므로 각각의 feature map의 열은 원본 영상의 사각형 부분과 일치. 그러한 사각형은 각 feature map의 열과 일치
- Feature sequence 내의 각 vector는 수용 영역과 관련. 그 지역에 대한 영상 묘사자로 여겨짐

![image](https://github.com/user-attachments/assets/ae57c0b4-ff5e-4bcd-aab8-a3d61056ab6f)

### 2.2 Sequnce Labeling
- 양방향 순환신경망은 합성곱 층 다음에 위치
- Recurrent layers는 각각의 frame $X_t$에 대해 label인 $Y_t$를 예측
1. 순환 신경망은 문맥 정보를 포착하는 데 장점이 있음(문맥적인 단서를 사용하는 것이 독립적으로 다루는 것보다 좋음. 특정 문자들은 문맥과 함께 유추하는 것이 구별해내기 더 쉬움)
2. 순환 신경망은 오차 역전파를 사용할 수 있음 => 순환 신경망과 합성곱 신경망을 공동으로 학습 가능
3. 순환 신경망은 임의의 길이의 sequence에 대해 시작부터 끝까지 순회하면서 작동

![image](https://github.com/user-attachments/assets/b52519c5-f8b0-4e8e-b20e-ad8dc2848acc)

#### Vanilla RNN
- 입력층과 출력층 사이에 은닉층을 가짐
- Sequence가 길어지게 되면 경사 소실 문제 발생

#### LSTM
- Memory cell, input gate, output gate, forget gate로 구성
- 장기의존성 보존

#### Bidirectional LSTM
- LSTM은 방향성이 있고, 오직 과거의 문맥 사용
- Image sequence에서는 양방향성으로 나온 문맥이 훨씬 유용하고 상호 보완적

#### Transcription
- 순환 신경망으로부터 만들어진 frame 당 예측을 label sequence로 변환하는 과정
- Frame 당 예측이 가장 높은 확률과 함께 label sequence를 찾는 것
- 사전이 있는 lexicon-based transcriptions, 사전이 존재하지 않는 lexicon-free

