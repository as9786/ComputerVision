# Image as a Foreign Language: BEIT Pretraining for All Vision and Vision-Language Tasks

## Abstract 

- Language, vision and multi-modal fusion
- 범용적
- Multi-modal based 
- Image-text 쌍을 MLM으로 통일

![image](https://github.com/as9786/ComputerVision/assets/80622859/a2dc39a0-18d6-46dc-97aa-d057f5c23c38)

![image](https://github.com/as9786/ComputerVision/assets/80622859/c2cda52c-143d-4787-9bfe-a878fe6461fb)

## Introduction: The Big Convergence

- Massive data에 대한 대규모 사전 학습을 수행함으로써 모형을 다양한 downstream task에 쉽게 전송 가능
- Masking data modeling은 다양한 양식에 성공적으로 적용
- Image를 text처럼 처리
- 모형 크기와 data size를 확장하면 기초 모형의 일반화 품질이 보편적으로 향상
- 모형 크기를 수십억 개의 가중치를 사용
- 접근 가능한 data resource만 사용
- Scale up은 대규모 언어 모형 사전 훈련을 위해 개발된 pipleline을 직접 재사용 가능 => Image를 외국어로 처리
- Image, text, image-text 쌍에 대해 masking data modeling
- 입력 형식 또는 출력 형식에 관계없이 다양한 작업에 대해 용도를 변경 가능
- 사전 훈련과 미세 조정을 위해 얻기 쉬운 data만을 사용함에도 불구하고 성능이 좋음

![image](https://github.com/as9786/ComputerVision/assets/80622859/8062070c-4cf6-4b79-b308-bbc0e27e7f5e)

## BEIT-3: A General-Purpose Multimodal Foundation Model

- Shared multi way transformer network 사용. Mono-modal and multi-modal data에 대한 masking data modeling

### Backbone Network : Multiway Transformers

- 다양한 양식을 encoding 하기 위해 backbone model로 multi way transformer
- Shared self-attention module과 서로 다른 양식에 사용되는 FFN로 구성
- 양식에 따라 각 input token을 전문가에 전달
- 각 계층에는 vision expert와 언어 전문가가 포함
- 상위 3개의 계층에는 fusion encoder를 위해 설계된 vision language expert가 있음

![image](https://github.com/as9786/ComputerVision/assets/80622859/f254b72e-7935-41f5-9b6d-45bc45c05198)

- Monomodal(Image, text) 와 multimodal(image-text)에 대한 unified mask data modeling
- 사전 훈련 중에는 text token or iamge patch의 일부 비율을 무작위로 masking -> Masked tokenㅇ르 복구
- Unifed mask 후 예측 작업은 표현을 학습할 뿐만 아니라 다른 양식의 정렬도 학습
- Text data는 sentencepiece tokenizer 사용
- Image data는 BEIT v2의 tokenize 사용(discrete visual token)
- Image-text 쌍에서는 monomodal text 15% token과 text token 50%를 무작위로 masking
- Image의 경우에는 BEIT에서와 같이 block masking strategy 사용(Image patch의 40% masking)
- 하나의 사전 훈련 작업만 사용 => 훈련 과정을 쉽게 확장
- 훨씬 작은 사전 훈련 배치 크기로 학습

![image](https://github.com/as9786/ComputerVision/assets/80622859/5e2f7ac7-abdf-41e6-8c79-8f399c27d2ac)

### Scaling up: BEIT-3 Pretraining

#### Backbone Network

- hidden size : 1408, intermediate size : 6144, num_head = 16, num of transformer block : 40
- 모든 계층에는 vision expert와 언어 전문가 포함
- Vision language expert는 상위 3개의 multiway transformer layer에 사용
- Self attention은 서로 다른 양식에서 공유
- 1.9B parameters

#### Pretraining Data

- 
