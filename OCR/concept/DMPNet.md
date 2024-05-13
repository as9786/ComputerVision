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
4. 
