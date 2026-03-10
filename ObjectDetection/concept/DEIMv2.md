# Real-Time Object Detection Meets DINOv3

# 초록
- 단순하면서 효과적인 dense O2O에 기반하여, DEIM은 더 빠른 수렴과 향상된 성능을 보여줌
- Backbone : DINOv3 or distilled using DINOv3
- Spatial Tuning Adapter(STA)
- 단일 크기 출력을 효율적으로 다중 크기 특징으로 변환. 강력한 의미적 표현에 대한 세밀함을 보완=> 검출 성능 향상

## 1. 서론
- DETR-based approaches are preferred due to their end-to-end design
- Propose DEIMv2 by integrating the DEIM pipeline with DINOv3
- STA operates in parallel with DINOv3 and efficiently transforms the single-scale output of DINOv3 into multi-scale features required for object detection without additional parameters
- 
