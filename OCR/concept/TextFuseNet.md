# TextFusetNet : Scene Text Detection with Richer Fused Featrues

## 초록

- 실제 생활에서 임의의 형태를 가진 글자를 탐지하는 것은 어려운 작업
- 글자를 세 개의 단계로 입력 받음(문자, 단어, 전역). 그리고 세 개를 합쳐서 다양현 형태의 글자를 탐지
- 여러 단계의 특징 표현은 일반적인 의미는 유지하면서 글자를 개별 문자로 해부하여 적절하게 표현할 수 있음
- 서로 다른 표현을 효과적으로 정렬하고 융합할 수 있는 multi-path fusion architecture를 사용하여 서로 다른 수준에서 글자의 특징을 수집 및 병합
- 해당 방법은 문자 단위의 정답 정보가 많이 없어서 사용 가능

## 1. 서론

- 글자는 다양한 형태를 가지고 있고, 배경과 같은 기타 환경에 영향을 쉽게 받음
- 기존 방법은 두 가지 형태(문자 단위, 단어 단위)
- 문자 단위 방법은 글자를 여러 문자들의 조합으로 봄
- 문자 탐지기로 문자를 탐지하고 이를 단어로 묶음
- 하지만 해당 방법은 너무 많은 시간이 듬
- 단어 기반 탐지 방법은 일반적인 객체 탐지처럼 바로 단어를 탐지함
- 해당 방식은 단순하고 효율적인 반면에, 다양한 형태의 글자를 탐지하는데 어려움을 겪음
- 이와 같은 문제를 해결하기 위해 instance segmentation 기법을 도입
- Instance segmentation 기법은 다양한 형태의 글자를 탐지하는데 도움을 줌
- 첫째, 이러한 방법은 글로벌 컨텍스트를 고려하지 않고 단일 관심 영역(RoI)을 기반으로 텍스트만 감지하므로 제한된 시각적 정보를 기반으로 부정확한 감지 결과를 생성하는 경향이 있습니다.
- 하지만 이러한 방법은 전역 정보를 고려하지 않고 단일 RoI를 기반으로 글자를 감지하므로 제한된 시각 정보를 가지게 됨-> 정확도 하락
- 다양한 수준의 단어 의미를 모형화하지 않음
- TextFuseNet은 Mask R-CNN과 Mask TextSpotter에 기반하며 글자 탐지 문제를 instance segmentation 문제로 공식화
- 세 가지 단계의 정보를 잡기 위해 Mask R-CNN 모형 구성 요소를 변경

![image](https://github.com/user-attachments/assets/a82e3791-bace-4779-8eb3-e3151a824aa2)

- Semantic segmentation branch : 전역 단계의 표현들을 추출. 탐지 안내를 해줌
- Mask R-CNN detection branch : 문자 단위, Mask R-CNN mask branch : 단어 단위
- Mask R-CNN에서 단어만 탐지하는 것이 아니라 문자도 탐지
- Multi path fusion을 통해서 각 단계를 합침

## 2. 관련 연구

### 문자 단위 방법
- SWT, MSER, FASText
- 문자인지 아닌지를 판별하는 분류기를 통해서 후보군을 추려나감
- 최종적으로 남아있는 문자들을 사전 지식 또는 군집화 모형 등을 통해서 단어로 묶음
- 그러나 해당 방식은 정교한 design과 여러 처리가 필요하여, 매우 복합하고 오류 발생 가능성을 높임
- 그러므로 항상 시간이 오래 걸림

### 단어 단위 방법
- 일반적인 객체 탐지 방법 사용
- CTPN(CNN+RNN), TextBoxes, TextBoxes++
- 해당 방식은 직사각형에 어울림
- 다양한 형태의 글자에 대비하기 위해 instance segmenation 방법들이 제안됨
- SPCNet, PSENet

## 3. 방법론

### 3.1 Framework
- 여러 단계에서 특징 표현을 추출하고 이를 합치는 과정
- 5개의 구성 요소(FPN, RPN, 의미적 분할, 탐지, instance segmentation)
- Backbone : ResNet + FPN
- 글자 영역 제안을 위해 RPN 사용
- Semantic segmentation branch를 도입함으로써, 입력 사진의 전역 단계의 특징들을 얻는데 도움을 줌
- 그 후 category를 예측하고 경계 상자 회귀를 채택하여 글자 영역 제안을 조정하는 detection branch에서 단어 및 전역 수준의 정보들을 융합하여 단어와 문자 모두를 감지
- Mask branch : Detection branch에서 탐지된 객체에 instance segmentation 적용.
- 최종적으로는 각 branch에서 추출된 특징들을 합쳐서 글자 탐지

### 3.2 Multi-level Feature Representation
- ROIAlign 사용
- Semantic segmentation brach는 FPN 구조
- 병합을 위해 1 x 1 convolution filter 사용

### 3.3 Multi-path Fusion Architecture
- Detection branch와 mask branch에 적용
- Detection branch에서 전역 및 단어 단위의 정보를 추출함
- Detection branch에서는 아직 문자 예측을 안했기 때문에 문자 단위의 정보를 활용할 수 없음
- FPN의 결과에서 RoIAlign을 적용하여 정보 추출
- 그 후 원소별 합과 합성곱층을 통해서 최종적인 feature map 추출
- 해당 feature map은 분류와 경계 상자 회귀에 사용됨

![image](https://github.com/user-attachments/assets/3db77b9b-d6fc-4d30-a317-dc2336259b38)

- Mask branch에서는 문자, 단어, 전역 단계의 특징들을 합침
- 다른 경로에서 multi-level features를 추출하고, 더 풍부한 정보를 위해 합침

![image](https://github.com/user-attachments/assets/abb5f628-50a2-445e-b657-19e8408417d7)

- $r_i$ : 입력 단어, $C_i$ : 문자 결과, b : 경계 상자, $c_j$: 문자, T : 임계값(기본값=0.8)
- $C_i$가 단어 후보 영역에 속하는지 교차 비율을 기준으로 식별
- 단어 상자가 문자를 완벽히 덮으면 1, 그렇지 않으면 0
- 감지된 단어에 대해 문자들의 수가 고정되어 있지 않기 때문에, 해당 단어에 속하는 문자들의 특징을 하나의 통합된 표현으로 나타냄

### 전체 목표

![image](https://github.com/user-attachments/assets/56e57d8d-40c0-407b-b46c-68de9686319f)

### 3.4 약한 지도 학습
- TextFuseNet은 단어와 문자를 모두 학습해야하기 때문에 annotation이 많이 필요
- 하지만 모든 dataset이 textfusenet에 맞는 정보를 제공하지 않음
- Character annotation을 만드는 것은 비용이 많이 들기 때문에 약한 지도 학습 방법 제시
- 문자와 글자를 모두 학습한 사전 학습 모형 준비
- 단어 데이터셋 A에 대해, 사전 학습된 모형 M을 통해서 문자를 추론하는 것이 목표 
- 먼저, A에 대해 M을 적용
- 문자 후보 표본을 얻을 수 있음
- $R={r_0(c_0,s_0,b_0,m_0), r_1(c_1,s_1,b_1,m_1)..., r_i(c_i,s_i,b_i,m_i)}$
- c : Category, s : Confidence score, b : Bounding box, m : Mask, r : 영역
- Confidence score 임계값과 단어 수준의 정답을 기반으로 false positive를 거르고, positive character samples를 얻음


