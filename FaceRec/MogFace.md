# MogFace: Towards a Deeper Appreciation on Face Detection

## 1. 서론
- 얼굴 dataset(WIDER FACE)와 COCO set은 근본적인 환경 차이 때문에 3가지 문제 발생
1. 극단적인 스케일 편차(Scale distribution bias)
    - 20 pixel 이하의 소형 객체가 18%에 불과한 반면, WIDER FACE는 전체 얼굴의 55%가 20 pixel 미만.
    - 기존 범용 data augmentation은 이러한 극단적인 크기 차이를 올바르게 학습 못함
2. 
