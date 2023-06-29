# ONE-PEACE: EXPLOARING ONE GENERAL REPRESENTATION MODEL TOWARD UNLIMITED MODALITIES

## Abstract

- Modality adapters, shared self-attention layers, modality FFNs로 구성
- Adapter와 FFN을 추가하여 새로운 modality를 쉽게 확장할 수 있음. Self-attention layers를 통해 multi-modal fusion이 가능
- Modal에 구애 받지 않는 cross-modal aligning contrast와 intra-modal denosing contras는 서로 다른 modality의 의미 공간을 정렬하고 modality 내에서 세밀한 detail을 포착 가능
- 무한한 modality로 확장할 수 있는 잠재력을 가지고 있음 
- 사전 학습된 computer vision 및 language를 사용하지 않고 좋은 성능

## Introduction
- 대량의 data로부터 학습한 representation model은 다양한 downstream task에서 강력한 일반화 능력을 보여줌
- Uni-modal representation model은 우수한 결과를 보여주지만 image-text, audio-text와 같이 multi-modal data를 효과적으로 활용하는데 어려움
- General representation model은 다음 조건을 충족해야 함
1. 모형 구조는 다양한 modality를 수용하고 multi-modality 간 상호 작용을 지원할 수 있을 만큼 유연해야 함
2. 사전 학습 방법은 각각의 modality에서 정보를 추출할 뿐만 아니라 modality 간에도 일치가 조정되어야 함
3. 사전 학습 방식은 일반적이고 간단해야 하며, 다양한 modality에 적용이 가능하여야 함

- 해당 모형은 여러 modality adapter와 modality fusion encoder로 구성
- 각 modality에서는 raw input을 feature sequence로 변환하는 adapter가 장착
- Modality fusion encoder는 transformer architecture의 feature sequence에서 작동
- 각 transformer block에는 shared self attention alyer와 multi modality FFN이 포함
- Self-attention layer는 attention mechanism을 통해 multi modal features 간의 상호 작용을 가능하게 함. Modality FFN은 modality 내에서 feature 추출을 용이하게 함
- 사전 훈련하기 위해 두 가지를 설계
1. Modal 간 대조 학습 => Modality 간 semantic space를 효과적으로 정렬
2. Modal 내 잡음 제거 대조 학습
- 위의 설계는 미세 조정 성능을 향상시킴과 동시에 cross modal retrieval 기능 유지
- 모든 modality에 보편적으로 적용이 되므로 개별 설계 불필요



## Related Work

### Vision-Language Pretraining

- 수많은 작업이 transformer를 사용하여 우수한 성능을 보임
- 사진과 언어의 대조 학습
- Encoder-decoder model을 사용하여 모든 vison-language 작업을 생성 작업으로 변환
- Multiway transformer를 사용하여 vision language data를 처리. Text token과 공동 학습을 위해 CLIP 사용 => Image token

  ### Audio-Language Pretraining
  - Audio-text joint pretraining

## Method

### Architecture

