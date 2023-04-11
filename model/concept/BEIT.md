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
- 
