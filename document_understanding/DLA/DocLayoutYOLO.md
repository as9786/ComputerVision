# DocLayout-YOLO: Enhancing Document Layout Analysis through Diverse Synthetic Data and Global-to-Local Adaptive Perception

## 초록
- 문자와 시각적 기능들을 모두 활용하는 multi modal 방법은 높은 정확도. 속도가 느림
- Uni modal 방법은 속도는 빠르지만 정확도가 떨어짐
- 이와 같은 문제를 해결하기 위해 DocLayout-YOLO 제안
- Mesh-candidate BsetFit algorithm : 문서 내 글자, 사진, 표 등과 같은 문서의 다양한 요소들을 document layout에 배치하여 문서를 생성(2D bin-packing)
- 위 방법을 통해 DocSynth-300K 생성
- 위 data를 사용시 사전 학습 및 미세 조정에서 성능을 크게 향상 시킴
- 모형 최적화 측면에서는 문서 요소들의 다양한 크기 변형을 잘 다룰 수 있는 G2L_CRM(Global-to-Local Controllable Receptive Module)을 제안
- 다양한 문서 유형의 성능을 검증하기 위해 DocStructBench 사용

## Diverse DocSynth-300K dataset construction
- 문서 유형에 대한 적응력을 높이기 위해서는 다양한 문서로 학습해야 함
- Train set diversity type
1. Element diversity : 다양한 글자, 다양한 형식의 표 등
2. Layout diversity : 학술 논문, 잡지, 신문 등 다양한 형식


### Mesh-candidate BestFit

![image](https://github.com/user-attachments/assets/17dbd165-6c7b-41f9-a75b-ec4b8bcfd83f)

## 전처리
- 문서를 유형별로 분류 후에 element pool을 구성
- Data augmentation
    - 뒤집기
    - 밝기 및 대조
    - 자르기
    - 가장자리 추출(Sobel filter)
    - Elastic transform & Gaussian noisification(p=1)

## Layout generation
- 2D bin packing. Layout의 다양성과 일관성을 보장. Layout으로 만들어진 사용 가능한 grid를 다양한 크기의 bins로 보고, 반복적으로 최상의 매칭을 수행하여 layout의 다양성과 미적 부분의 균형을 맞춤. => 보다 다양하고 합리적인 document layouts

## G2L_CRM(Global-to-Local model architecture)
- 자연스러운 사진과 달리 문서의 다양한 요소는 한 줄 제목, 표와 같이 크게 다를 수 있음
- 이러한 규모 변화를 처리하기 위해서 CRM(Controllable Receptive Module)과 GL(Global-to-Local design) 두 가지 주요 구성 요소들로 구성된 계측정인 구조 도입
- CRM : 다양한 규모와 세분화된 기능을 유연하게 추출하고 통합. GL : Global context에서 medium scale, local context 정보에 이르는 계층적인 인식 단계를 제공

### CRM

![image](https://github.com/user-attachments/assets/f01d69c3-4ddf-4fdd-8db5-61b07d5afa4a)

- Weight-shared convolution layer(Feature extraction)
- Dilated convolution => 다양한 세분성

### GL

![image](https://github.com/user-attachments/assets/5da75044-7a95-4167-8881-1052f40cdb99)

- Global level : Dilated convolution

![image](https://github.com/user-attachments/assets/03fa2a10-d4dd-42e4-b932-c65a5e3ec34f)



