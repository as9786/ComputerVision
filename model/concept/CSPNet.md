# CSPNet : A New Backbone that can Enhance Learning Capability of CNN

## 초록
- Computing power가 낮은 환경에서도 모형을 돌릴 수 있게 연산량 완화
- 연산량이 많아지는 이유는 신경망이 최적화되는 과정에서 경사의 중복 때문

## 서론
- 신경망이 깊어질수록 효과가 더 강해짐.
- 그러나 구조의 확장은 연산량을 많아지게 함
- 경량화도 중요
- 기본 층에서 두 개의 단계로 나눈 다음 마지막 cross-stage에서 합치는 기법 사용

## 방법

### Cross Stage Partial Network
- DenseNet
- 이전 층들의 값이 연결되어 합성곱을 통해 가중치와 출력이 만들어짐

![image](https://github.com/user-attachments/assets/1f0a5bed-3332-49d0-8928-fc43ecb5f200)

- 역전파 식

![image](https://github.com/user-attachments/assets/a0731786-4dbc-49b0-a674-44bc3efae2eb)

- f : Optimizer, w : 가중치, g : 경사
- 역전파와 순전파 과정에서 많은 경사 정보가 재사용
- 복사된 경사 정보를 반복적으로 학습

![image](https://github.com/user-attachments/assets/75f69f2f-3b44-4780-aaf4-ada98abb3f20)

- DenseNet의 출력값 연결을 통한 재사용을 유지하면서도, 경사 정보가 많아지는 것을 방지

### Exact Fusion Model
- EFM은 FoV(Field of View)를 적절하게 포착하여 one-stage detection 강화

![image](https://github.com/user-attachments/assets/9f8fa0b1-e2cf-459e-81af-9974d345c07b)







