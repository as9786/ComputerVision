# MixNet: Toward Accurate Detection of Challenging Scene Text Text in the Wild

## 서론
- 작은 글자를 검출하는 것은 불규칙한 위치, different style, 조명 조건 등 여러 가지 요인으로 인해 어려움 

## 모형
- 글자를 정확하게 검출하기 위해 CNN + Transformer의 장점을 결합한 MixNet
- Two core module
1. Feature Shuffle Network(FSNet)
    - Backbone of MixNet
    - Feature shuffling
    - 여러 크기 간의 특징(feature) 교환을 허용하여 고해상도, 고품질 특징을 생성
2. Central Transformer Block(CTBlock)
    - 글자 영역의 주요 축에 중점을 둠
    - 글자의 윤곽 또는 가장자리를 감지하는 방법보다, 작은 글자가 밀접하게 나타나는 어려운 상황에서 효과적
- MixNet architecture

![image](https://github.com/user-attachments/assets/98073091-25c7-4011-83b6-23e300f2d289)

- FSNet과 후처리를 통해서 글자 윤곽의 점들을 구함
- 해당 윤곽의 점들중 P개의 점들과 image sequence가 CTBlock의 입력으로 사용
- 첫 번째 transformer module은 sample point의 x와 y의 offset을 예측하고, 이들을 사용하여 글자 윤곽의 중심선을 생성
- 해당 중심선은 sampling되고, 대략적인 윤곽의 feature seqeunce와 결합된 다음, 두 번째 transformer module에 전송되어 더 정교한 글자 윤곽을 생성

### FSNet
- 많이 쓰이는 backbone인 ResNet과 VGG는 대체로 rough한 고해상도 특징을 생성. 이는 작은 글자 검출에 적합하지 않음
- 저해상도 특징이 noise에 더 강한 능력이 있음
- FSNet은 고해상도와 저해상도 특징 모두 교환하도록 설계
- 이로 인해 추출된 고해상도 특징이 noise에 덜 취약
- HRNet과 유사하지만, 특징을 섞는 과정에 핵심적인 차이가 있음
- HRNet은 층 간의 특징을 더하는 반면, FSNet은 각 해상도의 channel을 균등하고 나누고 섞음
- 섞은 후 각 해상도의 잘린 특징들은 동일한 크기로 upsampling or downsampling 후 새로운 특징으로 연결

![image](https://github.com/user-attachments/assets/851178cc-a867-4882-9787-7ba73ec18c9d)

- Convolution block : 특징 추출
- Down-sample block : Downsampling
- Shuffle layer : 각 해상도의 feature channel을 입력 수 N으로 나눔. 이 층에서의 연산은 여러 크기 간의 특징을 교환.
- 위 세 가지 module을 통해 다양한 크기의 글자들을 noise에 덜 민감하게 함 

### CTBlock

- 이전 연구에서는 text instance의 주변 sampling point를 활용
- 하지만 위와 같은 sampling point는 배경 특성을 포함하기 때문에, 글자에만 집중하는 것을 방해
- Encoder(세 개의 층으로 구성된 tranformer block)-Decoder(Simple MLP) transformer. 
- 각 block head에는 multi-head self attention과 MLP 포함
- Transformer의 장점으로 주변 특징과 중심선 특징의 조합을 통해 더욱 정확한 글자 윤곽을 생성
- 두 text instance가 가까이 위치하면, 인접한 영역의 윤곽 특징이 방해를 받을 수 있는데 중심선은 이를 분리해줌

