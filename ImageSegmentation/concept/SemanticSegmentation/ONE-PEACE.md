# ONE-PEACE: EXPLOARING ONE GENERAL REPRESENTATION MODEL TOWARD UNLIMITED MODALITIES

## Abstract

- Modality adapters, shared self-attention layers, modality FFNs로 구성
- Adapter와 FFN을 추가하여 새로운 modality를 쉽게 확장할 수 있음. Self-attention layers를 통해 multi-modal fusion이 가능
- Modal에 구애 받지 않는 cross-modal aligning contrast와 intra-modal denosing contras는 서로 다른 modality의 의미 공간을 정렬하고 modality 내에서 세밀한 detail을 포착 가능
- 무한한 modality로 확장할 수 있는 잠재력을 가지고 있음 
- 사전 학습된 computer vision 및 language를 사용하지 않고 좋은 성능

## Introduction
- 대량의 data로부터 학습한 representation model은 다양한 downstream task에서 강력한 일반화 능력을 보여줌
- Uni-modal representation model은 우수한 결과를 보여주지만 image-text, audio-text와 같이 multi-modal data를 효과적으로 활용하는데 어려움
- General representation model은 다음 조건을 충족해야 함
1. 모형 구조는 다양한 modality를 수용하고 multi-modality 간 상호 작용을 지원할 수 있을 만큼 유연해야 함
2. 사전 학습 방법은 각각의 modality에서 정보를 추출할 뿐만 아니라 modality 간에도 일치가 조정되어야 함
3. 사전 학습 방식은 일반적이고 간단해야 하며, 다양한 modality에 적용이 가능하여야 함

- 해당 모형은 여러 modality adapter와 modality fusion encoder로 구성
- 각 modality에서는 raw input을 feature sequence로 변환하는 adapter가 장착
- Modality fusion encoder는 transformer architecture의 feature sequence에서 작동
- 각 transformer block에는 shared self attention alyer와 multi modality FFN이 포함
- 