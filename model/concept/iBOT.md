# iBOT : Image BERT pre-training with online tokenizer

## 1. 초록
- BERT에서는 [MASK]된 토큰을 복원하는 학습을 하여 모형이 문맥을 이해
- 영상에서도 똑같이 하자 => Masked Image Modeling(MIM)
- 하지만 영상 patch에는 semantic token이 존재하지 않음 -> Online tokenizer : 선생 모형 자체를 visual tokenizer로 사용
- 선생 모형은 고정되어 있지 않음. 학생 모형의 EMA로 계속 최신화됨.
- 별도의 tokenizer를 사전 학습할 필요가 없음

## 2. 서론
- 자연어 처리에서는 MLM이 잘 됨
- 기존 Vision SSL(Self-Supervised Learning)에서는 global image representation에 집중(Ex. DINO)
- 히지만 검출 분야에서는 지역 표현도 중요

## 3. iBOT

<img width="797" height="287" alt="image" src="https://github.com/user-attachments/assets/3172568a-d44d-411c-a1ed-390498d9a450" />

- Tokenizer = Teacher
- 영상에서 두 view를 만듦. 선생 모형에는 원본, 학생 모형에는 masked view를 넣음
- 두 가지 손실을 계산. $L = L_{cls} + L_{MIM}$

### 3-1. CLS Self-Distillation
- Cross-View
- 선생 모형과 학생 모형의 서로 다른 view로 손실 계산
- View가 달라져도 영상의 의미적 동일성은 유지되어야 하기 때문
### 3-2. MIM Loss
- 학생 모형이 선생 모형을 따라감
- $L_{MIM} = -\sum_{i} m_i P^{patch}_{\theta '} (u_i)^T log P^{patch}_{\theta} (\hat {u_i})$
- 


