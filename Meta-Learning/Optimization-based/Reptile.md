# On First-Order Meta-Learning Algorithms
- 매우 간단한 meta-learning optimization algorithm
- 경사하강법을 통해서 meta-optimization 수행, 일반적인 경사하강법은 small dataset에 부적합할 수 있음
- 과정
1. Task Sampling
2. Multiple Gradient Descent step을 통해 task 학습
3. 새로운 paramter를 얻을 수 있게 model weight를 움직임

![캡처](https://user-images.githubusercontent.com/80622859/186355866-f6d53dd9-1f1e-411e-a421-ca4a9e7ef570.PNG)

- SGD는 inital parametet $\theta$를 가진 상태에서 loss 에 대한 k step 동안의 확률적 경사 하강법을 수행하고, output으로 final paramter vector를 내보냄. 
- 위와 같은 batch 형태는 매 반복마다 하나가 아닌 여러 task를 sampling 함
