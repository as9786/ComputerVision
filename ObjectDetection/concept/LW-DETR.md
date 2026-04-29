# LW-DETR: A transformer replacement to YOLO for real-time detection

## 초록
- Composed of a ViT encoder, a projector and a shallow DETR decoder
- 학습 효율 향상 기법. Window-based attention and global attention are used alternately
- Multi-Level feature maps
- Window-Major feature maps

## 방법

### Encoder

<img width="412" height="141" alt="image" src="https://github.com/user-attachments/assets/aca389c2-15b4-45c5-8d0e-5da82190f2bf" />

- ViT
- The time complexity of global self-attention is high
- The time complexity is reduced by applying window-based self-attention in some transformer encoder layers
- Intermediate feature maps, the final feature map and multi-level feature maps are aggregated
- Mixed-Query selection scheme = Content query + Spatial query
- Content query : A learnable embedding similar to that used in DETR
- Spatial query : From the final layer of the projector, tho top K features are selected to predict bounding boxes, which are then converted into embedding

### Projector

<img width="437" height="277" alt="image" src="https://github.com/user-attachments/assets/5ecb6ab9-86d2-4a94-a1e1-0694e8b4ed2e" />

- C2F block

### 목적함수
- IoU-Aware classification loss(IA-BCE loss)

<img width="298" height="53" alt="image" src="https://github.com/user-attachments/assets/032489c5-77fd-4d67-9a29-fbefb2e66d2c" />

- $\alpha=0.25$
- 전체 손실 함수는 분류 손시로가 경계 상자 손실의 합. Same as the original DETR

<img width="155" height="27" alt="image" src="https://github.com/user-attachments/assets/7ba62597-5739-45bd-a049-ff528220f5f2" />

- $\lambda_{iou}=2, \lambda_{l1}=5$

### 학습 방법
- 추가적인 감독 신호
- Group DETR

### 추론 방법
- Interleaved window attention and global attention
- Some global self-attention layers are replaced with winodw-based self-attention
- C2F block(YOLOv8)
  
