# Scene Text Recognition with Permuted Autoregressive Sequence Models

## 초록

- Context-Aware STR 방법은 전통적으로 자기 회귀 모형을 사용
- 자기 회귀 모형은 two-stage 방법을 사용. 외부 언어 모형을 사용
- 외부 언어 모형의 조건부 독립은 정확한 예측을 잘못할 수 있음
- PARSeq는 permutation language modeling을 사용하여 공유하는 가중치를 활용해 내부 자기 회귀 언어 모형의 ensemble을 학습
- 이는 context-free-non-AR과 context-aware AR inference를 단일화
- 그리고 양방향 문맥을 반복적으로 조정
- Attention 덕분에 임의의 방향의 글자에도 견고 

## 서론

- 문서들에 쓰이는 OCR은 글자 속성이 단일화되어 있는 반면, STR은 다양한 글씨체와 방향, 모양, 조명 등 조건이 다양
- STR은 vision 작업인데, 글자 부분을 읽는 것이 중요
- Image feature만으로는 정확한 추론을 하기 어려움
- 언어적 의미가 인식 과정을 돕기 위해 사용됨
- Context-Aware STR : Semantic priors 통합. 단어 표현 모형이나 사전, sequence modeling을 사용한 data로부터 학습되어지는 사전 확률을 통합
- Sequence modeling은 end-to-end 가능
- 내부 언어 모형을 활용한 STR 방법은 iamge feature와 언어 문맥을 동시에 처리
- 이는 future tokens가 past tokens에 영향을 미치는 언어 문맥에 대한 제한적인 자기 회귀를 활용
- P(y|x), x : image, y : text label
- 해당 방식은 두 가지 한계를 지님
1. 한 방향에 대해서만 token dependencies 학습. 보통 LTR(Left To Right). 이는 결과적으로 잘못된 접미사를 추가하거나, 방향 의존적인 예측 값을 내놓음
2. 추론 동안, output token을 연속적으로 같은 방향으로 출력(monotonic AR decoding)
- 해당 문제를 해결하기 위해, 기존 연구들을 left-to-right과 right-to-left를 합침
- 이는 양뱡향성 문제를 해결해주지만 시간 복잡도를 증가시킴

![image](https://github.com/user-attachments/assts/b742e714-6b41-4291-b9ce-cefa659d0760)

## Permuted Autoregressive Sequence Models

### Model Architecture

![image](https://github.com/user-attachments/assets/56d425ed-a2f2-4194-946d-6d1c41730ffc)

- Sequence modeling task에서 흔히 사용되는 구조
- Encoder는 12개의 층을 가지고 있고, decoder는 단 한 개의 층을 지니고 있음

#### ViT encoder
- Classification head가 없고, CLS token도 없음
- Standard ViT와 다르게 all output tokens z는 decoder의 입력으로 사용

#### Visio-lingual Decoder
- Prelayernorm
- 3개의 입력을 필요(위치 정보, 문맥 정보, image token). 해당 입력들의 optinal attention mask가 필요
- Context-Position attention

![image](https://github.com/user-attachments/assets/2b2a4cf5-2521-4f8b-b65c-0687404102f2)

- T : 문맥 길이, p : Position token, c : context embedding with positional information, m : Attention mask
- Special token : [B] or [E] 사용
- Position token은 예측된 target position을 encode
- 각각의 출력은 specific position에 대응
- Mask는 학습동안, 임의의 순열으로부터 생성. 추론 시에는 left-to-right mask, cloze mask, no mask가 생성
- 두 번째 MHA에서는 image-position attention이 사용

![image](https://github.com/user-attachments/assets/529ced6d-1385-40a2-8bfd-6756bb945d9c)

- 여기서는 attention mask가 사용되지 않음
- Last decoder hidden state는 MLP의 출력

![image](https://github.com/user-attachments/assets/9555be79-ae66-4d60-bef8-3856720a98aa)

### Permutation Language Modeling
- Image x가 주어지면, model parameter $\theta$들이 있다고 가정했을 때, text label y의 가능도가 최대화되어야 함
- 3개의 element sequence y에 대한 표준적인 자기 회귀 모형은 (a)에서 보여지는 attention mask를 가짐

![image](https://github.com/user-attachments/assets/1b3c6f76-3771-4846-a9f7-45f3c98339d9)

- PLM의 key idea는 모든 T! factorization의 가능도를 학습

![image](https://github.com/user-attachments/assets/c864e500-0269-43a0-8b0e-2ab5f3feefec)

- $Z_T$는 index sequence의 가능한 모든 순열 집합을 의미
- Text label y를 실제로 섞을 필요는 없음
- z에 의해 구체적인 순서를 강요하는 attention mask를 생성
- Input sequence와 output sequence의 순서는 유지되는 반면, 네 가지 순열이나 factorization order에 의해 지정된 다른 자기 회귀 모형
- 기존의 자기 회귀 모형은 하나의 순열만이 사용된 PLM의 special case
- 하지만 모든 T에 대해서 순열 집합을 계산하는 것은 비효율적
- 


