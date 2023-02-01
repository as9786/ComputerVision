# Selective Search(SS)

- R-CNN, SPPNet, Fast R-CNN 방식에 후보 영역을 추천하는데 사용
- SS 사용 시 end-to-end 방식으로 학습 불가
- 실시간 적용에 어려움

# 목표

- 객체 인식이나 검출을 위한 가능한 후보 영역을 알아낼 수 있는 방법을 제공하는 것
- Exhaustive search 방식과 segmentation 방식을 결합하여 보다 뛰어난 후보 영역을 선정
- Exhaustive search : 후보가 될만한 모든 영역을 샅샅이 조사하는 방식, 후보가 될만한 대상의 크기가 일정하지 않음 => 연산 시간 증가
- Segmentation : 영상 데이터의 특성에 기반하는 방식
- Segmentation 방식으로 seed를 설정하고, 그 seed에 대하여 exhaustive한 방식으로 영역을 찾음(Data-driven SS)

![image](https://user-images.githubusercontent.com/80622859/216040720-8b5e1bf1-9eba-4a91-94c2-1a5e02a619d3.png)

- 그림의 윗 부분이 segmentation 결과, 아랫 부분은 region을 찾은 결과
- Bottom-up 방식으로 영역을 확정

1. 영상은 계층적 구조를 가지므로 적절한 방식을 사용하여, 크기에 상관 없이 대상을 찾음
2. 색상, 무늬, 명암 등 다양한 기준을 고려
3. 속도 개선

# 과정

1. 초기 sub-segmentation을 수행

![image](https://user-images.githubusercontent.com/80622859/216041105-522b6b5c-0e76-48e5-9d0e-5ba598df3878.png)

2. 작은 영역을 반복적으로 큰 영역으로 통합

![image](https://user-images.githubusercontent.com/80622859/216041205-7ef274ca-c52f-4d93-a638-39f3b7701d14.png)

- Greedy algorithm
- 여러 영역으로부터 가장 비슷한 영역을 고르고, 이것들을 통합해 나가는 방식
- 1개의 영역이 남을 때까지 반복

3. 통합된 영역들을 바탕으로 후보 영역 생성

![image](https://user-images.githubusercontent.com/80622859/216041382-ea6506ac-e475-41b7-8e21-da8f4a5a064c.png)

