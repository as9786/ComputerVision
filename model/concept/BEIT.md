# BERT Pre-Training of Image Transformers

## Abstract

- BERT를 ViT에 적용
- 각 image는 사전 훈련에서 image patch와 시각적 토큰의 두 가지 보기를 가짐
- 원본 image를 visual token으로 tokenize
- Image patch를 무작위 masking하여 Vit에 전달
- 사전 학습 목표는 손상된 image patch를 기반으로 원본 시각적 token을 복구

## 1. Introduction

- 경험적으로 transformer model 기반은 합성곱 신경망보다 더 많은 train data 필요
- Data 부족 문제를 해결 하기 위해 자체 학습한 사전 학습은 대규모 image data를 활용할 수 있는 유망한 해결책
- ViT를 사전 학습하기 위해 denoising auto encoding idea를 전환
- Image data에 BERT style의 사전 학습을 직접 적용하는 것은 어려움
- ViT는 입력 단위, 즉 image patcgh에 대한 사전 어휘가 없음
- 단순히 softmax 분류기를 사용하여 masked patch의 가능한 모든 후보를 예측할 수 없음
- 단어와 BPE와 같은 언어 어휘는 잘 정의되고 있고, autoencoding 예측을 용이하겧 ㅏㅁ
- 간단한 대안은 작업을 masked patch의 pixel을 예측하는 회귀 작업으로 간주
- Image transformer의 양방향 encoder representation을 나타내는 준지도 학습
- 사전 학습 작업인 MIM(Masked Image Modeling)
- MIM은 각 image에 대해 두 개의 보기, 즉 image patch 및 시각적 token을 사용
- 
