# 자가 정규화 신경망(Self-Normalizing Neural Network)

![image](https://user-images.githubusercontent.com/80622859/229462120-b282d409-8ed4-4bbb-b17e-c1525e509e64.png)

- CNN에 약간의 변화를 줌으로써, 스스로 정규화하는 계층을 형성
- Batch noramlization 대비 훨씬 더 안정적이면서도 좋은 성능을 보임

## SELU(Scaled Exponential Linear Unit)

- 음수 값은 exponential하게 활성화
- $\lambda$와 $\alpha$의 값에 따라 특성이 결정
- 자가 정규화를 위한 값 

