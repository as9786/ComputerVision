# Character Region Awareness for Text Detection

- Scene Text Detection(STD) 문제를 해결하기 위해 DL 사용

![image](https://github.com/as9786/ComputerVision/assets/80622859/1d3b1102-6713-493b-9f15-00de12753089)

- 모형의 목적은 입력으로 사용한 사진에 대해 pixel마다 영역 점수(region score)와 affinity score를 예측
- Region score : 해당 pixel이 문자의 중심일 확률
- Affinity score : 해당 pixel이 인접한 두 문자의 중심일 확률. 이 점수를 통해서 개별 문자가 하나의 단어로 그룹화될 것인지 결정

![image](https://github.com/as9786/ComputerVision/assets/80622859/5383b906-945a-4bf4-8706-0d0f7f286895)

- 각 pixel이 문자의 중심에 가까울수록 확률이 1에 가깝고, 문자 중심에서 멀수록 확률이 0에 가깝도록 예측
- 동시에 각 pixel이 인접한 문자의 중심에 가까울 확률(Affinity score) 예측

## 모형 구조

![image](https://github.com/as9786/ComputerVision/assets/80622859/1c078bf9-d25f-4f0a-a84c-5ac7cdac83a4)

- 완전 합성곱 신경망
- VGG-16 기반
- 배치 정규화 사용
- U-