![image](https://github.com/as9786/ComputerVision/assets/80622859/8091cfcf-4370-4780-bd88-c533ce54af8f)

- 3 가지 modality adapter와 modality fusion encoder로 구성

#### Modality Adapters
- 서로 다른 raw input을 feature로 변환하기 위함
- 서로 상호 작용 X
- Transformer, 합성곱 신경망, 순환 신경망 등과 같이 adapter에 적합한 신경망을 유연하게 선택 가능

#### Vision Adapter(V-Adapter)
- 사진이 주어지면 계층적 MLP를 사용하여 patch size를 16 x16으로 점진적으로 증가시켜 image patching
- 서로 다른 patch 간에는 상호  작용 X
- $E^V = {e^V_{cls}, e^V_1,...,e^V_M}$

#### Audio Adapter(A-Adapter)

- Audio가 주어지면 sampling speed를 16kHz로 설정하고 raw audio wave를 표준화
- 정규화된 파형이 convolution feature extractor에 의해 처리되어 audio embedding 생성
- Relative positional embedding 사용
- $E^A = {e^A_{cls}, e^A_1,…,e^A_{N}}$

#### Language Adapter(L-Adapter)

- BPE
- 문장의 시작과 끝에 두 개의 special token 추가([CLS],[EOS])
- Absolute positional encoding
- $E^L = {e^L_{cls}, e^L_1,…,e^A_{K},e*L_{eos}}$

#### Modality Fusion Encoder

- Transformer architecture
- 각 transformer block에 shared self-attention layer와 세 가지 FFN 설정
- Shared self-attention은 서로 다른 modality 간 상호 작용을 가능하게 함
- FFN(V-FFN, A-FFN, L-FFN)은 각각의 modality 내에서 feature를 추가로 추출

#### Sub-LayerNorm
- Slef-attention layer와 FFN layer 전에 층 정규화 사용

#### GeGLU Activation Function
- FFM의 중간 차원은 embedding 차원의 4배

#### Relative Position Bias(RPB)
- Text와 audio에 대한 1D 상대 위치 편향. 사진에 대한 2D 상대 위치 편향
- 사전 훈련 단계에서 서로 다른 self-attention layer의 상대적 위치 편향이 공유
- 미세 조정 단계에서 각 self-attention layer의 상대적 위치 편향을 분리하고 사전 훈련된 상대 편향의 가중치를 상속 받음

#### LayerScale

- Residual block의 출력을 동적으로 조정
- 잔차에 추가하기 전에 각 계층의 출력을 학습 가능한 대각 행렬로 곱하여 값이 1e-6으로 초기화
- Sharing-separated는 다양한 modality의 작업을 처리하는 서로 다른 분기로 분해 가능

![image](https://github.com/as9786/ComputerVision/assets/80622859/591a5065-3ffb-4cde-a248-0b7ad80a785a)

![image](https://github.com/as9786/ComputerVision/assets/80622859/bc7d3ad5-11c5-45f0-b7e9-a2e449bad243)

- N : 배치 크기, i, j : 배치 내의 식별자, w : 학습 가능한 온도 매개 변수(0.07로 초기화),
- Cross mode contrastive loss는 모든 GPU 장치에서 negative feature를 수집하여 계산
- Cross mode contrastive loss를 각각 $L_{CL-VL}$과 $L_{AL-VL}$로 표시되는 image-text, audio-text 쌍에 적용

#### Intra-Modal Denosing Contrastive Learning
- Cross mode contrastive loss는 주로 서로 다른 modal 간의 특징을 정렬하는데 중점
- 하지만 위의 손실은 downstream task에서 최적의 성능을 발휘 X
- 이를 해결하기 위해 denosing contrastive learning 학습
- 미세한 mask feature와 그렇지 않은 사이에서 대조적 손실 계산
- Image patch, text token, audio wave feature
- Sequence 내 무작위 masking
- Unmasked unit만 modality fusion encoder에 입력
- Encoded unmasked features는 학습 가능한 masked token과 연결되어 masked feature를 생성하는 경량화된 transformer decoder에 입력

![image](https://github.com/as9786/ComputerVision/assets/80622859/2c86ebd2-10ec-46b9-a930-5aee5c099cc5)

### Training

![image](https://github.com/as9786/ComputerVision/assets/80622859/da3d1cef-6fb1-4b13-929b-224225153a80)

![image](https://github.com/as9786/ComputerVision/assets/80622859/a02e04a1-1378-428d-877b-3da342dd695e)

## Pretraining Detils

### Pretraining Datasets

- Image-text : LAION-2B
- Audio-text : Open source

### pretraining Settings
- 4B 매개변수를 가짐

![image](https://github.com/as9786/ComputerVision/assets/80622859/126249b9-50e8-44cc-bf60-83c5f59528dc)

