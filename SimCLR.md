# 서론

- Generative learning and proxy task

## Generative learning

![image](https://github.com/as9786/ComputerVision/assets/80622859/a62f9343-a759-43aa-a8db-d2ae3d7724af)

- Auto encoder와 같이 encoder-decoder 구성되어 있는 모형을 자가 지도 학습하는 것이 generative learning
- Encoder와 decoder를 학습해야 하기 때문에 계산 비용이 큼
- Image classification의 경우 decoder 필요 없음

## Proxy task

- Decoder X, 미리 사용자가 정답을 만듦
- 사용자가 만든 정답이 고차원적인 정보를 만드는데 도움이 되는지 확실치 않음

### Exempler
- 영상이 50만 장 있다면, 각각의 영상을 하나의 정답으로 생각해서 총 50 만개의 정답을 만듦
- 각 영상마다 증강을 하여 하나의 집단을 원본 영상의 정답에 할당

### Jigsaw puzzle
- Patch들을 서로 섞어서 순서를 맞춤
- Pretext task. Puzzle을 풀면서 학습한 모형이 영상 분류나 객체 탐지에 좋음
- 사람이 직접 정답을 만들어야 함이 문제
- 학습된 모형이 기존의 영상보다 고차원적인 정보를 갖는지 의문

## 자가 지도 학습(Self-Supervised learning)
- Pretext task : 자가 지도 학습을 하기 위해서 사용자가 만든 문제
- Downstream task : 자가 지도 학습을 적용해서 풀 문제

![image](https://github.com/as9786/ComputerVision/assets/80622859/14e94447-01cf-41b8-9147-d9a5e2bb2e5e)

1. 자가 지도 학습은 정답이 없는 dataset을 가지고 학습을 진행(Pretext task)
- 각 영상에 대한 정답을 사용자가 임의로 생성
- 출력은 embedding 형태. 실제 영상과 출력 간의 유사도 계산
2. 자가 지도 학습을 통해 학습한 모형을 기존의 모형에 적용하여 평가(Downstream task)
- 선형 평가(Linear evaluation), 준지도 학습(semi-supervised learning), 전이 학습
- 선형 평가 : Pretext task를 통해서 학습한 모형의 가중치를 고정 후 전결합 계층을 붙여서 미세 조정
- 준지도 학습 : Dataset label을 1%~10% 사이만 이용해서 학습
- 전이 학습 : 다른 dataset에 적용

# 방법

![image](https://github.com/as9786/ComputerVision/assets/80622859/45fdd8da-6096-4166-8ff8-9d4940dd9d7b)

1. X라는 dataset을 각각 2번 증강하여 $x_i, x_j$를 얻음
2. $x_i, x_j$에 모형 적용
3. Projection head 적용

![image](https://github.com/as9786/ComputerVision/assets/80622859/12a4bf6f-6fca-4d2e-b645-3fe19d4dfe39)

4. Projection head에서 나온 embedding 값을 InfoNCE(대조 손실, contrastive loss)를 이용하여 서로의 유사도를 계산후 손실 계산
- 분자는 긍정 표본(postive sample)에 대한 서로의 유사도, 분모는 긍정 표본 + 부정 표본(negative sample)에 대한 유사도의 총합을 이용해서 확률 계산
- 실제 code에서는 cross entropy 사용(cross entropy에 유사도 대입)
- 

