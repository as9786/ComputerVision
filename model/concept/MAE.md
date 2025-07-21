# Masksed Autoencoders are Scalable Vision Learners

## 초록
- Masked patch를 복원하는 작업으로 학습한 사전 학습 가중치로 downstream task를 미세 조정
- BERT와 유사

## 서론
- 합성곱 신경망과 다르게 transformer는 self-attention module을 여러 block으로 쌓아서 표현력을 높임
- Self-attention은 위치 정보에 대해 불변하기 때문에 positional encoding을 입력에 더해주어 위치 정보를 부여
- Positional encoding을 사용하지 않게 되면, 각 patch를 임의로 뒤섞인 사진을 넣더라도 self-attention 결과는 원본과 동일

## MAE
- ViT 구조

## 1. 구조 및 학습 방법

<img width="1177" height="504" alt="image" src="https://github.com/user-attachments/assets/3a1cd1c5-393f-4847-86f9-84bc64ad0f6e" />

1. Input patch 중 일부를 날림
2. Poistional encoding을 입력에 더해주고, encoder로 보냄(Encoder : Self-attention based transformer encoder)
3. Encoder output에서 mask 씌운 위치에 대응되는 mask token을 붙임
4. Decoder 입력 전에 positional encoder를 한 번 더 더해주고, decoder를 거쳐 나온 출력을 unflatten
5. Decoder output(예측값)과 정답값 사이의 MSE loss 계산. 역전파 진행
6. Encoder를 활용하여 downstream task에 대하여 미세 조정

<img width="873" height="475" alt="image" src="https://github.com/user-attachments/assets/9cf644a5-fce9-45c3-8acf-d72050e450c4" />

- Masking 기법에 대해 3가지 실험(임의/덩어리/규칙적) 진행 결과, 임의로 하는 것이 성능이 가장 좋음
- Masking ratio=75%(BERT는 15%)
- 사전 학습 때, 사용하는 decoder design에 따라 미세조정 작업 성능이 다름
- 
