# NMS

- Non-Maximium Suppression
- 동일한 객체에 여려 개의 경계 상자가 있다면, 가장 점수가 높은 상자만 남기고 나머지를 제거하는 방법
- 입력 : 경계 상자들, confidence scores, 중첩 임계값
- 출력 : BBox which is filtered

## Algorithm

1. Confidence score가 가장 높은 경계 상자를 선택하고 예비 후보군에서 제거 후, 최종 후보군에 추가
2. 최종 후보군에 추가된 경계 상자와 나머지 경계 상자를 비교 후, IoU가 임계 값보다 큰 경우 예비 후보군에서 제거
3. 다시 예비 후보군에서 confidence score가 가장 높은 경계 상자를 제거하고, 최종 후보군에 추가
4. 다시 한 번 최종 후보군에 추가된 경계 상자와 예비 후보군에 남아 있는 경계 상자 간 IoU를 계산하여 임계값보다 높은 경계 상자를 제거
5. 예비 후보군에 경계 상자가 존재하지 않을 때까지 반복

![image](https://github.com/as9786/ComputerVision/assets/80622859/b910c6c1-c016-48c3-958d-33f0c06f70f4)

# Soft-NMS

- 임계값을 설정하는 것은 어려움

![image](https://github.com/as9786/ComputerVision/assets/80622859/d400f81f-1918-406f-bc76-c9c5392d5868)

- 임계값에 따라 confidence score가 가장 높은 0.9를 제외하고 0.8의 말은 사라지게 됨
- Soft-NMS는 일정 비율 이상으로 겹쳐진 경계 상자를 제거하는 것이 아닌 confidence score를 줄임
- 이 방법은 mAP의 성능을 떨어뜨리지 않음

![image](https://github.com/as9786/ComputerVision/assets/80622859/b72f2149-6a74-49bf-9cc8-645ab06ee99d)

![image](https://github.com/as9786/ComputerVision/assets/80622859/7e0c9d70-ba92-4707-b5cf-49643b2f0808)

