# Episode training

## 1. 개념

### 기존 방식

- 쥐, 소, 호랑이, 토끼, 용을 구분하는 사진 분류기를 만들고자 한다면 각 class 별 data가 100개라고 했을 때, 쥐, 소, 호랑이, 토끼, 용 각각 80개는 학습해 5-class classifier를 만듦
- 쥐, 소, 호랑이, 토끼, 용 각각 20개 testset으로 만든 후 성능 평가

### Episode

- 한 번에 모든 class를 활용하지 않음
- 작업 1 : {쥐, 소}
- 작업 2 : {호랑이, 토끼}
- 작업 3 : {토끼, 용}
- 분류기를 쪼갠 뒤, 완전히 새로운 data(뱀, 말, 양)으로 분류 성능 확인

## 2. 학습 방식

![image](https://github.com/user-attachments/assets/5e379477-7df5-4834-be0e-997fbccb1a03)

### 1) Train-Test data split
- Trainingset을 meta-train dataset, meta-test dataset으로 나눔
- Meta-test에 구성된 data class는 meta-train에 등장하지 않음

### 2) Task sampling
- Meta train dataset을 각 작업으로 쪼갬
- 전체 class 중 일부 class가 작업 1에 추출
- 여기서 각각의 작업을 episode라고 부름

### 3) Support Query dataset split
- 각 작업별로 data를 다시 support set(trainset), query set(testset)으로 분리

### 4) Task training
- 각각의 작업별로 학습을 진행하여 모형 생성

### 5) Meta test evaluation
- 생성된 모형에 meta-test의 support set으로 새로운 사진을 학습시키고, 최종적으로 meta-test query set을 분류

- 학습에 활용되지 않은 meta-test에서도 일부 meta-test support set으로 학습한 뒤, meta-test query data를 구분하는 것이 목표
