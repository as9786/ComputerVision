# Language Matters: A Weakly Supervised Vision-Language Pre-training Approach for Scene Text Detection and Spotting

## 초록

- Vision-Language Pre-training 기술들은 OCR에 좋은 영향을 보임
- 하지만 이는 쉽지 않음
- 시각적 정보와 textual information을 함께 학습하고 정렬여 효과적인 scene text representation을 획득할 수 있는 weakly supervised pre-training oCLIP 제시
- 신경망은 image encoder와 character-aware text encoder로 구성

## 1 서론
- 현존하는 OCR 기술들은 시각적 특징을 추출하고 회귀나 분류를 통해 글자를 탐지하고 인식

![image](https://github.com/user-attachments/assets/3ef60ee8-ca83-47f7-95c4-93fc965ab12b)

- 하지만 사람들은 시각정 정보뿐만 아니라 글자 지식들도 활용함
- 그러므로 모형도 시각정 정보와 글자 지식들을 같이 학습해야 함
- 최근에는 VLP(Vision-Language Pre-training) 기법들이 등장(VQA etc)
- VL(Vision-Language) 작업의 각 사진은 일반적을 ㅗ단어 또는 구문(token)이 읽기 순서대로 배열된 하나의 문장과 연관
- 반면, OCR 작업의 사진은 하나 또는 여러 개의 tokens로 구성된 여러 text instance를 포함하는 경우가 많음
- 같은 text instance 내의 token들은 연관되어 있지만, 다른 text instance tokens는 연관이 없는 경우가 많음
- 또한, Image-text 쌍을 수집하기 어려움
- oCLIP(OCR Contrastive Language-Image Pre-training)은 위의 문제점들을 보완
- 관계 없는 text instances 간의 관계는 고려하지 않고 각 text instance 내 sequence of characters로부터 사걱적 정보를 encoding하여 언어 특징을 추출
- Visiual-Texture decoder를 사용하여 입력 사진과 각 labelled text instance 간의 관계를 모형화
- 위 두 가지 방법을 통해 data 수집의 어려움은 크게 완화
- 세 가지 기여
1. End-to-End
2. Character-aware text encoder, visual-textual decoder
3. 더 나은 성능

## 2 관련 연구
- 
  




