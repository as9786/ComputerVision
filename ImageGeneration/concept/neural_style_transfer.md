# Neural style transfer

<img width="1176" height="1000" alt="image" src="https://github.com/user-attachments/assets/11b97e20-73d9-4d88-a240-4bde144d5684" />

<img width="1183" height="668" alt="image" src="https://github.com/user-attachments/assets/a516cd39-b8ae-4ee2-9e83-6761ec747a98" />

- 신경망을 이용한 style transfer
- Content image와 style image가 있을 때, 신경망을 통해 content image에 style image의 style을 입힌 사진을 생성하는 것
- 합성곱 신경망의 얕은 층과 깊은 층의 특성을 파악해야 함

## 합성곱 신경망

<img width="1000" height="1161" alt="image" src="https://github.com/user-attachments/assets/b9671e93-74fb-4017-b401-4191f3dfaa73" />

- 얕은 층 : 경계선이나 색상 같은 저수준 특징
- 깊은 층 : 위치, 자세 등 고수준 특징
- 신경망 층이 깊어질수록 더 복잡한 특징들을 잡음

## 비용 함수
- $J(G)=\alpha J_{content}(C,G)+ \beta J_{style}(S,G)$
- G : 생성된 사진, C : Content image, S : Style image, $\alpha$, $\beta$ : Weighting factor
- $\frac{\alpha}{\beta}=10^{-3}$ or $10^{-4}$로 설정
- 사진을 생성하는 방법
  1. G 초기화
  2. 경사하강법을 통해 J(G) 최소화
- 
