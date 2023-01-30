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

