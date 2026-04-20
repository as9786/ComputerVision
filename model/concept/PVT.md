# Pyramid Vision Transformer

## 1. 서론

<img width="896" height="222" alt="image" src="https://github.com/user-attachments/assets/dafb4660-5b08-4620-b716-c1019dd61664" />

- It uses a progressively shrinking pyramid to achieve both high resolution and low compuational cost
- 장점
    1. Generate a global receptive field through attention
    2. Thanks to its pyramid structure, it can be integrated into many dense prediction pipelines
    3. No convolution filter

## 2. 방법

<img width="932" height="446" alt="image" src="https://github.com/user-attachments/assets/06aaaba2-ae65-4dcb-ace9-57cf99071700" />

- It consists of four stages, each producing feature maps at different scales
- The scale of the feature map is adjusted through the patch embedding layer
- Spatial-Reduction Attention(SRA)

<img width="373" height="187" alt="image" src="https://github.com/user-attachments/assets/5b09b718-4616-458c-964d-10f49a48b6d3" />

- Query는 그대로 유지하고, key, value만 downsampling
