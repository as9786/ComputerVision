# Slicing Aided Hyper Inference and Fine-tuning for Small Object Detection

## 초록
- 작은 객체를 탐지하는 것은 주요 도전 과제
- 각 모형 별로 추가적인 미세 조정이 필요없는 효율적인 추론 방법 제시

## 1. 방법
- A framework based on iamge slicing
- It is based on the characteristic that dividing an input image into patches can relatively increase the pixel area of small objects with respect to the image fed into the network

### 2-1. Slicing Aided Fine-tuning(SF)

<img width="427" height="240" alt="image" src="https://github.com/user-attachments/assets/dd5cf365-b67c-4880-b2fc-ece1766d913e" />

- Patches are extracted from each image in the dataset to perform augmentation
- 각 영상은 미리 정의된 크기 M, N의 중첩된 패치로 분할
- 기존 영상에 비해 겍체의 상대적 크기를 증가

### 2-2. Slicing Aided Hyper Inference(SAHI)

<img width="421" height="230" alt="image" src="https://github.com/user-attachments/assets/54de9f5a-56d6-4692-aac6-25bee200f59d" />

- M x N 크기의 중첩된 패치로 원본 영상을 분할하고, 각 패치는 종횡비를 유지하며 크기 조정
- 원본 영상을 사용하여 기존 모형의 추론도 함께 수행
- 조정된 영상에 대한 추론값과 원본 영상에 대한 추론값이 중첩될 경우, 비 최대 억제를 통해 원래 영상 크기로 병합 
