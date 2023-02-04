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


