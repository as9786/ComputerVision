# Deep Image Blending

## 초록
- Image blending은 source image로부터 약간의 mask adjustment를 통해서 target image와 합치는 것
- 널리 사용되는 방식인 Poisson image bledning은 composite image에 경사 영역의 부드러움을 적용
- 그러나 이 방법은 대상 사진의 경계 pixel만 고려하므로, 질감에 적용 불가능
- Target image의 색상이 원본 사진 객체에 너무 많이 스며들어 source obejct의 내용이 크게 소실
- 본 논문은 Poisson blending loss를 제안하면서 인공 신경망에서 계산된 style, content loss를 같이 최적화. L-BFGS solver를 사용해 pixel을 반복적으로 최신화
- 혼합 영역의 경사를 부드럽게할 뿐만 아니라 혼합 지역의 질감도 유지

## 1. 서론
- 사진 혼합은 사진 합성의 방법
- 목적 : Source image의 특정 부분을 잘라서 target image 특정 좌표에 위치시키고, 자연스럽게 보이도록 함
- 하지만 자른 영역은 정확히 묘사되는 것이 쉽지 않음
- 그러므로 혼합 과정은 자른 영역이 배경과 자연스럽게 연결되어야 함
- 현재 가장 유명한 방법은 Poisson image editing
- 이 방법은 target image의 경계 pixel에 대해 혼합 경계가 부드럽도록 pixel transition 또는 작은 경사를 갖도록 혼합 영역의 pixel을 재구성
- 하지만 해당 방법은 closed-form matrix 때문에 다른 재구성 목적 함수와 결합이 쉽지 않음
- 최근에는 이를 GAN과 결합하지만, 이는 품질 좋은 data가 필요
- 본 논문에서는 two-stage blending algorithm 제안
- 첫 번째는 자연스러운 경계를 생성 후, style과 texture를 조정
- Poisson loss와 동일한 목적을 갖는 미분 가능한 손실을 제안하며, 다른 목적 함수와 쉽게 결합 가능
- Deep feature로부터 내용 및 style loss를 활용하여 실제 대상 사진뿐만 아니라 양식화된 그림에서도 동작
- 오직 source, mask, target image만 사용
- Training set이 필요 없음 => 일반화


## 2. 관련 연구 


