# Scalable Diffusion Models with Transformers(DiT)

## 1. 서론
- 생성 모형에서는 transformer는 채택율이 낮음
### 1-1. DDPM
- 초기에 pixel-level의 자기 회귀 모형과 조건부 생산적 적대 모형에서 성공을 본 U-Net은 개선되어 PixelCNN++에서 상속됨.
- 본 논문은 U-Net inductive bias가 확산 모형의 성능에 중요하지 않으며, transformer로 대체될 수 있음을 보임

## 2. Related work 

### 2-1. Classifier-Free guidance
- Conditional diffusion model은 class label c와 같은 추가 정보를 입력으로 사용. 이 경우 reverse process는 $p_{\theta}(x_{t-1}|x_t, c)$가 되며, 여기서 $\epsilon_{\theta}$와 $\sum_{\theta}$는 c로 조건화됨
- 위 설정에서 classifier-free guidance를 사용하여 표본 추출 절차가 log p(c|x)가 높은 x를 찾도록 장려할 수 있음
- 베이즈 정리에 따라

<img width="377" height="42" alt="image" src="https://github.com/user-attachments/assets/0f1b0aab-90cd-414c-a776-d383d8521902" />

<img width="471" height="41" alt="image" src="https://github.com/user-attachments/assets/7fa90cb6-173f-4fdc-88ac-6178ca4c1181" />

- 확산 모형의 출력을 점수 함수로 해석하면 DDPM sampling process는 다음과 같이 p(x|c)가 높은 표본 x로 유도 가능

<img width="502" height="80" alt="image" src="https://github.com/user-attachments/assets/2fe94bee-3a72-41a6-be4c-9c9912a832e4" />

- 일반 표본 추출 기술에 비해 상당히 개선된 표본을 생성 => DiT에도 적용

### 2-2. Latent diffusion models(LDM)
- 고해상도 pixel space에서 직접 확산 모형을 학습하는 것은 계산적으로 불가
- LDM은 2 단계 접근 방법으로 해결
1. Trained encoder E를 사용하여 영상을 더 작은 공간의 표현으로 압축하는 auto encoder 학습
2. 영상 x의 확산 모형 대신 표현 z=E(x)의 확산 모형 학습(E는 고정)
- 확산 모형에서 표현 z를 표본 추출하고 학습된 decoder x = D(z)를 사용하여 새 영상을 생성

## 3. Diffusion Transformer

<img width="1614" height="682" alt="image" src="https://github.com/user-attachments/assets/78107fcc-fc2c-4376-badc-0f6391634c52" />

### 3-1. Patchify
- Dit input은 공간적 표현 x (256x256x3 사진의 경우 z는 32x32x4)
- 입력에 각 patch를 선형으로 삽입하여 입력을 차원 d의 T개의 token sequence로 변환
- 그 후, positional embedding

### 3-2. DiT block
- 
