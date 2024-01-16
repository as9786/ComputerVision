# End-to-End Object Detection with Transformers

## Hungarian algorithm

- 두 집합 사이의 일대일 대응 시 가장 비용이 적게 드는 bipartite matching(이분 매칭)을 찾는 algorithm
- 어떠한 집합 I와 사상 대상인 집합 J가 있으며, $i \in I$를 $j \in J$에 사상하는데 드는 비용을 c(i,j)라고 할 때, $\sigma$ : I -> J로의 일대일 대응 중 가장 적은 비용이 드는 사상에 대한 permutation $\sigma$를 찾는 것
- Permutation : 사상 시 최적의 순서에 대한 식별자
- I, J에 대한 비용을 표현한 행렬에 대하여 동작
- DETR은 예측한 경계 상자를 정답 경계 상자에 일대일로 대응시키기 위해 hungarian algorithm을 사용

![image](https://github.com/as9786/ComputerVision/assets/80622859/7f9bb088-7ce4-4613-b16d-515e701b4941)

- 행은 예측한 경계 상자, 열은 정답 경계 상자, 원소들은 matching되었을 때의 비용
- 위의 사진의 경우 비용이 32

![image](https://github.com/as9786/ComputerVision/assets/80622859/df8b8ebd-9a0d-4123-bff7-dcb3eb725470)

- 한편, 위의 사진의 경우에는 비용이 12로 최소가 됨
- Hungarian algorithm은 이처럼 비용에 대한 행렬을 입력 받아, matching cost가 최소인 permutation을 출력

## 경계 상자 손실

- 기존의 방법들은 anchor box를 기반으로 예측을 수행하기 때문에 예측하는 경계 상자의 범위를 크게 벗어나지 않음
- 반면, DETR은 초기 추측이 없이 경계 상자를 예측하기 때문에 예측하는 값의 범주가 상대적으로 큼
- 따라서 절대적인 거리를 측정하는 L1 loss만 사용할 경우, 상대적인 오차는 비슷하지만 크기가 큰 상자와 크기가 작은 상자에 대하여 서로 다른 범위의 손실을 가지게 됨(큰 상자는 큰 손실, 작은 상자는 작은 손실)
- 이러한 문제를 해결하기 위해 L1 loss와 generalized IoU(GIoU) loss를 함께 사용

![image](https://github.com/as9786/ComputerVision/assets/80622859/eb96b8a9-64ea-4874-b343-227918402e6c)

![image](https://github.com/as9786/ComputerVision/assets/80622859/5c58cfe2-adde-4d96-9e1f-029e134161f0)

- GIoU는 두 경계 상자 사이의 IoU 값을 활용한 손실. Scale-invariant
- 예측한 경계 상자와 정답 경계 상자를 둘러싸는 가장 작은 상자를 구함($B(b_{\sigma (i)}.\hat b)$)
- 예측한 상자와 정답 경계 상자가 많이 겹칠수록 해당 값은 작아지고, 두 경계 상자가 멀수록 해당 값은 커짐
- $IoU(b_{\sigma (i)},\hat b)$는 두 상자의 사이의 IoU를 의미
- GIoU 식의 우변은 $B(b_{\sigma (i)}.\hat b)$에서 예측 경계 상자와 정답 경계 상자의 영역의 합을 뺀 영역
- GIoU는 -1과 1 사이의 값을 가지며, GIoU를 손실로 사용할 때, 1 - GIoU 형태로 사용하며 손실의 최댓값은 2, 최솟값은 0이 됨

![image](https://github.com/as9786/ComputerVision/assets/80622859/2130027e-4e06-4537-870f-ac6751b917f5)

- L1 loss와 GIoU loss를 사용한 전체 경계 상자 손실은 위와 같음
- $\lambda_{iou}$, $\lambda_{L1}$은 두 term 사이를 조정하는 scalar hyperparameter
- 두 손실은 mini-batch 내 객체의 수에 따라 정규화
-  

