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

## 2. 제안 방법

![image](https://github.com/as9786/ComputerVision/assets/80622859/e83a7dce-6e00-4d41-86ce-a1f86bd6e736)

### 2.1 Roughly recall text with quadrilateral sliding window

- 다양한 사각형의 sliding winodw를 추가
- 겹치는 정도는 sldiing window가 긍정인지 아닌지를 판단
- 만약에 sliding winodw(SW)가 긍정일 경우, 문자의 위치를 찾기 위해 조정됨
- 작은 임계값은 많은 backgroud noise를 불러오고, 정밀도를 낮춤. 반면에 높을 경우, 문자 영역 추출을 하기가 힘듦
- Quadrilateral slding window를 사용할 경우, 높은 임계값을 가져도 정밀도와 재현율 모두 향상
- Background noise를 줄이고, 실제로 더 신뢰가 있으며, false positive를 제거

#### 2.1.1 Shared Monte-Carlo method

- 각각의 정답 영역에 대해서 모든 SW와 겹치는 정도를 계산해야 됨
- Monte-Carlo를 사용할 경우, 속도와 정확도 모두 좋아짐
1. 먼저 정답 영역에 주변에 1만 개의 좌표를 균일하게 표본추출. 정답 영역(SGT)은 전체 좌표 중 겹치는 좌표의 비율을 내접하는 직사각형 면적으로 곱해 계산.
2. 겹치는 부분이 없으면 계산 X. SW에도 똑같이 표본 추출을 통해 점들을 구하며, 정답 영역과 동일하게 면적 계산

![image](https://github.com/as9786/ComputerVision/assets/80622859/510c5ce3-7ad6-49cf-b815-514e59ef3760)

### 2.2 Finely localize text with quadrangle

- 4개의 좌표를 예측
- 4개의 좌표 순서를 정해주는 것이 중요
- 사각형이 아닌 다각형의 영역을 계산

#### Sequential protocol of coordinates

![image](https://github.com/as9786/ComputerVision/assets/80622859/e96ee9dd-1b58-47de-8d6f-a4d6976984fb)

- 먼저 최소값 x를 갖는 첫 번째 점을 결정. 두 점이 동시에 최소값 x를 가지면, 더 작은 값 y를 가진 점을 첫 번째 점으로.
- 둘째로 첫 번째 점과 나머지 세 점을 연결하고, 중간 기울기를 갖는 선에서 세 번째 점을 찾음.
- 두 번째, 네 번째 지점은 중간선의 반대편에 있다.
- 두 개의 좌표와 8개의 길이를 예측 $(x, y, w_1, h_1, w_2, h_2, w_3, h_3, w_4, h_4)$
- x,y는 중앙 좌표
- $w_i, h_i$는 i 번째 점에서의 상대적 위치

![image](https://github.com/as9786/ComputerVision/assets/80622859/1805e10b-5df1-4c62-a62e-82779677e681)



