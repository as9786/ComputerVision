# Swin2SR: SwinV2 Transformer for Compressed Image Super-Resolution and Restoration

## Abstract

- 압축은 매우 중요한 역할
- 하지만 압축은 어느 정도의 손실을 초래하게 됨
- 이와 같은 문제를 해결하기 위한 영상 복원 작업은 현재 좋은 성능을 보이고 있음
- 크기 문제, resolution gaps between pre-training and fine-tuning, hunger on data 문제 해결

## Introduction

- 영상 복원 기술은 높은 품질의 깨끗한 영상을 낮은 품질의 영상으로부터 재구성하는 것이 목표
- 합성곱 신경망은 단일 영상에 대해서 해당 문제를 해결
- 전통적인 방식보다 deep learning based method가 더 좋은 성능을 보임
- 하지만 합성곱 신경망 기반은 문제가 있음
- Transformer는 전역 정보를 포착하면서 몇몇 vision problems에서 괄목할만한 성과를 보임
- 
