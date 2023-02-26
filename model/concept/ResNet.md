# Residual Network

- Facebook
- 기존 20 계층 수준의 신경망을 152 계층까지 늘이는 성과
- Human performance를 뛰어넘는 모형

## 구조

![image](https://user-images.githubusercontent.com/80622859/221402608-953e0416-8eed-48a0-b594-e31f0675b21c.png)

- Skip-Connection

## Skip Connection

![image](https://user-images.githubusercontent.com/80622859/221402624-4fe55459-2ab0-4f2c-99bd-df58065cffe9.png)

- Feature를 추출하기 전 후를 더함

## Identity Mapping

![image](https://user-images.githubusercontent.com/80622859/221402714-30b0be5f-dd04-4195-832f-9d73bd64a4be.png)

- 한 단위 feature map을 추출하고 난 후 활성 함수를 적용하는 것이 상식
- 개선된 구조에서는 identity mapping을 얻기 위해 pre-activation을 제안

### Pre-Activation

![image](https://user-images.githubusercontent.com/80622859/221402774-e96e013d-2fe2-416d-9a79-050bceed0602.png)

- Conv-BN-ReLU 구조를 BN-ReLU-Conv 구조로 변경
- Gradient highway가 형성되어 극적인 효과
