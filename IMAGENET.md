# IMAGENET croudsourcing, benchmarking & other cool things

## Constructing of ImageNet

### Constructing

#### 1. Internet을 통해 후보 images 모음
- Query expansion
- 동의어 : German shepherd = German police dog
- 상위 class로부터의 단어 추가 : sheepdog, dog
- Multiple languages : Italian, Dutch, Spanish, Chinese
- More engines : YAHOO!, microsoft live search, picsearch, flickr, Google Image Search
- Parallel downloading
- 하나는 사전과 유의어/반의어 사전의 배합을 만들어 보다 직관적으로 사용할 수 있고 자동화된 본문 분석과 인공 지능 응용을 뒷받침
- synset(유의어 집단)

#### 2. 수작업으로 후보 images를 골라냄
- 유의한 사진의 수 : 40,000
- 유의한 사진 당 labeling할 후보 images의 수 : 10,000
- 검증 시 필요한 사람의 수 : 2~5
- 사람이 labeling할 때 걸리는 속도 : 2 images/sec
- 40,000 x 10,000 x 3/2 = 600,000,000 sec = 19 years
- Crowdsourcing 발견 => 대량 병렬화(N) = %10^{2~3}$
- $40,000 x 10,000 x 3/2 = 600,000,000 sec = \frac{19 years}{N}$
- 기본 UI

![캡처](https://user-images.githubusercontent.com/80622859/194321391-067e166f-8de1-4712-817d-1a37a07f6b51.PNG)

- 향상 방안
#### 1. Wiki와 goole links에 제공

#### 2. 작업자가 정의를 읽는지 확인
- 단어는 모호함
- 이러한 유의어들은 얻기 힘듦
- 몇몇 작업자들은 읽지 않거나 이해하지 않음 => 정의 문제

![캡처](https://user-images.githubusercontent.com/80622859/194321855-779a3749-a6b7-4cb2-ab81-029d4f4108ce.PNG)

#### 3. Feedback 허용

- Crowdsourcing을 통해서 많은 data를 만들어 낼 수 있었음
- 다양성

![캡처](https://user-images.githubusercontent.com/80622859/194322213-9a16e5b0-5ecd-43cb-80b2-ad22b9726b7c.PNG)

- 의미적 계급

![캡처](https://user-images.githubusercontent.com/80622859/194322266-08b9be5d-db6d-4508-97de-a3d8fe92a972.PNG)

- 크기

![캡처](https://user-images.githubusercontent.com/80622859/194322344-2d36d3b2-7c4a-43fa-b5fb-d88bf99d8a7a.PNG)

![캡처](https://user-images.githubusercontent.com/80622859/194322405-5185531b-c74f-4803-aad4-a103ec5dec4c.PNG)

- 무료 datasets 간 비교

![캡처](https://user-images.githubusercontent.com/80622859/194322499-39fe72e8-ae0b-4eab-951c-baf55544e242.PNG)

## Benchmarking : what dose classifying 10k+ image categories tell us?

### Basic evaluation setup
- IMAGENET : 10,000 categories, 9 million images, 50 : 50 train test split
- Multi-class classification in 1-vs-all framework

### Computation issues first

#### BOW + SVM
- 1-vs-all with LIBLINEAR -> 1 CPU 시간
- 10,000 categories -> 1 CPU 시간

#### SPM + SVM
- Memory bottlenect -> 조정 필요
- 10,000 categories -> 6 CPU 시간

#### Cluster에서의 병렬화
- 하나의 실험을 하는데 몇 주 걸림

### Size matters

![캡처](https://user-images.githubusercontent.com/80622859/194323507-0c4f642a-b417-4703-a69c-fff28c6008b8.PNG)

- Data 세트 크기가 다를 때, 서로 다른 범주에 대한 결론을 도출

![캡처](https://user-images.githubusercontent.com/80622859/194323765-6e9321cf-12ff-48cb-be02-d8332d3941c8.PNG)

- 개념의 순수 의미 체계화는 의미 있는 시각적 구조를 나타냄

![캡처](https://user-images.githubusercontent.com/80622859/194323923-dffc4b49-6f95-4630-b424-856dc47c6c33.PNG)

### Density matters
- Datasets의 밀도 또는 희소성이 매우 다름
- 기능 및 분류기 선택과 무관하게 서로 다른 dataset 간의 난이도에 상당한 차이가 있음

### Hiearchy matters
- "개"를 "고양이"로 분류하는 것은 아마도 "전자레인지"로 분류하는 것만큼 나쁘지 않을 것이다.
- 분류 비용을 통합하는 간단한 방법

![캡처](https://user-images.githubusercontent.com/80622859/194324411-95cf63b0-e22b-454e-8f6b-fdd8183aacad.PNG)

## Summary
- ImageNet은 dataset과 knowledge ontology를 구축
- 새로운 검색 분야에 대해서 거대한 크기의 image dataset 구축(Crowdsourcing)







