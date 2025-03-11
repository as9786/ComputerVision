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

### 입력 구성 

- Text-image multi-modal transformer를 사용하여 교차 양식 표현을 학습
- 입력 :  Text embedding sequence, image embedding sequence
- Text embedding은 RoBERTa
- Positional embedding
    - 1D : Text sequence 내 token index
    - 2D layout : Text의 경계 상자 좌표
    - Segment level layout position
- Image embedding은 linear projection 사용
1. 문서를 H x W로 조정
2. P x P 크기의 균일한 patch로 분할
3. Patch를 D 차원으로 선형 투영
4. Vector sequence로 평탄화($L=HW/P^2$)

### 사전 학습 목표
- MLM : Text token의 30% masking
- Span masking($\lambda=3&)
- $L_{MLM}(\theta)=-\sum{log p_{\theta}(y_l|X_{M'},Y_{L'})$ 

