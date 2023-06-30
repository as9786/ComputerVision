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
- 
