# Pyramid Scene Parsing Network

## 1. 서론
- The pyramid pooling module aggregates contextual information from differenet regions, enabling effective utilization of global context information
- 지역 문맥 정보(Local context information) : 모양, 형상, 재질 등
- 전역 문맥 정보(Global context information) : 형상과 주변 상황 모두 고려
- Global information is effective on scene parsing
- FCN fails to capture global scene text
- PSPNet uses dilated convolution

### Dilated convolution
- 실시간 분할에서 주로 사용
- 더 넓은 시야 제공
- It enlarges the receptive field without pooling, therby preserving spatial resolution and acbieves computational efficiency due to the sparsity of its weights

## 2. 방법
- 기존의 방식은 비슷한 형상 또는 재질을 가진 객체를 잘 구별하지 못함
- 배는 물 위에 있어야하지만, 땅 위에 있는 물체에 대해서도 배로 예측하는 문제 발생(전역 문맥 정보 부족)

### 2-1. Pyramid Pooling Module
- Sub-Region context
- A hierarchical global prior enables the model to capture information across different scales and sub-regions
1. Four different pyramid scales
2. 1x1 convolution to reduce dimension
3. 쌍선형 보간법

<img width="802" height="237" alt="image" src="https://github.com/user-attachments/assets/f2d1490f-33b5-4813-8ef3-e057c1435ca1" />

- Pre trained ResNet
- 보조 손실 함수 적용


