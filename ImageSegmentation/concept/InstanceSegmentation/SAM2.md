# SAM2: Segment Anything in Images and Videos

## 서론
- SAM은 사진에서 분할을 위한 모형
- 하지만 사진은 정적
- 보편적인 분할은 동영상에도 적용되어야 함
- 동영상에서의 분할은 개체의 시공간적 범위를 결정
    1. 개체는 움직임, 변형, 가려짐, 조명 변화 등 요인으로 인해 모양이 바뀜
    2. 동영상은 camera action, blur, 낮은 해상도로 품질이 낮음
    3. 많은 수의 frame을 효율적으로 처리해야 함
- 본 논문은 사진을 frame이 하나인 동영상으로 간주
- Video domain에 사진 분할을 일반화하는 Promptable Visual Segmentation(PVS) task에 집중
- 해당 작업은 동영상의 모든 frame에서 입력 좌표, 상자 그리고 mask를 사용하여 시공간 mask인 masklet을 예측
- Masklet이 예측되면 추가로 frame에서 prompt를 제공받아 반복적으로 정제 가능
- 객체와 이전 상호작용에 대한 정보를 저장하는 저장소를 갖추고 있어 동영상 전체에 masklet을 예측하고, 이전에 관찰된 frame object에 대한 저장된 memory context를 기반으로 효과적으로 수정
- 
