# MixNet: Toward Accurate Detection of Challenging Scene Text Text in the Wild

## 서론
- 작은 글자를 검출하는 것은 불규칙한 위치, different style, 조명 조건 등 여러 가지 요인으로 인해 어려움 

## 모형
- 글자를 정확하게 검출하기 위해 CNN + Transformer의 장점을 결합한 MixNet
- Two core module
1. Feature Shuffle Network(FSNet)
    - Backbone of MixNet
    - Feature shuffling
    - 여러 크기 간의 특징(feature) 교환을 허용하여 고해상도, 고품질 특징을 생성
2. Central Transformer Block(CTBlock)
    - 글자 영역의 주요 축에 중점을 둠
    - 글자의 윤곽 또는 가장자리를 감지하는 방법보다, 작은 글자가 밀접하게 나타나는 어려운 상황에서 효과적
- MixNet architecture

![image](https://github.com/user-attachments/assets/98073091-25c7-4011-83b6-23e300f2d289)

