# FAST : Faster Arbitrarily-Shaped Text Detection with Minimalist Kernel Representation

## 초록
1. Minimalist kernel representation(only has 1-channel output)

## 서론
- 현재 OCR의 문제
1. 낮은 후처리 효율성
- 후처리는 추론속도의 30%를 차지
- GPU-friendly representation method 필요
- 글자 탐지를 위해서 image classification model(ex. ResNet)을 쓰는 것은 제일 좋은 선택은 아님
- 이에 두 가지를 제안
1. Minimalist Kernel Representation(MKR)
    - Text line 주변 pixel로 둘러싸인 text region으로 형성
    - 이는 GPU 병렬에도 좋음
2. 
