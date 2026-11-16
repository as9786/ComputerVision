# RetinaFace: Single-stage Dense Face Localization in the Wild

## 1. 서론

- 수백 명이 찍힌 군중 사진처럼 엄청 작은 크기의 얼굴, 가려진 얼굴, 측면으로 돌아간 얼굴들이 존재
- 기존 얼굴 검출기들은 단순히 사각형만 찾는 데 집중했기 때문에, 극단적인 조건에서는 얼굴의 형태적 맥락을 파악하지 못해 검출에 실패
- 얼굴의 기하학적 구조를 신경망이 함께 이해하도록 강제

## 2. 방법

### 2-1. 손실 함수
- 4가지 multi-task loss
- 4가지 작업을 동시에 수행하도록 손실 함수 설계

$$ L = L_{cls}(p_i, p^*_i) + \lambda_1 p^*_i L_{box} (t_i, t^*_i) + \lambda_2 p^*_i L_{pts} (l_i, l^*_i) + \lambda_3 p^*_i L_{pixel}$$

