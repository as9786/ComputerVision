# A Survey of Deep Learning Approaches for OCR and Document Understanding

## 1. 서론

- 광학 문자 인식(OCR)
- 정보들을 사용하여 어떤 영역이나 경계 상자가 어느 위치에 해당되는지 확인


## 2. Document Processing & Understanding

- Handcrafted rule algorithm
- Deep learning
- 객체 검출 및 영상 분할 발전. 자연어 처리 및 음성 등을 포함하는 다른 다양한 분야에도 적용
- 문자 탐지(Text detection) 및 instance segmentation을 사용
- 사업 문서 내 문자가 매우 조밀하며 길어질 수 있기 때문에, 모형 구조의 수정은 필수적
- 가장 간단한 방법은 문서를 512개의 token보다 더 작은 길이로 줄이는 것

1. CV 기반의 document layout analysis module : 각각의 문서 장을 개별적인 content area로 분할. 무관한 영역을 걸러내고, 식별된 content area를 분류
2. 광학 문자 인식(Optical Character Recognition) : 문서 내 작성된 모든 text를 찾아서 전사(transcription). CV와 NLP 사이의 경계를 넓히면서 OCR model은 문서 분석을 직접적으로 사용하거나 독립적인 방식으로 문제를 해결
3. 정보 추출 모형 : 광학 문자 인식의 출력을 이용하여 문서에서 전달되는 정보 간의 관계를 이해하고 식별

## 3. Optical Character Recognition

- 문자 탐지와 문자 전사(text transcription)으로 이루어짐
- 일반적으로 2개의 요소는 개별적. 서로 다른 모형 적용

![image](https://github.com/as9786/ComputerVision/assets/80622859/e772d355-727a-4fc5-9371-02de6e31d00a)

- 왼쪽 : 객체 탐지 모형을 통과하여 경계 상자들을 출력하고, 전사 모형을 통과하여 각각의 경계 상자 내 text를 확인
- 중앙 : 객체들은 일반적인 text instance segmentation model을 통과하여 text가 포함된 경우 pixel이 검은색으로 칠해짐. 이후 문자 전사 모형을 통과하여 text 영역 해석
- 오른쪽 : 문자별 instance segmentation 모형을 통과하여, 각 pixel에 해당하는 문자를 출력

### 3.1 Text Detection

- 영상에 나타난 text를 찾는 작업. 입력은 3차원
- 다양한 모양과 방향을 가진 text가 종종 왜곡되어 나타나기 때문에 도전적 문제
1. 문자 탐지 : text 주변의 경계 상자들의 좌표를 학습
2. Instance segmentation : Text를 가진 pixel은 표시되고, 없는 pixel은 표시되지 않은 mask 학습

#### 3.1.1 Text Detection as Object Detection

- 전통적으로 text detection은 문자들을 검출하기 위해 hand-crafting features를 사용하는 방식으로 연구
- 객체 탐지와 객체 분할의 발전으로 text detection 연구 방향의 변화가 생김
- SSD와 faster R-CNN family 등을 활용하여 text detector 구축
- Text에 대해 회귀 기반 모형을 적용한 논문은 TextBoxes(SSD에 종횡비가 긴 기본 상자 추가)
- 회귀 기반 모형들이 방향에 대처할 수 있도록 모형 수정(DMPNet, Rotation-Sensitive Regression Detector)
- Text에 맞춰 조정된 자체적인 신경망 개발
- 객체 탐지 모형은 IoU와 F1 score를 사용하여 평가
- 후보 경계 상자와 정답 경계 상자가 겹치는 정도를 총 공간으로 나눈 값
- 임계값을 선택하여 어떤 상자가 true positive로 계산되는지 결정(나머지는 false positive)

#### 3.1.2 Text Detection as Instance Segmentation
- Text는 보통 조밀하며, 문서는 자연 영상보다 훨씬 더 많은 text 정보를 포함
- 이러한 밀도 문제를 대처하기 위해 instance segmentation task로 철
- 영상 내 pixel을 미리 정의된 특정한 category로 분류
- Text boundary, characters, 인접한 characters 간의 관계에 대한 확률을 추정
- FCN과 같은 분할 기법 사용. Text가 잘못 정렬되었거나 왜곡된 경우를 위해 객체 탐지 모형 개선
- 분할 결과로부터 직접 경계 영역을 추출하여 단어 경계 영역 확보
- TextSnake는 FCN에서 text 영역, 중심선, 방향, 후보 반경 등을 예측
- Striding algorithm과 결합하여 중앙 축 점(central axis points)를 추출하여, text instance 재구성

### 3.2 Word-level versus character-level

- CRAFT는 FCN model을 사용하여 각 문자에 대한 2차원의 gausiian heatmap 출력
- 그 후 서로 가까운 문자들은 문자들의 집합으로 묶음
- RPN을 사용하여 획득한 global, word-level, character-level의 특징들을 결합
