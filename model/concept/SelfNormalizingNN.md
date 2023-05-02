# 자가 정규화 신경망(Self-Normalizing Neural Network)

![image](https://user-images.githubusercontent.com/80622859/229462120-b282d409-8ed4-4bbb-b17e-c1525e509e64.png)

- CNN에 약간의 변화를 줌으로써, 스스로 정규화하는 계층을 형성
- Batch noramlization 대비 훨씬 더 안정적이면서도 좋은 성능을 보임

## SELU(Scaled Exponential Linear Unit)

![image](https://user-images.githubusercontent.com/80622859/235625907-fcc86fbe-73e1-4ab7-8c05-8818043c8578.png)

- 음수 값은 exponential하게 활성화
- $\lambda$와 $\alpha$의 값에 따라 특성이 결정
- 자가 정규화를 위한 값 : $\lambda = 1.0507, \, \alpha = 1.67326$ 

## $\alpha$-Dropout

![image](https://user-images.githubusercontent.com/80622859/235626725-8f781ad9-9c61-4c64-9570-0c6ad42e70e5.png)

- Dropout은 ReLU에 잘 동작. SELU에 적합하도록 변형 버전
- 복잡한 미분을 통해 $\alpha^{'}$ 값을 결정. Dropout rate = 5~10%(비교적 작음)

- 아직 DL에서도 세심한 수학적 연구가 직관을 뛰어넘을 수 있다는 것을 보여줌



