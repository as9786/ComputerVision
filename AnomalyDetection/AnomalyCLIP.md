# Anomalyclip: Object-agnostic prompt learning for zero-shot anomaly detection

## 초록
- Zero-Shot Anomaly Detection(ZSAD) : Target dataset에서 어떠한 train sample 없이도 이상 탐지
- 다양한 domain에서의 일반화는 어려움

## 1. 서론
- Data privacy policy를 위해 ZSAD가 필요
- VLM은 사진에서의 정상성/이상성보다는 foreground 객체의 범주 의미에 일치되도록 학습

![image](https://github.com/user-attachments/assets/f53b2c0c-4c5c-4ca8-a959-c10cb85e838a)

- AnomalyCLIP은 foreground object와 상관없이 이상성, 정상성을 포착할 수 있는 object-agnostic text prompt training을 목표
- 간단하지만 보편적으로 효과적인 학습 가능한 prompt template을 정상성, 이상성 class에 대해 고안. Image-level & Pixel-level loss function => 전역적, 지역적 학습

![image](https://github.com/user-attachments/assets/c3e404e2-05e1-4223-8a31-73dc0cdca461)

## 2. AnomalyCLIP: Object-Agnostic Prompt Learning

### 2.1 Approach Overview

![image](https://github.com/user-attachments/assets/d1214615-f27b-4a31-b74e-64329f3fbf3f)

- 두 개의 일반적인 object-agnostic text prompt template $g_n, g_a$를 고안. 정상과 이상 class에 대한 일반화된 embedding
- 일반화된 text prompt template를 학습하기 위해, 전역적, 지역적 context 최적화
- Textual prompt tuning과 DPAM을 사용해서 CLIP의 texual & local visual 공간을 학습
- 최종적으로 중간층을 결합 => 더 많은 지역적 visual detail 제공
- 추론 시에는 textual과 global/local visual embedding 간의 불일치 정도를 측정하여 anomaly score과 map을 얻음

### 2.2 Object-Agnostic Text Prompt Design
- 기존 CLIP의 text prompt는 객체 의미에 집중할 뿐 정상/비정상 의미를 포착하는 textual embedding을 생성하진 못함
- 이상 탐지를 위한 text embedding을 학습하기 위해, text prompt template에 prior anomaly semantic을 통합
- 간단한 방법은 특정한 anomaly type과 함께 구성. Ex) A photo of a [cls] with scratches
- 가능한 모든 anomaly type을 나열하는 것은 어려움
- damaged [cls]로 통일
- 하지만 해당 글을 사용 시 이상 탐지를 위한 text embedding을 생성하는데 무리가 있었음
- CLIP은 객체 의미에 일치시키는 것에 집중하기 때문
- 이와 같은 한계를 극복하고자 학습 가능한 text prompt template를 도입.
- 이와 같은 text prompt를 object-aware text prompt templates로 정의

![image](https://github.com/user-attachments/assets/ee462fee-c080-45c2-bce4-56e27b2d3cd2)

- 객체 의미가 다르더라도, anomaly pattern은 유사

![image](https://github.com/user-attachments/assets/68780266-3019-4523-b1e2-94dd05ddbcb7)

- 위와 같이 object-agnostic text prompt templates 제안

### 2.3 Learning Generic Abnormality and Noramlity prompts

#### Glocal context optimization
- 전역적, 지역적 관점 모두로부터 학습할 수 있도록 하는 joint optimization 방법
- 다양한 객체 사진의 전역적인 vision embedding을 text embedding과 matching
- Local context 최적화는 vision encoder M개의 중간층으로부터의 fine-grained 지역적 이상 영역에 집중

![image](https://github.com/user-attachments/assets/202f171f-6ba4-4def-ab6d-1e0696c1dbb6)

- $L_{global}$ : Object-agnostic textual embedding과 vision embedding 간의 cosine similarity를 matching하는 cross entropy

![image](https://github.com/user-attachments/assets/a52be96e-1c3c-4739-b909-9631a6caf3c5)

- Focal loss를 통해 불균형 문제 해결

#### Refinement of the textual space
- 


