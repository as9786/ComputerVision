# Deformable DETR: Deformable Transformers for End-to-End Object Detection

## 초록
- DETR은 수렴이 늦고 공간 해상도 특징이 제한
- A proposal for achieving strong performance with less training 

## 1. 서론

## Limitations of DETR
- 수렴이 오래 걸림
- Attention weights are initialized uniformly -> 의미 있는 위치에 집중시키기 위해 학습하는 시간이 길어짐
- DETR의 attention query는 전체 image feature를 보게 됨
- 초기 상태 : 어디가 중요한지 모름 => 모든 위치에 비슷한 가중치 => 수렴 느림
- 작은 객체에 대한 성능이 낮음

<img width="591" height="424" alt="image" src="https://github.com/user-attachments/assets/2effade5-1cde-473a-8965-4aa9e682c510" />

- Deformable DETR uses multi-scale features to detect small objects with high-resolution feature maps (DETR can't utilize them due to computational compexity)
- Multi-head attention -> Deformable attention module (Attention is performed by sampling a set of locations, similar to deformable convolution)
- It aggregates multi-scale features without FPN

## 2. 방법

<img width="652" height="401" alt="image" src="https://github.com/user-attachments/assets/5ee2e3fd-ce90-42a7-8d1d-eeda667f533a" />

<img width="596" height="74" alt="image" src="https://github.com/user-attachments/assets/31803b47-5277-45b2-9f36-56f19e1a8b53" />

### Deformable attention module
- Sampling a small seft of keys around the reference point and attends only to those locations
- Referecne point : Query가 여기가 객체일 것 같다 생각한 중심 좌표
- Sampling process
    1. Set reference point (Init random, learnable parameter) : (x, y)
    2. Offset을 이용하여 주변 위치 탐색 : $(x+ \nabla x_1, y + \nabla y_1)$. Offset은 학습을 통해 최신화 
    3. 선택된 위치들을 K(key)로 사용
    4. 해당 K끼리 attention 연산 수행(Deformable attention)

### Multi-Scale deformable attention module
- It leverages multi-scale feature maps from the backbone network, considering featrues from multiple stages similar to an FPN.
- Previously, each attention head focused on a single sampling point, but here each attention head attends to multiple sampling points across multiple scales. 
- 4개의 크기를 사용한다면, 각 크기마다 reference points를 추출하여 모든 크기에서 정보를 가져옴

### Deformable transformer Encoder
- The encoder takes multi-stage feature maps as input
- These feature maps are transformed into the same dimension using 1 x 1 convolutions and the input and output resolutions remain the same
- To enable information exchange across multi-scale feature maps, a top-down FPN structure is not used 

### Deformable transformer decoder
- Cross-Attention + Self-Attention
- Cross-Attention uses multi-scale deformable attention


