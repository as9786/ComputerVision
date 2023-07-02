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

- 사진 : 2048, text : 2048, image-text : 2048개. 총 6144개
- Image augmentation : Zoom, crop, 수평 뒤집기, color jittering
- 64k 단어 크기의 sentencepiece
- Adamw($\beta_1 = 0.9, \beta_2 = 0.98, \epsilon = 1e-6$
- 가중치 감퇴 = 0.05

## Experiments on Vision and Vision-Language Tasks

![image](https://github.com/as9786/ComputerVision/assets/80622859/f5f9e6e0-b07a-435b-bb0d-8a6abcdc3352)

### Vision-Language Downstream tasks

#### Vision Question Answering(VQA)

- Input image에 대한 자연어 질문에 답
- VQA v2.0 dataset에 대해 미세 조정
- 주어진 질문과 image embedding을 연결한 다음 input embedding을 multi way transformer에 공급하여 image-question 쌍을 같이 encoding
- Final pooling output은 답변을 예측하기 위해 분류 층으로 공급

#### Visual Reasoning

- 영상과 자연어 설명에 대한 공동 추론을 수행하는 모형이 필요
- 한 쌍의 영상에 대한 text 설명이 사실인지 여부 결정

#### Image Captioning
- 주어진 영상에 대한 natural language caption을 생성
- Caption token의 일부 미율을 무작위 masking
- Image 단서와 caption context를 기반으로 token 복구
- 모형이 생성을 종료하는 방법을 학습할 수 있도록 special token [SEP] masking
- Cross-entropy loss
- Image는 bidirectional, 생성은 자동 회귀 방식

![image](https://github.com/as9786/ComputerVision/assets/80622859/acc7c083-36b4-4074-b5bb-bcef0fbc3e87)

#### Image-Text Retrieval

- Image와 text 간의 유사성을 측정
- Image : text, text : image 검색
- Dual encoder로 미세 조정
- Image와 text를 개별적으로 encoding
- 이러한 표현의 cosine similarity 계산
- Fusion encoder model 보다 효율적
- 가능한 모든 쌍을 공동으로 encoding할 필요 X

![image](https://github.com/as9786/ComputerVision/assets/80622859/1c005b2d-d2a7-43e8-9c44-f7349878baed)

### Vision Downstream Tasks

- ViT-giant와 parameter의 수 비슷

#### Object Detection and Instance Segmentation
- BEIT-3를 backbone으로 사용
- COCO dataset fine-tuning

#### Semantic Segmentation
- Image의 각 pixel에 대한 label을 예측
- ADE20K dataset
- ViT-Adapter의 task 방식을 따름
- Segmentation framework로 Mask2Form 사용

#### Image Classification

- ImageNet-1K dataset
- 작업은 image-text 검색 작업으로 공식화
- Category 이름을 image-text 쌍을 구성하는 text로 사용
- Class 이름의 feature embedding과 image의 feature embedding을 계산
- 가장 가능성이 높은 label을 예측하기 위해 cosine similarity 사용

![image](https://github.com/as9786/ComputerVision/assets/80622859/985fbb91-24cd-41c5-abc9-2a5759b15413)

## Conclusion

- 모든 양식에 대해 masked language model로 통일된 방식으로 수행
- Multi way transformer가 다양한 vision 및 vision language task를 효과적으로 modeling
