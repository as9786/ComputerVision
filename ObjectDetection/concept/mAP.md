# Mean Average Precision

## Precision-Recall

![image](https://user-images.githubusercontent.com/80622859/216757637-a2a746a9-8ab3-4e2e-a4ea-d46fff843280.png)

## Intersection over union(IoU)

![image](https://user-images.githubusercontent.com/80622859/216757680-d60848c0-fb77-4208-aeab-3f34e7be62fe.png)

- bbox가 맞는지 틀린지를 판단
- 예측된 bbox와 정답 bbox 간 중첩되는 부분의 면적을 측정해서 중첩된 면적을 합집합의 면적으로 나눠줌
- IoU의 계산 결과 값이 0.5 이상이면 제대로 검출(TP)라고 함
- IoU의 계산 결과 값이 0.5 미만이면 잘못 검출(FP)되었다고 함
- 0.5와 같은 임계값은 초매개변수

## Precision

- 정확도를 의미. 검출 결과 중 옳게 검출한 비율

![image](https://user-images.githubusercontent.com/80622859/216757759-972a89ff-4af9-4b8a-8d9b-96e191711cad.png)

## Recall

- 검출율을 의미. 실제 옳게 검출된 결과물 중에서 옳다고 예측한 것의 비율

![image](https://user-images.githubusercontent.com/80622859/216757796-4dcbe2ab-2560-4b22-afc8-db75b22768db.png)

- 일반적으로 정확도와 검출율은 서로 반비례 관계
- Precison-recall graph

## Precision-recall 곡선

- Confidence level에 대한 threshold 값의 변화에 따라 precision과 recall 값들이 달라짐
- Confidence : 검출한 것에 대한 algorithm이 얼마나 정확하다고 생각하는지 알려주는 값
- Ex) Confidence level = 0.99, 물체가 검출해야 하는 물체와 거의 일치해야 함
- Confidence level이 높다고 무조건 좋지는 않음
- Confidence level에 대한 threshold 값의 변화에 따라 달라지는 precision과 recall을 시각화한 곡선

![image](https://user-images.githubusercontent.com/80622859/216758033-07538b3b-fb62-404a-9d9f-c56205345294.png)

## Average Precision(AP)

- Precison-recall algorithm은 성능을 정량적으로 비교하기에 불편
- AP : Precision-recall graph에서 아래 쪽의 면적
- 높을수록 성능이 좋다는 것을 의미
- mAP : Class가 여러 개일 경우 각 class 당 AP를 구한 다음에 그것을 평균내준 값
