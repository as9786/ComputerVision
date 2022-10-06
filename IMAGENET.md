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



