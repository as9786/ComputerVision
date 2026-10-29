# Adding Conditional Control to Text-to-Image Diffusion Models

## 서론
- 작업별 사용 가능한 data size는 text-to-image domain만큼 크지 않음
- 이를 위해 과적합을 피하고 대형 모형의 일반화 능력을 보존하기 위한 방법이 필요
- 허용 가능한 시간과 memory 공간 내에서 특정 작업에 대해 대형 모형을 빠르게 최적화하는 방법이 중요(미세 조정, 전이 학습 등)
- ControlNet : 작업별 입력 조건을 학습하기 위해 확산 모형을 제어하는 구조
- 확산 모형의 가중치를 학습가능한 복사(trainable copy)와 locked copy로 복제
    - Locked copy : 신경망 능력을 보존
    - Trainable copy : 작업별 dataset에서 학습되어 조건부 제어

## 방법

<img width="1269" height="544" alt="image" src="https://github.com/user-attachments/assets/3b17fa2a-d90a-42f1-936c-aed1ee105f7b" />

- 신경망의 입력 조건을 조작하여 전반적인 동작을 추가로 제어
- Network block : 신경망을 구축하기 위해 자주 사용되는 단위. 층의 집합. Ex) ResNet block, attention block
- 모든 가중치를 $\theta$로 잠근 다음 $\theta_c$에 복제
- $\theta_c$는 외부 조건 vector c로 학습
- $\theta$ : Locked copy, $\theta_c$ : Trainable copy
- 복사를 하는 이유는 dataset size가 작을 때 과적합을 방지하고, 대형 모형의 성능을 유지하기 위함
- Zero convolution layer : 가중치와 편향이 0으로 초기화된 1x1 합성곱 층
- 첫 번째 학습 단계에서는 trainable copy와 locked copy의 모든 입력과 출력은 같음

### ControlNet in Image Diffusion Model
- Stable diffusion은 U-Net 구조

<img width="1150" height="997" alt="image" src="https://github.com/user-attachments/assets/ef158518-7b03-4dfe-85ff-373c550cbf49" />

- U-Net에 각 단계를 제어


