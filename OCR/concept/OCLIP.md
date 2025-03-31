![image](https://github.com/user-attachments/assets/c0f50c5c-fafc-4c81-9c2f-5265c146d492)# Language Matters: A Weakly Supervised Vision-Language Pre-training Approach for Scene Text Detection and Spotting

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

### 2.1 Scene Text Detection and Spotting
- 대부분의 최신 글자 탐지기들은 fully-annotated data로 학습
1. 문자 단위 탐지 후, 군집화를 해나가는 방식(Bottom-Up)
2. 객체 탐지 문제로 치환
- 게다가 많은 방법들이 data bias를 다루기 위해 고안됨

### 2.2 Vision-Language Pre-training

## 3 방법

![image](https://github.com/user-attachments/assets/6b074556-9f64-4ecd-bc30-413c66111889)

- 입력 사진으로부터 image embedding을 얻음(ResNet-50 + Multi-head attention layer)
- Character-aware text encoder는 각 text instance 내에 sequence of characters를 encoding함으로써 입력 사진 내의 text instances의 transcriptions로부터 문맥적 정보를 추출하도록 고안
- 추출된 시각적 정보와 문맥적 정보는 visual-textual decoder로 들어감
- 학습 중에, 각 text instance에 무작위로 masking. 신경망은 masked characters를 예측하도록 최적화

## 3.1 Character-Aware Text Encoder

- 일반적인 VL 작업에서는 글자들은 보통 sequences of text tokens로 구성된 문장들
- 이에 따라, VL 작업들은 순차적인 방식으로 글자들을 encode
- 하지만 OCR에서는 하나 이상의 text instances를 포함
- OCR에서 text instances들은 모두 연관이 있는 것은 아님
- 이러한 부분이 OCR에서의 VL 작업을 어렵게 함
- 위 문제를 해결하기 위해 character-aware text encoder를 사용
- 이 encoder는 문자열 연속인 text instances로부터 instance-level text embedding을 추출

![image](https://github.com/user-attachments/assets/6e0648ba-bc6c-4610-81a8-373544f21391)

- $T={t_0, t_1, ..., t_{n-1}$ : Annotated text instances, $t_i = [c^i_0, c^i_1,...,c^i_{k=1}]$ : Sequence of characters, $W_c$ : Character embedding matrix
- 문자를 고정된 크기의 vector로 변환하고, poisitional encoding PE를 더함
- ce는 transformer encoder를 통과
- 무작위로 몇 개의 text instance masking
- 





