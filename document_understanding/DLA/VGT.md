# Vision Grid Transformer for Document Layout Analysis

## 초록

- 문서를 사전학습하거나 grid-based models은 document AI에서 좋은 성능을 보임
- 하지만 DLA는 문서 사전 학습 모형, multi-modal 방식으로 사전 학습된 모형조차 문자적 특징 또는 시각적 특징에 의존하게 됨
- Grid based model은 사전 학습의 효과를 무시
- 위 문제를 해결하기 위해 본 논문에서는 VGT를 제안. 해당 모형은 2D token-level & segment level 이해를 위해 제안
- $D^4LA$라는 새로운 dataset 제안 

## 서론
- DLA는 문서를 구조화된 표현으로 변환. 이는 후속 작업을 위해서 중요
- DLA의 목표는 시각적 단서와 문서 내용을 토대로 문서 구역을 탐지하고 식별하는 것
- 하지만 DLA는 여러 가지 어려움을 지님
    - 다양한 문서 종류
    - 복잡한 형식
    - 저화질
    - 의미적 이해
- DLA는 객체 탐지와 의미적 분할 작업으로 간주될 수 있음
- Document Image Transformer(DiT)처럼 문서를 사전학습하는 것도 좋은 방법
- 문서는 multi-modal 특징을 지니고 있음. 그래서 multi-modal 방식으로 사전학습을 진행하지만 미세 조정 시 시각적 정보만을 사용한다는 단점
- Grid based method는 layout 정보가 포함된 글자를 2D semantic representation 또는 sentence-grid로 투영하고 시각적 특징과 결합
- Grid based는 추가적인 글자 입력이 가능하지만, DLA 작업 학습 시에는 시각적 지도 학습 방법만이 사용됨

![image](https://github.com/user-attachments/assets/edc9aba1-508d-433a-8ee9-1000d539f4a1)

- DLA dataset은 제한적
- 현재는 논문 위주로 dataset이 구성
- 하지만 현실은 다양한 문서가 존재
- Label 또한 논문에 맞춰서 제목, 문단, 초록 등으로 구성
- 본 논문에서는 2D language information을 직접 modeling하기 위해 GiT가 포함된 two-stream multi-modal VGT 제안
- 문서를 2D token-level grid로 표현하고 GiT에 입력
- GiT는 두 가지 사전 학습 방법 사용
- Masked Grid Language Modeling(MGLM) : 일부 token을 무작위로 masking하고 2D spacial context를 통해서 원본을 복구하는 작업
- Segment Language Modeling(SLM) : 대조 학습을 통해 GiT의 표현과 기존 언어 모형의 표현을 일치시킴
- Token-level & Semantic-level 특징은 좌표에 따라 RoIAlign을 통해 GiT가 encoding한 2D grid feature에서 얻음
- ViT의 vision feature를 추가로 결합하여 GiT와 ViT의 글자 및 시각적 특징을 최대한 활용
- Diverse and Detailed Dataset ever for Document Layout Analysis($D^4LA$) dataset 제안

![image](https://github.com/user-attachments/assets/394cf8c3-ae1b-4a63-a9e4-9a47579f10a3)

## 2. 관련 연구
- 이전에는 규칙 기반 접근. Pixel 및 문맥 정보 활용
- 단순 vision tech로 접근(합성곱 신경망)
- 자기 지도 학습 기반의 사전 학습 방법론은 좋은 효과를 보임
- 이후 많은 모형들이 사전 학습 및 multi-modal 방법론을 사용했지만 text embedding 과정 없이 vision backbone을 사용
- Grid based는 text 정보를 사용하지만 단순히 입력으로만 사용
- 또한, news, 논문, 잡지 등에 국한되어 있었음

## 3. Vision Grid Transformer 

![image](https://github.com/user-attachments/assets/9b431790-354e-4db8-b703-be506f75d07d)

- GiT는 MGLM과 SLM으로 사전 학습

### 3.1 Vision Transformer
- 일반적이 ViT

### 3.2 Grid Transformer
- ViT와 유사
- PDFPlumber를 사용해서 경계 상자의 단어들을 추출
- 사진들에 대해서는 open-sourced OCR 적용
- Tokenizer를 통해서 단어들을 sub-word로 쪼개고, 이를 단어 상자의 너비 또한 sub-word와 동일하게 나눔
- Background pixel은 special token [PAD]로

### 3.3 Pre-Training for Grid Transformer
- MGLM & SLM
- VGT는 Grid 입력 내에서 시각과 언어 사전 학습을 분리. 오직 GiT만 사전 학습
- 이유
    1. 유연성 : ViT에는 다른 사전 학습을 적용 가능
    2. GiT 자체에 공간적 정보를 포함하고 있음
    3. 효율성 : 속도를 위해 

#### Masked Grid Language Modeling(MGLM) 
- MLM 2D version
- - FPN을 통해서 GiT feature 출력
- RoIAlign을 통해서 region textual feature를 추출
- 이후 masking 된 지역을 복원
- 이는 2D 공간 정보를 보존

#### Segment Language Modeling(SLM)
- Token-level의 정확도는 크게 중요하지 않음
- Segment-level이 더 중요
- SLM을 통해 segment level 학습
- PDFMiner를 통해서 줄을 추출
- 언어 모형(BERT 등)을 사용해서 segment $l_i$에 대한 특징 $e_i$를 pseudo target으로 둠
- Semantic feature $e_{l_i}$는 line box로부터 RoIAlign을 통해 추출
- 대조 학습을 통해서 최적화(Cosine similarity)

### 3-4. Multi-Scale Multi-Modal Feature Fusion
- FPN은 다양한 크기의 특징을 추출하기 위해서 사용됨
- 4개의 다른 transformer block을 사용 후, FPN을 통해 합침
- GiT와 ViT의 출력을 요소별 합으로 최종 특징 출력

## 4. $D^4LA Dataset$

### 문서 요약
- RVL-CDIP에서 추출
- 12개의 문서 유형을 선택. 각 유형마다 1000장을 직업 라벨링
- Filtering

![image](https://github.com/user-attachments/assets/e561edfd-1c12-4f18-8c50-d53325c7fb57)

### Category Description
- 27가지의 layout categories
- Key-Value로 구성된 RegionKV와 그렇지 않은 RegionList로 분류

![image](https://github.com/user-attachments/assets/abceee48-5697-4719-9446-6f629dfad134)

### 특징
- 다양한 유형과 특징
- 다만, 저화질이 많기 때문에 이를 해결해야 함




