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
