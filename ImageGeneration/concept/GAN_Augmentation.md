# GAN Augmentation: Augmenting Training Data using Generative Adversarial Networks

## GAN augmentation
- Progressive Growing of GANs(PGGAN)을 기반으로 학습
- Image data 내에서 필요한 특성(pertinent variance)과 필요하지 않은 특성(non-pertinent variance)이 존재
- 필요하지 않은 특성이 많이 존재하면, 필요한 특성을 찾는 데 어려움을 주고 과적합 위험성이 올라감
- 불필요한 특성을 제거하기 위해서 data distribution을 단순화(intensity normalization, registration to a standard space 등)와 증강 기법을 사용
- GAN은 기존의 증강 기법과 다르게 직접 조정해야하는 특징들에 대한 필요성을 줄여줌

### 학습 방법
1. 사용하려는 dataset에서 k개 사진을 추출하여 PGGAN 학습
2. PGGAN을 사용하여 k개의 합성 사진 생성(같은 사진을 생성하지 않기 위해 gaussian noise 추가)
3. 생성된 합성 사진으로부터 일부를 무작위로 추출하여 기존 dataset에 합침
4. 최종적으로 생성된 training data로부터 학습

![image](https://github.com/user-attachments/assets/375889bf-1aa9-4cf0-923c-e60f5437e9ec)

### Hyper parameter
- Amount of available real data : Training data = Real data + Synthetic data에서 real data의 양
- Amount of available synthetic data : Training data = Real data + Synthetic data에서 synthetic data의 양
- Network : 사용되는 모형
- 증강 기법 : GAN

## 결론
- GAN과 기존의 증강 기법을 같이 사용하는 것이 성능이 좋음(GAN과 기존 증강 기법은 독립적)
- Training data에 너무 많은 synthetic data를 추가하면 오히려 성능 저하

