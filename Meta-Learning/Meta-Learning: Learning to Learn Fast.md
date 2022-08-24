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
- 좋은 meta-learning model은 학습하는 task에 대한 다양성에 대해서 학습되어야 하고, 잠재적으로 인지되지 못한 task를 포함해서 여러 task들의 분포상에서 최고의 성능을 낼 수 있도록 최적화되어야 함
- 각 task들이 dataset D로 구성되어 있는데, 여기에는 각각 feature vector들과 true label들이 포함되어 있음
- 이 때 optimal model parameter는 아래와 같음

![캡처](https://user-images.githubusercontent.com/80622859/186351180-f25087b2-bbca-4338-bd60-123fd8e7dd50.PNG)

- 여러 개의 dataset 중에서 샘플링된 dataset D에 대해서 loss function $L_\theta(D)$ 을 최소화할 수 있는 $\theta$를 찾겠다는 의미
- 일반적인 learning task와 매우 유사하지만, 한 가지 다른 부분은 하나의 dataset 자체가 하나의 data sample로 활용되고 있음
- Few-shot classification은 지도 학습 상에서 meta-learning을 활용한 예시
- dataset D는 크게 두 가지로 나눔
1. learning을 위한 support set S
2. trainin이나 testing을 위한 prediction set B
- dataset D = <S,B>
- K-shot N-class classification task : support set이 각 N개 class에 대해서 K개로 labeling된 데이터를 포함하고 있다는 것

![캡처](https://user-images.githubusercontent.com/80622859/186352121-16c02fcd-6eb4-41ae-a9d1-b830965b9d34.PNG)

### Training in the Same Way as Testing
- dataset D는 여러 쌍의 feature vector와 label들을 포함하고 있고, $D={(x_i,y_i)}$ 라고 표현 가능

![캡처](https://user-images.githubusercontent.com/80622859/186352707-998817e2-0087-4004-98ed-bfd33acf8aac.PNG)

- label은 우리가 알고 있는 label set L에 속해 있다고 가정하고, parameter $\theta$를 가진 classifer $f_\theta$는 주어진 데이터가 feature vector x에 대해서 class y에 속할 확률인 $P_\theta(y|x)$ 를 출력으로 내보냄
- optimal parameter는 dataset D 내에 있는 여러 개의 training batch B에 대해서 true label을 얻을 수 있는 확률을 높여야 함
- Few-shot classification의 목표는 fast learning을 위해서 추가한, 약간의 support set을 가지고 unknown label에 대한 데이터의 prediction error를 줄이는 것
1. Label set에서 일부를 샘플링 
2. Support set과 training batch를 dataset으로부터 샘플링(두 개의 set모두 1에서 샘플링된 label set에 속한 label을 가진 데이터만 가지고 있어야함)
3. Support set은 모델의 input
4. Final optimizer 단계에서는 지도 학습에서 하는 것과 동일한 방법으로, mini-batch $B^L$을 이용해서 loss를 계산하고, 역전파를 통해서 model parameter를 update함
- $(S^L,B^L)$이 하나의 data point로 고려. 그러면 model은 다른 dataset에 대해서도 일반화할 수 있도록 학습
