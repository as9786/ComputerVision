# BERT Pre-Training of Image Transformers

## Abstract

- BERT를 ViT에 적용
- 각 image는 사전 훈련에서 image patch와 시각적 토큰의 두 가지 보기를 가짐
- 원본 image를 visual token으로 tokenize
- Image patch를 무작위 masking하여 Vit에 전달
- 사전 학습 목표는 손상된 image patch를 기반으로 원본 시각적 token을 복구

## Introduction

- 경험적으로 transformer model 기반은 합성곱 신경망보다 더 많은 train data 필요
- Data 부족 문제를 해결 하기 위해 자체 학습한 사전 학습은 대규모 image data를 활용할 수 있는 유망한 해결책
- ViT를 사전 학습하기 위해 denoising auto encoding idea를 전환
- Image data에 BERT style의 사전 학습을 직접 적용하는 것은 어려움
- ViT는 입력 단위, 즉 image patcgh에 대한 사전 어휘가 없음
- 단순히 softmax 분류기를 사용하여 masked patch의 가능한 모든 후보를 예측할 수 없음
- 단어와 BPE와 같은 언어 어휘는 잘 정의되고 있고, autoencoding 예측을 용이하게 함
- 간단한 대안은 작업을 masked patch의 pixel을 예측하는 회귀 작업으로 간주
- 위와 같은 방법을 사용할 경우 short-range dependencies와 high-frequency detail만 학습 
- Image transformer의 양방향 encoder representation을 나타내는 준지도 학습
- 사전 학습 작업인 MIM(Masked Image Modeling)
- MIM은 각 image에 대해 두 개의 보기, 즉 image patch 및 시각적 token을 사용
- 사전학습된 DALL-E tokenizer를 이용해서 image patch들을 tokenizer 해서 위의 문제들을 해결

## Method

### Backbone/Image Patch

- 16 x 16 patch(ViT) (224 x 224 size)
- 개별 patch들을 평탄화 및 선형 변환 과정을 거치고 position embedding이 더해져서 최종 입력값이 됨
- Backbone network도 ViT 사용

### Visual Token

- Image의 경우에는 사전에 정의된 tokenizer가 없었기 때문에 image를 일정하게 token으로 만들 수 없음
- DALL-E에서 사용한 image tokenizer를 사용

![image](https://user-images.githubusercontent.com/80622859/231164192-2b474623-7093-4642-8020-221385414532.png)

- Image -> Discrete token sequence
- 위 그림에서 빨간 상자 안에 있는 부분이 DALL-E tokenizer
- DALL-E tokenizer를 통해 이미지를 descrete visual token으로 만들 수 있음

## Pre-Training
- Image patch의 40%에 masking
- Masking patches는  trainable embedding으로 교체한 뒤 masking 되지 않은 patch와 함께 ViT의 입력으로 들어감
- ViT의 최종 hidden vector들은 입력값의 encoded representation으로 취급하며, softmax classifier(MIM head)를 통과해 최종 출력을 얻음
- Masking 되었던 patch들의 최종 출력이 DALL-E를 통해서 미리 생성되었던 discrete token을 예측하도록 모형을 훈련(최대우도추정법)
- 자료 형태가 image인 것을 제외하면 BERT와 유사
- Masking selelction : Not randomly, blockwise
- 무작위로 block 크기를 정하고, block의 위치를 정하는 과정을 masked patch가 전체의 40%가 될 때까지 반복
- Image label은 전혀 사용하지 않았기 때문에 사전학습 과정은 온전히 비지도학습 방법론

## Fine-Tuning
- Image classification은 global average pooling을 사용해 최종 output vector를 모으고 선형 분류기를 통과 시킴

## Experiment


