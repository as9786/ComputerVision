# Difference of Gaussians

## 1. 개념
- 서로 다른 표준편차를 가진 두 개의 gaussian kernel로 영상을 각각 smoothing 한 뒤, 두 결과의 차이를 구하는 연산

$$DoG(x,y)=I(x,y) \ast G(x,y,\sigma_1) - I(x,y) \ast G(x,y,\sigma_2)$$

- 
