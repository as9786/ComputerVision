# Segment Anything

<img width="2006" height="507" alt="image" src="https://github.com/user-attachments/assets/a29e5a6d-9402-4132-8f8d-581fc9336d23" />

## 서론
- 사전 학습된 대규모 언어 모형은 강력한 zero-shot, few-shot 일반화로 자연어 처리를 혁신
- Foundation model은 학습 중에 볼 수 있는 것 이상으로 작업과 data distribution을 일반화
- Prompt engineering으로 구현

## Segment Anything Task 
- Next token prediction이 foundation model pre-training에 사용되고, prompt engineering을 통해 다양한 하위 작업을 해결하는 자연어처리에서 영감을 얻음

### 작업
- 자연어처리 -> 분할
- Prompt : 점, 상자, mask, 글 또는 영상에서 분할 대상을 나타내는 모든 정보
- Promptable segmentation task : Prompt가 주어지면, 유효한 segmentation mask를 반환
- 유효한의 의미 : Prompt가 모호하고, 여러 개체를 참조할 수 있는 경우에 대해 출력이 그 객체 중 적어도 하나에 대한 합리적인 mask여야 함
- Zero-Shot

### 사전 학습
- 각 학습 표본에 대한 일련의 prompt를 simulation. Model mask prediction을 GT와 비교
- Prompt가 모호한 경우에도 모든 prompt에 대해 항상 유효한 mask를 예측하는 것이 목표

## Segment Anything Model

<img width="1874" height="381" alt="image" src="https://github.com/user-attachments/assets/3dd44d4f-6623-4ed2-86de-e33361395dbf" />

- 세 가지 구성 요소
1. image encoder
2. Prompt encoder
3. Mask decoder
- ViT based

### Image encoder
- MAE pre-trained ViT

### Prompt encoder
- 두 집합의 prompt를 고려
1. Sparse(점, 상자, 글자)
2. Dense(Mask)
- CLIP text encoder를 사용하여 각 prompt type과 자유 형식 text에 대해 pre-trained embedding으로 합산된 positional encoding으로 점과 상자를 나타냄
- Mask는 합성곱을 사용하여 embedding되고 image embedding과 함께 원소별 합산

### Mask decoder
- Image embedding, prompt embedding, output token을 mask에 효율적으로 사상
- Transformer decoder block을 수정하고 dynamic mask prediction head를 사용
- Prompt self-attention과 corss-attention을 두 방향으로 사용
- 위 블록들을 지난 후, image embedding을 upsampling. MLP는 ouput token을 dynamic linear classifier로 사상한 다음 각 image position에서 mask 예측

### 모호성 해결
- 모형은 모호한 prompt가 주어지면 여러 개의 유효한 mask를 하나의 출력으로 평균화
- 단일 prompt에 대해 여러 출력 mask를 예측하도록 모형 수정
- 3개의 mask 출력이 대부분의 일반적인 경우를 처리하기에 충분하다고 판단
- 학습 중에는 mask 중 최소 손실만을 역전파
- Mask 순위를 매기기 위해 모형은 각 mask에 대한 신뢰도 점수를 예측(Ex. IoU)

### 손실과 학습
- DETR에서 사용된 focal loss와 dice loss의 선형 결합

## Segment Anything data engine
- Data engine 구축
1. Model-assisted annotation을 사용하는 수동 단계
2. 자동으로 예측된 mask와 model-assisted annotation이 혼합된 반자동 단계
3. 완전 자동 단계
- 모형은 주석 입력 없이 mask 생성

### Assisted-manual stage
- 직접 labeling
- 개체에 label을 지정하는데 의미론적 제약을 부과 X
- 주석 작성자를 따로 두어, 개체에 label을 지정
- 충분한 주석 후, 새로 주석이 달린 mask만 사용하여 재학습

## Semi-automatic stage
- 분할 능력을 향상시키기 위해 mask의 다양성을 높임

## Fully automatic stage
1. 이 단계를 시작할 때, 이전 단계의 다양한 mask를 포함하여 모형을 크게 개선할 수 있는 충분한 mask 수집
2. 모호한 경우에도 유효한 mask를 예측할 수 있도록, 모호성 인식 모형 개발
- 주석은 완전히 자동으로 이루어짐

