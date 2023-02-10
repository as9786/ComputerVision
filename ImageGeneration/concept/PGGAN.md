# Progressive Growing of GANs for Improved Quality, Stability, and Variation

## 1.1 문제점

- 이전까지 GAN 모형들은 high resolution image를 만드는 것이 힘들었음
- 고해상도일수록 판별기는 생성기가 생성한 image가 진짜인지 아닌지를 구분하기가 쉬워짐
- 고해상도로 만든다고 해도, memory issue로 mini-batch size를 줄여야 함 -> Batch size를 줄이면 학습과정 중 학습이 불안정

## 1.2 접근법

- 점진적으로 생성기와 판별기를 키우자
- 저해상도에서 고해상도로 키우기 위해 점진적으로 층을 추가 => High resolution image
- 논문에서는 1024 x 1024까지 생성

## 2. Progressive Growing of GANs

![image](https://user-images.githubusercontent.com/80622859/217967097-861c8e1c-318f-42e1-af15-95bad84f0bbd.png)

### 2.1 점진적으로 층을 추가해서 학습하는 장점

- Image distribution에서 large scale 구조를 먼저 발견하도록 도움을 줌
- Large scale : ex) 사람 얼굴에 대한 dataset이 있을 때, 전반적인 전체 얼굴의 형태
- G와 D의 model을 점진적으로 쌓아 올려가며 학습을 하는 것
- 처음에는 저해상도에서 보여질 수 있는 feature인 large scale들을 보면서 사람 얼굴에 대한 전반적인 내용들을 학습하고 점차 층을 쌓아 세부적인 특징들(눈, 코, 입 등)을 보면서 학습을 진행
- 
