# Scene Text Recognition with Permuted Autoregressive Sequence Models

## 초록

- Context-Aware STR 방법은 전통적으로 자기 회귀 모형을 사용
- 자기 회귀 모형은 two-stage 방법을 사용. 외부 언어 모형을 사용
- 외부 언어 모형의 조건부 독립은 정확한 예측을 잘못할 수 있음
- PARSeq는 permutation language modeling을 사용하여 공유하는 가중치를 활용해 내부 자기 회귀 언어 모형의 ensemble을 학습
- 이는 context-free-non-AR과 context-aware AR inference를 단일화
- 그리고 양방향 문맥을 반복적으로 조정
- Attention 덕분에 임의의 방향의 글자에도 견고 
