# LayoutLMv3 : Pre-training for Document AI with Unified Text and Image Masking

## 서론

### 기존 기술의 한계

#### 1. Text modality
- BERT의 MLM 사용
- 양방향 표현 학습

#### 2. Image modality
- DocFormer
    - CNN decoder로 image pixel 재구성
    - Noise가 있는 세부 사항 학습 경향
    - 고수준 구조 파악 한계
- SelfDoc
    - Masking area 특징 회귀
    - 이산 특징 분류보다 학습이 어려움
 
### LayoutLMv3의 혁신점
- 통합된 접근 방식
- Text와 image masking 목표 통합(MLM & MIM)
- Image patch 직접 활용
- 합성곱 신경망 없이 iamge embedding 구현(합성곱 신경망 의존성 제거)
- Parameter efficiency
- 영역 주석 불필요
- 간단

## LayoutLMv3
- 
