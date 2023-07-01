# BEIT V2: Masked Image Modeling with Vector-Quantized Visual Tokenizers

## Abstract 

- MIM은 손상된 image patch를 복구하여 자체 지도 표현 학습에서 인상적인 결과
- 하지만 기존 연구는 낮은 수준의 image pixel에서 작동 => 높은 수준에서의 활용 X
- Vector quntization knowledge distilation 
- 개별 image patch를 연결하여 전역적인 의미 표현을 향상 시키는 patch aggregation strategy


## Introduction

- Language modeling은 풍부한 의미 표현을 학습하지만, BEiT의 경우에는 그렇지 못함

![image](https://github.com/as9786/ComputerVision/assets/80622859/0cd2b68b-b503-4a28-b6c3-1e509d9a81a0)

- 의미 공간을 이산화하기 위해 VQ-KD 도입
- VQ-KD encoder는 먼저 학습 가능한 codebook에 따라 input image를 개별 token으로 변환
- Decoder는 개별 token을 조건으로 교사 모형에 의해 encoding된 semantic feature를 재구성하는 방법을 배움
- [CLS] token이 모든 patch를 연결하도록 patch aggregation 사용
- MIM이 전역 특징을 제대로 학습하지 못하는 문제 해결

- 학습된 image representation의 범위를 향상
- 이는 작업에서의 성능을 향상
- VQ-KD를 통하여 반지도 표현 학습을 masked image modeling을 pixel 수준에서 의미론적 수준으로 촉진
- 개별 의미 token이 주어진 전역 구조를 적용하고 학습된 표현의 성능 향상시키는 patch aggregation


## Methodology

- Masking image modeling framework 상속
- Visual tokenizer를 사용하여 각 image를 개별 visual token set으로 변환
- Masked visual token을 복구
- VQ-KD

![image](https://github.com/as9786/ComputerVision/assets/80622859/8608de4b-bc98-4295-af81-3e06bfaaca4f)

### Image Representation

- ViT backbone
- 224 x 224 image는 14 x 14 image patch grid로 분할.  각 patch 16 x 16 크기
- Image patch는 평탄화 작업을 거친 후 transformer input embedding에 들어감으로써 선형 변환

### Training Visual Tokenizer

- Visual tokenizer는 image를 일련의 visual token, code에 사상
- Tokenizer는 vision transformer encoder와 quantizer로 구성
- Tokenizer는 먼저 input image를 vector로 encoding
- Vector quantizer는 각 patch representation $h_i$에 대해 codebook에서 가장 가까운 이웃을 찾음
- i 번째 image patch의 양자화된 code는 다음과 같음

![image](https://github.com/as9786/ComputerVision/assets/80622859/50494ee6-304d-46b3-8251-eda8a0ce6ddf)

- j와 L-2 정규화는 codebook 조회에 사용
- 위의 거리는 cosine similarity 
- Codebook embedding을 decoder에 전달
- Decoder는 mulit-layer transformer
- Output vector는 CLIP과 같이 교사 모형의 특징을 가짐(재구성)
- Decoder output $o_i$와 정답인 $t_i$의 유사성을 최대화
- 양자화 식은 미분이 불가능. 경사는 decoder input에서 encoder output으로 복사
- Quanitizer는 encoder output에 대해 가장 가까운 code를 찾고, codebook embedding의 경사는 encoder에 대한 최적 값을 찾음

![image](https://github.com/as9786/ComputerVision/assets/80622859/fa3f9c53-0378-43e9-989b-32deb000e422)

### Improving codebook utilization

- Codebook의 극히 일부만 사용하게 됨
- VQ-KD

![image](https://github.com/as9786/ComputerVision/assets/80622859/97820e25-1c9e-418e-913e-06b53cdb4c1b)

- Embedding dimension을 32 차원으로 줄이면서 가장 가까운 code를 찾기 위해 L-2 distance 사용
- 저차원 codebook embedding은 decoder에 공급되기 전에 고차원 공간에 사상
- Codebook embedding을 최신화하기 위해 지수 이동 평균 사용 => 더 안정적

## Pretraining BEIT V2

- MIM 설정에 따라 ViT를 사전 학습
- Input image x가 주어지면 약 40%가 block으로 masking
- M : Masking position
- 학습 가능한 embedding $e_{[M]}$을 사용하여 원래 image patch embedding을 $e_i$로 대체
- 학습 가능한 [CLS] token을 image patch embedding과 함께 입력에 추가하여 ViT에 공급
- MIM head를 단순한 FCL로 설계, 손성된 정보를 기반으로 masking position의 visual token을 예측
- Softmax로 분류

![image](https://github.com/as9786/ComputerVision/assets/80622859/dafdc52f-6351-4f74-b7a9-ae47bed46780)

### Pretraining global representation

- Global image representation을 위해 [CLS] token을 사전 훈련
- Patch 수준의 사전 훈련과 image 수준의 표현 집계 간 불일치 완화
- 마지막 층의 [CLS] token을 사전 학습하기 위해 중간 층의 patch vector와 연결 
- 그 후 연결된 vector들을 두 개의 transformer block decoder에 공급하여 다시 MIM
- Parameter는 두 MIM head에 대해 공유
- 새로 추가된 decoder는 사전 훈련 때만 사용

## Experiments

### Pretraining Setup

#### Visual tokenizer training

- Code size : K = 8192, D = 32
