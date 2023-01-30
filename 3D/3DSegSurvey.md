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
