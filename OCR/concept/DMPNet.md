# Deep Matching Prior Network: Toward Tighter Multi-oriented Text Detection

## 초록

- 그 동안은 직사각형의 경계 상자만을 사용
- 그래서 이를 해결하기 위해 좀 더 문자에 적합한 사각형을 사용
- Sliding window 방식이 아닌 quadrilateral sliding window 사용

## 1. 서론

- 촬영된 사진의 품질은 문자를 탐지하는데 큰 영향을 끼침
- 여러 뱡향의 문자 인식이 중요함
- 직사각형 기반의 경계 상자 문제점
1. 중복된 정보 발생
2. 주변 문자의 인식 문제
3. 비 최대 억제를 사용할 때, 불필요한 중복이 정답을 제거

- DMPNet -> Tighter text detection
- 대략적으로 문자를 예측하고 이를 조정
1. 문자의 본질적인 형태에 대한 사전 지식을 바탕으로, 특정 중간 합성곱 계층에서 다양한 종류의 사각형 sliding window를 설계하여, 미리 정의된 임계값과 겹치는 영역을 비교함으로써 대략적으로 문자를 예측(Sliding window와 정답 영역 참조 사이의 수많은 다각형 중첩 영역이 계산되어야 하기 때문에 이를 해결하기 위해 Monte-Carlo 방법 사용)
2. 그 후에 많이 겹치는 sliding window를 조정.
- 새로운 smooth Ln loss 더 나은 회귀를 제공(L2와 smoothing L1 loss보다 뛰어남)
- 
