# Meta-Learning: Learning to Learn Fast
- 몇몇 training 예제를 통해서 모델로 하여금, 새로운 기술을 배우거나, 새로운 환경에 빠르게 적응할 수 있도록 설계하는 것
1) (metric 기반) efficient distance metric을 학습하는 방식
2) (model 기반) external/internal memory를 통한 (recurrent) network를 사용하는 방식
3) (optimization 기반) fast learning을 위한 model parameter를 최적화하는 방식
- 머신러닝에서도 적은 샘플만을 가지고도 새로운 개념과 기술을 빠르게 학습하도록 하는 것
- 좋은 meta-learning model : training time 동안에 접하지 않았던 새로운 task나 environment에 대해서 잘 적응하거나, 일반화가 잘 되는 것
- task : 지도학습이나 강화학습과 같이 machine learning으로 정의될 수 있는 모든 문제들
- ex) : 고양이가 없는 이미지를 학습시킨 classifier도 몇 개의 고양이 사진을 본 후에는 test image 상에 고양이가 있는지 판단 가능

## Define the Meta-Learning Problem

### A Simple View
