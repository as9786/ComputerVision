# Deep Learning for 3D Point Clouds: A Survey

## 1. 소개

- 3D 기술의 급속한 발전과 함게 다양한 유형의 3D scanner, LiDAR, RGZB-D camera 등이 보다 보급됨
- 3D data는 풍부한 기하학적, 형태 및 규모 정보를 제공
- 자율 주행, robotics, 원격 감지 및 의료를 포함한 다양한 분야에서 활용
- 3D data는 일반적으로 depth images, point clouds, meshes 그리고 volumetric grids로 표현
- 일반적으로 사용되는 point cloud는 원래의 기하학적 정보를 이산화 없이 3D 공간에 보존 => 자율 주행 및 robotics과 같은 분야에서 선호

![image](https://user-images.githubusercontent.com/80622859/215386012-1de30f3b-276a-4a68-b133-34a9f7e29d32.png)


## 2. 선행 연구

### 2.1 Datasets

- 분류 : Synthetic datasets와 real-world datasets
- Synthetic datasets : 배경 X
- Real-word datasets : 다양, noise 존재

- 탐지 및 추적 : 실내 장면(Indoor scenes)과 실외 도시 장면(outdoor urban scenes)
- Indoor scenes : Dense map 또는 3D meshes로부터 sampling된 것으로부터 변환됨
- 실외 도시 장면 : 자율 주행 자동차를 위해서 고안, 객체들이 잘 분리되어 있고, point cloud가 희박

- 분할 : Mobile Laser Scanners(MLS), Aerial Laser Scanners(ALS), static Terrestrial Laser Scanners(TLS), RGB-D cameras, 기타 등등으로 촬영
- 형상 불완전성 및 class imbalance를 포함한 다양한 문제 해결을 위해 사용되는 dataset

### 2.2 평가 지표

- 분류 : QA(전체 정확도), mAc(평균 class 정확도)
- 객체 탐지 : 평균 정밀도(AP)
- 분할 : QA, mIoU, mAcc

## 5. 3D Point Cloud Segmentation

- 전체적인 기하학적 구조와 각 point의 분할된 특징들을 모두 이해해야 함
- Semantic segmentation, instance segmentation 긔리고 part segmentation으로 분류 

### 5.1 3D Semantic Segmentation

- Point cloud가 주어지면, semantic segmentation의 목표는 point의 의미에 따라 여러 하위 집합으로 분리
- Projection based, discretization-based, point-based 그리고 hybrid-based

![image](https://user-images.githubusercontent.com/80622859/215390202-1e9b4282-a571-42c2-a437-0f256088b408.png)

![image](https://user-images.githubusercontent.com/80622859/215390220-5d6d9cb2-3797-48f3-a131-cd4d9db087fe.png)


#### 5.1.1 Projection-based Method

- 일반적으로 3D point cloud를 multi-view 및 spherical images를 포함한 2D image에 투영

##### Multi-view Representation

-  Multiple virtual camera views에서 3D point cloud를 2D 평면에 투영
-  Multi-stream FCN을 사용하여 image의 pixel 단위 점수를 예측
-  각 point의 최종 semantic label은 서로 다른 뷰와 합쳐져서 얻게 됨

-  여러 camera 위치를 사용하여 point cloud의 여러 RGB 및 depth snapshots을 생성
-  2D semantic segmentation model을 사용하여 이러한 snapshots에 pixel 단위 labeling 수행
-  RGB에서 예측된 점수와 depth image는 residual correction을 사용하여 추가로 더해짐
-  Point cloud가 local Euclidean surfaces에서 sampling 된다는 가정에 기초하여, dense cloud point segmentation을 위한 tangent convolution(접선 합성곱) 도입
-  이러한 방법은 먼저 각 점 주위의 local surface geometry을 가상 접선 평면에 투영.
-  그 다음 tangent convolution이 surface geometry에서 직접 작동
-  뛰어난 확장성, 수백만 개의 point로 대규모 point cloud 처리 가능
-  Projection이 정보 손실을 초래하기 때문에 기본 기히학적 및 구조적 정보를 완전히 얻을 수 없음

##### Spherical Representation

- 빠르고 정확한 분할을 위해 squeezeNet 및 Conditional Random Field(CRF)를 기반으로 하는 end-to-end network 제안
- 분할 정확도를 향상시키기 위해 학습하지 않은 domain이더라도 domain adaptation pipleline을 통해 문제 해결(SqueezeSegV2)

- 실시간 point cloude semantic segmentation을 위해 RangeNet++ 제안
- 2D 범위의 image의 semantic label은 먼저 3D point cloud에 전송되며, 이산화 오류 및 추론 문제를 완화하기 위해 효율적인 GPU 지원 및 KNN 기반 후처리 단계가 활용
- 더 많은 정보를 유지하며 LiDAR에 적합
- 이산화 오류 및 폐색과 같은 몇 가지 문제 초래

#### 5.1.2 Discretization-based Methods

- Point cloud to dense/sparse discrete representation(ex. volumetric and sparse permutohedral lattices)

##### Dense Discretization Representation

- 초기 방법은 일반적으로 point cloud를 dense한 grid로 voxelized 그리고 표준 3D 합성곱을 사용
- 처음에는 point cloud를 voxels의 집합으로 나눔, 그리고 voxel-wise segmentation을 위해 이러한 중간 data를 fully-3D CNN에 사용
- 마지막으로 voxels 내의 모든 점에는 voxel과 동일한 semantic label이 할당
- 이 방법은 point cloud와 voxel의 경계 산출물로 사용 X

- 세분화되고 전역적으로 일관된 semantic segmentation을 위해 SEGCloud 제한
- 3D-FCNN에 의해 생성된 coarse voxel 예측을 다시 point cloud에 사상시키기 위해 3선 보간법을 사용한 다음, 완전 연결 CRF(Fully Connected CRF)를 사용하여 point label의 공간 일관성을 적용

- Voxel 내의 lcoal geometrical structures를 encoding 하기 위해 kernel based interpolate4d variational autoencoder architecture를 소개
- 이전 표현 대신 RBF가 각 voxel에 사용되어 연속 표현을 얻고 각 voxel의 점 분포를 포착
- VAE는 각 voxel 내의 점 분포를 잠재 공간에 사상하는데 추가로 사용
- 그 후 대칭 그룹과 equivalence CNN을 사용하여 강건한 특징을 학습 

- 3D CNN의 우수한 확장성 덕분에 volume-based network는 공간 크기가 다른 point cloud에서 자유롭게 학습 및 추론 가능
- FCPN(Full-Convolutional Point Network)에서 다양한 수준의 기하학적 관계는 먼저 point cloud에서 계층적으로 추상화된 다음 3D 합성곱 및 가중 평균 pooling을 사용하여 특징을 추출하고, long-range dependencies를 통합
- 대규모 point cloud를 처리할 수 있으며, 추론 중에 확장성이 좋음

- ScanComplete
- FCN의 확장성을 활용하여 훈련 및 추론 중에 다양한 입력 크기에 적용될 수 있음
- Coarse-to-fine strategy 예측된 결과의 해상도를 향상시킴

- 전체적으로 volume based representation은 3D point cloud의 이웃 구조를 자연스럽게 보존
- 3D 합성곱을 직접 적용 가능
- Voxelization은 본질적으로 이산화 산출물과 정보 손실을 초래
- 해상도가 높으면 memory 및 계산 비용이 많이 드는 반면 해상도가 낮으면 세부 정보가 손실
- 실제로는 적절한 grid 해상도를 선택하는 것은 중요하지 않음 

##### Sparse Discretization Representation

- 0이 아닌 값의 수가 차지하는 비율이 작기 때문에 volume 표현은 자연스럽게 희박
- 공간적으로 sparse data에 밀도 높은 합성곱 신경망을 적용하는 것은 비효율적
- Indexing 구조를 기반으로 한 submanifold sparse convolutional networks 제안
- 합성곱의 출력을 사용된 voxels만으로 제한함으로써 memory 및 계산 비용을 크게 감소시킴

- MinkowskiNet : 4D 시공간 합성곱 신경망
- 고차원 data를 효과적으로 처리하기 위해 일반화된 희소 합성곱이 제안
- 일관성을 강화하기 위해 trilateral-stationary conditional random field를 사용

- Sparse Lattice networks(SPLATNet) : Bilateral Convolutional layers(BCLs)에 기반
- 처음 point cloud을 정다면체 희소 격자에 보간한 다음 BCL을 적용하여 희박한 격자의 점유 부분을 합성곱 계산
- Filtering 된 출력이 다시 처음 point cloud에 보간
- Multi view image와 point cloud의 유연한 공동 처리가 가능

- LatticeNet
- DeformsSlice라는 data-dependent interpolation module이 도입되어 격자 특징을 point cloud에 back projection 함

#### 5.1.3 Hybird Method

- 사용 가능한 모든 정보를 추가로 활용하기 위해 3D scan에서 multi-modal features를 배우기 위해 몇몇 방법들이 제안되어 지고 있음
- RGB 특징과 기하하적 특징을 결합하기 위한 joint 3D-multi-view network 제안
- 특징을 추출하기 위해 3D CNN stream과 2D stream을 사용, 학습된 2D embedding과 3D 기하학적 특징을 공동으로 융합하기 위해 차별화 가능한 역투영층을 제안

- Point cloud에서 2D texture shape, 3D 구조 및 global context 기능을 학습하기 위한 통합 point 기반 framework 제안
- Voxelization 없이 희박하게 sampling 된 point set에서 local geometric feature와 global context를 추출하기 위해 point 기반 network를 직접 적용

- Standard point cloud space에서 2D multi-view image의 외관 특징과 공간 기하학적 특징을 집계하기 위해 MVPNet(Multi-view PointNet) 제안

#### 5.1.4 Point based Methods

- Point based network는 irregular point cloud에서 작동
- 그러나 point cloud는 순서가 없고 구조화되지 않아 표준 합성곱 신경망을 직접 적용하는 것은 불가능
- Shared MLP를 사용한 point별 기능과 symmetric pooling을 사용한 global 기능을 학습하는 PointNet
- Pointwise MLP methods, point convolution methods, RNN-based methods and graph-based methods

![image](https://user-images.githubusercontent.com/80622859/215403988-414cc4a7-2cbf-4fc3-9c2e-6ab29f5fa4f2.png)

##### Pointwise MLP Methods

- 보통 높은 효율성을 위해 신경망에서 shared MLP를 기본 단위로 사용
- 그러나 shared MLP에 의해 추출된 point별 기능은 point cloud의 local geometry와 point 간의 상호 작용을 포착할 수 없음
- 각 지점에 대한 더 넓은 context를 포착하고 더 풍부한 local architecture를 학습하기 위해 neighboring feature pooling, attetnion-based aggregation and local-global feature concatenation

###### Neighboring feature pooling

- Local geometric patterns를 포착하기 위해, 인접 지점의 정보를 집계하여 각 지점에 대한 기능을 학습
- PointNet++은 계층적으로 point를 주고 더 큰 local area에서 점진적으로 학습
- Point cloud의 불균일성과 다양한 밀도로 인한 문제를 극복하기 위해 multi-scale grouping과 multi-resolution grouping도 진행

- Orientation encoding과 scale awareness를 위해 PointSIFT module 제안
- 3단계 합성곱을 통해 8개의 공간 방향에서 정보를 쌓고 encoding
- 다양한 scale에 대한 적응성을 달성하기 위해 mulit-scale이 사용

- K-means clustering과 KNN을 활용하여 world space와 특징 공간에서 두 개의 이웃을 별도로 정의
- Feature space에서 동일한 class의 point가 더 가까울 것으로 예상된다는 가정에 기초하여, feature 학습을 더욱 정규화하기 위해 pairwise distance loss와 centroid loss가 사용됨

- 서로 다른 점 간의 상호 작용을 modeling 하기 위해 locally-linked web을 dense하게 구성하여 local area의 모든 점 간의 관계를 탐색하는 PointWeb
- 정보 교환 및 기능 개선을 위해 AFA(Adaptive Feature Adjustment) module이 제안
- 신경망이 차별적인 특징 표현을 학습하는데 도움을 줌

- Concentric spherical shells로부터 집계된 통계를 기반으로 Shellconv라는 permutation invariant convolution 제안
- Multi-scale concentric spheres set을 질의한 후에, max pooling 작업을 통해 통계를 요약하고 MLP 및 1D 합성곱을 사용하여 최종 합성곱 출력을 얻음

- 대규모 point cloud segmentation을 위한 RandLA-Net이라는 효율적이고 가벼운 신경망
- memory 및 계산 측면에서 매우 높은 효율성을 달성하기 위해 random point sampling을 사용
- 기하학적 특징을 포착하고 보존하기 위해 local feature aggregation 

###### Attention-based aggregation

- Attention 사용
- 점들 간의 관계를 modeling 하기 위해 group shuffle attention
- 널리 사용되는 FPS 방식을 대체하기 위해 permutation invarient에 구애받지 않고 차별화 가능한 GSS(Gumbel Subset Sampling) 제시
- 이상치에 덜 민감하고, 점의 대표적인 부분 집합을 선택할 수 있음

- Point cloud space layout과 local surface를 기반으로 공간 인식 가중치를 학습하는 LSA(Local Spatial Aware) 계층을 제안
- CRF와 유사하게, 신경망에서 생성된 분할 결과를 사후 처리하기 위해 Attention-based Score Refinement(ASR) module을 제안
- 초기 분할 결과는 학습된 attention 가중치로 인접 지점의 점수를 pooling하여 세분화
- 기존의 심층 신경망에 쉽게 통합되어 segmentation 성능을 향상시킬 수 있음

###### Local-global concatenation

- Point cloud의 local surface와 global context를 통합하기 위해 permutation invarient PS2-Net을 제안
- EdgeConv와 NetVLAD는 local information과 scene 수준의 global 기능을 포착하기 위해 반복적으로 쌓임

##### Point Convolution Methods

- Point cloud에 효과적인 합성곱 연산자를 제안
- 인접한 점들이 kernel cell로 묶인 후 kernel weight로 합성곱되는 point-wise convolution operation 제안

- Parametric continuous convolution layers
- MLP에 의해 파라미터화되고 continuous vector space에 분포됨

- Kernel Point Convolution(KPConv)
- KPConv의 paramter는 kernel point까지의 Euclidean distances로 결정. Kernel point 수는 고정되지 않음
- Kernel point의 위치는 구면 공간에 최적의 적용 범위를 정하는 최적화 문제로 공식화
- 반경 인접 지역은 일관된 receptive field를 유지하는데 사용되는 반면, grid undersampling은 다양한 point cloud 밀도에서 높은 견고성을 달성하기 위해 각 층에서 사용

- 수용 영역이 집계 기반 방식에 미치는 영향을 보여주기 위해 ablation experiment와 시각 결과를 제공
- K개의 가장 가까운 이웃 대신 확장된 이웃 특징을 집계하기 위해 Dilated Point Convolution(DPC) 사용
- 수용 영역을 늘리는데 매우 효과적. 기존의 집계 기반 신경망에 쉽게 통합 가능

#### RNN-based Methods

- 고유한 context를 찾기 위해, RNN point cloud의 semantic segmentation이 사용
- PointNet을 기반으로 입력 수준의 context를 얻기 위해 point block을 muti-scale block과 grid block으로 변환
- PointNet에 의해 추출된 block 단위 기능은 출력 수준의 context를 얻기 위해 CU(Consolidation Units) 또는 RCU(Recurrent Consolidation Units)로 순차적으로 공급
- 실험 결과는 space context를 통합하는 것이 분할 성능 향상에 중요하다는 것을 보여줌

- Lightweight local dependency modeling module, slice pooling layer를 사용하여 순서가 지정되지 않은 point feature set를 feature vector의 순서가 지정된 sequence로 변환

- Coarse-to-fine structure. Pointwise Pyramid Pooling(3P) module. 2개 방향 계층적 순환 신경망을 활용하여 장거리 공간 의존성을 추가로 얻음
- RNN을 적용하여 end-to-end 학습
- 전역 구조 특징으로 지역 이웃 특징을 집계할 대, point cloud에서 풍부한 기하학적 특징과 밀도 분포를 잃음

- Dynamic Aggregation Network(DAR-Net) : Global scene complexity와 local geometric features를 고려
- 자체 적응된 수용 영역 및 node weight를 사용하여 동적으로 작동

- Point cloud의 효율적인 의미 분석을 위해 3DCNN-DQN-RNN
- 3D CNN을 사용하여 공간 분포와 색상 특징을 학습하며, DQN은 특정 class에 속하는 개체를 localize하는데 사용됨.
- 최종 concatenated feature vector는 최종 결과를 얻기 위해 residual RNN에 전해짐

#### Graph-based Methods

- 3D point cloud의 근본적인 모양과 기하학적 구조를 얻기 위해, 몇몇 방법들은 graph networks를 사용
- Interconnected simple shapes and superpoints의 집합으로 point cloud를 표현하고, 구조와 context를 얻기 위해 attributed directed graph를 사용
- 대규모 point cloud segmentation 문제는 기하학적으로 균일한 분할, super point embedding 및 contextual segmentation으로 나눠짐

- 분할 단계를 향상시키기 위해, 지도 학습 기반의 point cloud를 pure superpoints로 oversegment하는 framework를 제안
- Adjacency graph로 구성된 deep metric 학습 문제로 정해짐
- 객체 간 경계 인식을 돕기 위해 graph 구조의 contrastive loss도 제안

- 높은 차원의 공간에서 local geometric relationships를 더 잘 포착하기 위해, Graph Embedding Module(GEM) 그리고 Pyramid Attention Network(PAN) 기반의 PyramNet 제안
- GEM module은 directed acyclic graph인 point cloud로 정의되며, 공분산 행렬을 사용하여 인접한 유사성 행렬의 구성을 위해 Euclidean distance로 대체
- PAN module에서는 네 가지 크기의 convolution kernel을 사용하여 different semantic intensities를 feature와 함께 추출

- Local neighboring set으로부터 관련있는 features를 선택적으로 배우기 위해 Graph Attention Convolution(GAC)가 제안됨
- 공간적 위치와 feature differences에 기반하여 다른 이웃 점들과 feature channels에게 동적으로 attention weight를 배정
- 분할을 위한 차별적인 features를 포착하는 것을 학습할 수 있고, CRF model에서 사용되는 비슷한 특징들을 가지고 있음

- Undirected graph representation을 사용하여 channel dimension에 따라 global contextual information 얻기 위한 PointGCR(Point Global Context Reasoning)
- Plug and play, end to end 학습
- 기존 segmentation model에 쉽게 통합 
