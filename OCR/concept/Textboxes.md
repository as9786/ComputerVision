![image](https://github.com/as9786/ComputerVision/assets/80622859/d7c20189-f8e5-48e9-9f60-b27f9b976c8f)# Textboxes: A Fast Text Detector with a single Deep Neural Network(2016)

## 1. 서론

- Scene text는 일상 환경에서 많이 접할 수 있는 visual object
- 전통적인 광학 문자 인식은 너무 다양한 배경과 글자의 형태, 빛 상태에 따른 글자 상태 변화 등으로 인해 어려움을 겪음
- 글자/단어 후보 생성 -> 후보 filtering -> grouping 등 여러 단계로 나누어져 있어 학습이 오래 걸림. 실시간 적용이 어려움
- Textboxes는 SSD를 참조하여 만듦. 하나의 신경망이기 때문에 기존의 모형에 비해 현저히 빠른 성능을 보임. 정확도 또한 향상
- 모형 내부의 몇 가지 초매개변수들만 text detection에 맞도록 수정(기본 상자와 convolution kernel의 종횡비를 가로로 길게 늘림)
- 문자 기반 모형
- Textboxes -> CRNN


## 2. Detecting with Textboxes

### 2.1 Training phase
- 합성곱과 pooling으로만 이루어진 완전 합성곱 신경망

![image](https://github.com/as9786/ComputerVision/assets/80622859/75f5c58b-3d90-40f9-8a26-ce798bcacfa8)

- 연속적인 합성곱 층이 이루어진 부분을 base network
- Base network에서 중간중간 feature map을 가져오는 위치를 map point
- Map point에서 가져온 feature map들을 새로운 합성곱 연산을 수행해서 만들어낸 이 모형의 출력들을 textbox layer
- Textboxex의 출력은 하나의 값이 아닌 textbox layer가 됨

#### 종횡비 구성
- Text는 기본적으로 옆으로 긴 형태를 띄고 있기 때문에 기본 상자의 종횡비 또한 가로로 김
- 6가지 종횡비 사용(1,2,3,5,7,10). Pixel의 중심에 한 번, pixel의 아래에 한 번 적용하여 총 12개를 한 pixel의 기본 상자로 정함
- 중심에 모든 상자를 넣지 않고 살짝 아래로 내림으로써 촘촘한 탐지 가능

![image](https://github.com/as9786/ComputerVision/assets/80622859/f13ab115-5e7a-489b-8770-01121c967f3d)


