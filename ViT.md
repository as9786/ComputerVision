# An Image is Worth 16x16 Words: Transformers for Image Recogintion as Scale

- Transformer를 사용한 구조가 수 많은 SOTA가 되고 있으며 그 시작점은 ViT
- 더 많은 data를 더 적으 cost로 사전 학습
- Image Classification을 비롯하여 다양한 분야에서 사용
- 대용량의 학습 자원과 data가 필요
- Text data에서는 이미 transformer가 가장 좋은 성능을 보이고  있음

## Visual Tranformer의 의의

![캡처](https://user-images.githubusercontent.com/80622859/185046721-e5fd8e00-d419-4737-9a37-e849c5213071.PNG)

1. 자연어 처리에 많이 사용되는 transformer를 vision task에 적용
2. 기존의 제한적인 attention 매커니즘에서 벗어나, CNN 구조 대부분을 transformer로 대체(입력층인 sequence of image patch에서는 제외)
3. 대용량 dataset을 사전 학습 -> small image dataset에서 전이 학습 => 훨씬 적은 계산 resource로 우수한 결과

## Visual Transformer 요약


