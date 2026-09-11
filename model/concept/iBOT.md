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
- 


