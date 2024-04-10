# CAM(Class Activation Map)

- 합성곱 신경망의 마지막 층을 전결합 계층으로 바꿀 때, pixel들의 위치 정보를 잃게 됨
- 분류 정확도가 높더라고 해당 모형이 무엇을 보고 결과를 내렸는지 확인하기 어려움
- Learning Deep Features for Discriminative Localization
- 전결합 계층 대신에 GAP(Global Average Pooling)을 적용하면 특정 class image의 heat map을 생성
- 해당 heatmap을 통해 모형이 어떤 이유로 결정을 내렸는지 이해 가능

![image](https://github.com/as9786/ComputerVision/assets/80622859/8b1d8c4e-3b17-4035-890b-90446d40dd5d)

## GAP

- 각각의 feature map 마다 GAP 적용
- 그 결과 GAP layer로 들어오는 feature map의 channel 수와 동일한 길이의 vector를 얻게 됨
- GAP에서 산출된 vector를 입력으로 사용

![image](https://github.com/as9786/ComputerVision/assets/80622859/6ba73560-98a6-4aa8-92c0-cc2b19fbfeb1)

- 위의 그림에서는 6차원 vector가 입력
- 6개의 범주 중 하나를 예측
- 가중치는 학습을 통해서 계산
- 가중치 1부터 가중치 6까지를 각 feature map에 곱한 뒤 각 pixel 별로 더해주어 최종 heatmap 출력

- 단순하지만 그럴 듯한 결과를 보임
- 마지막 합성곱 층을 통과한 feature map은 입력 사진의 전체 내용을 함축하기 때문
- 중간에 존재하는 feature map에 대해서는 CAM을 통해 heatmap을 추출할 수 없음

