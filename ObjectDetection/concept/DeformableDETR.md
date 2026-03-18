# Deformable DETR: Deformable Transformers for End-to-End Object Detection

## 초록
- DETR은 수렴이 늦고 공간 해상도 특징이 제한
- A proposal for achieving strong performance with less training 

 ## 1. 서론

## Limitations of DETR
- 수렴이 오래 걸림
- Attention weights are initialized uniformly -> 의미 있는 위치에 집중시키기 위해 학습하는 시간이 길어짐
- DETR의 attention query는 전체 image feature를 보게 됨
- 초기 상태 : 어디가 중요한지 모름 => 모든 위치에 비슷한 가중치 => 수렴 늘미
- 
