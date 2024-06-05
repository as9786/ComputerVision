# Transformer-based Optical Character Recognition with Pre-trained Models

## 소개

- Transformer를 OCR에 접목
- 글자 탐지는 글자 영상 내의 모든 text block을 word level 또는 text line level에서 localization하는 것이 목표
- 경계 상자를 잘 찾아야 함
- 글자 탐지는 일반적으로 기존 객체 탐지 모형으로 적용할 수 있음
- 하지만 인식은 글자 내용을 이해하고 시각적 신호를 natural language token으로 전사하는 것이 목표
- 글자 인식 작업은 일반적으로 영상 이해를 위해 합성곱 신경망 기반의 encoder와 글자 생성을 위한 순환 신경망 기반 decoder를 활용하는 encoder-decoder framework

## 모형

![image](https://github.com/as9786/ComputerVision/assets/80622859/cd8b124d-ca98-46dc-bb1e-61806081feaf)

- 사전 훈련된 CV & NLP model을 사용한 글자 인식을 위한 end-to-end transformer based OCR model
- CNN을 backbone으로 사용하지 않음. 단순하지만 효과적
- ViT를 따라 입력 영상을 384 x 384 크기로 조정하고, 해당 영상은 16 x 16 patch sequence로 분할되어 입력으로 사용
- Self attention은 encoder와 decoder에서 활용되며, 입력 영상에서 인식된 글자로서 wordpiece 단위가 생성
- 
