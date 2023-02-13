# Style Transfer

- 두 영상(content image & style image)이 주어졌을 때 그 image의 주된 형태를 content image와 유사하게 유지하면서 style만 우리가 원하는 style image와 유사하게 바꾸는 것
- 두 가지 방법
1. ImageNet 등의 data로 pretrained network를 이용한 방법
- Content image와 style image를 신경망에 통과시킬 때 나온 각각의 feature map을 저장하고, 새롭게 합성될 영상의 feature map이 content image와 style image로부터 나온 feature map과 비슷한 특성을 가지도록 영상을 최적화
- 장점 : 2장으로 수행 가능
- 단점 : 매번 image를 새롭게 최적화 =? 시간 문제
2. Style transfer network를 학습
