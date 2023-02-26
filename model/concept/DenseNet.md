# Densely Connected ConvNets

![image](https://user-images.githubusercontent.com/80622859/221403070-6b354129-2b37-4a9c-91a7-4ea4e495bb9c.png)

- ResNet의 idea 계승
- Dense한 connection을 추가

## 구조

![image](https://user-images.githubusercontent.com/80622859/221403105-c9279207-1342-471e-ab73-18e6358a519b.png)

- Dense block
- Pre-Activation 구조

## Dense block

![image](https://user-images.githubusercontent.com/80622859/221403222-b56fb132-5d31-407a-bdc2-1278d1e0db31.png)

- 이전 feature map에 누적해서 이어 붙이는 결과와 같음

## Bottleneck 구조

![image](https://user-images.githubusercontent.com/80622859/221403256-3a3d596b-4dfc-42f6-9cc2-41ed7f81f922.png)

- 1 x 1 Conv를 이용한 bottleneck layer

![image](https://user-images.githubusercontent.com/80622859/221403298-327e11de-4d3d-41b5-a42b-aa89f836248a.png)

