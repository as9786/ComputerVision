# GradCAM

- 기존 합성곱 신경망 모형 구조의 변화가 없음
- GAP 없이 두 개의 전결합 계층 존재
- 기존 합성곱 신경망 모형의 재학습이 필요 없음
- Feature map에 곱해줄 가중치를 미분을 통해 계산

![image](https://github.com/as9786/ComputerVision/assets/80622859/c0167a5f-e35d-4b14-8029-f6d126a13d1f)

- class c에 대한 점수 $y^c$를 각 원소로 미분
- 해당 미분값은 각 feature map의 원소가 특정 class에 주는 영향력
- 각 feature map에 포함된 모든 원소의 미분값을 더하여 neuron importance weight를 구함. 해당 값은 feature map이 특정 class에 주는 영향력

![image](https://github.com/as9786/ComputerVision/assets/80622859/f0c2c155-f184-4816-9dcc-28e1d2b17175)

- a와 각 k개의 feature map을 곱하여 weight sum of feature map 계산
- ReLU를 취하여 최종 Grad-CAM에 의한 heatmap이 출력
- ReLU를 취해주는 이유는 오직 관심 있는 class에 긍정적인 영향을 주는 feature에만 관심이 있기 때문

![image](https://github.com/as9786/ComputerVision/assets/80622859/e4be36f6-8cbd-411b-8ef3-3f005789e958)


