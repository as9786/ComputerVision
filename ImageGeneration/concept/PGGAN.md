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

