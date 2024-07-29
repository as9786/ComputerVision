# Model Agnostic Meta-Learning for Fast Adaptation of Deep Networks review

## 1. 서론

- Model Agnostic : 모형에 상관없이 적용 가능(경사하강법을 사용하는 모든 모형에 사용 가능)
- Fast adaptation : 새로운 작업을 빠르게 학습할 수 있음(Meta learning 핵심 개념)
- 여러 작업에 대해서 적합한 모형을 학습하면 세부적인 작업시 미세 조정 과정이 빠를 것이라는 생각에 기반
- Optimization-based 

## 2. Model Agnostic Meta-Learning
- 모형과 상관없이 대부분의 인공지능 모형에 적용 가능

![image](https://github.com/user-attachments/assets/a17ac7b2-076f-4fc6-8e15-403cf663b8c4)

- 일반화된 모형의 parameter $\theta$를 찾아나가는 방식으로 경사하강법 진행
- $\theta$가 작업 1, 2, 3에 대한 최적은 아니지만, 이후 task 1, 2, 3를 빠르게 찾아나갈 수 있는 지점. Meta parameter $\theta$가 위의 화살표를 가리키는 점으로 가게 됨
- $\theta$에서 new task $T_i$에 맞는 최적의 model parameter $\theta^*$를 찾아가는 방식으로 경사 하강법 진행

![image](https://github.com/user-attachments/assets/f4710075-5168-4f66-9755-4812d4148b9b)


