# 1. 개념
- 일반적인 기계 학습 분류 문제에서는 정확도나 F1-score를 주로 사용

## 1-1. APCER(Attack Presentation Classification Error Rate)
- 공격자 오인식율
- 가짜 얼굴이 들어왔을 때, 진짜 얼굴로 잘못 판별하여 통과시켜 버린 비율
- 보안의 치명적인 구멍
- 진짜로 오판된 가짜 시도 횟수/전체 가짜 공격 시도 횟수
- 가짜 얼굴 100장을 넣었을 때, 5장이 진짜로 인식할 경우. APCER=5%

## 1-2. BPCER(Bona Fide Presentation Classification Error Rate)
- 정상 사용자 오거부율
- 진짜 정상 사용자가 얼굴을 비췄을 때, 가짜로 오인하여 입장을 거부해 버린 비율
- 사용자 경험 저해
- 가짜로 오판된 진짜 시도 횟수/전체 가짜 시도 횟수
- 정상 직원 100명 중 3명이 거부 당했으면. BPCER=3%

## 1-3. ACER(Average Classificaiton Error Rate)
- 평균 분류 오류율
- APCER과 BPCER의 단순 평균
- 모형의 종합적인 기술력을 직관적으로 비교할 때 가장 흔하게 활용
- 낮을수록 우수한 모형
- ACER = (APCER + BPCER) / 2

## 1-4. EER(Equal Error Rate)
- 동일 오류율
- 임계값을 조절하다보니, APCER과 BPCER이 같아지는 순간의 오류율

## 1-5. HTER(Half Total Error Rate)
- 반종합 오류율
- Validation set에서 구한 최적의 임계값을 고정해두고, 이를 test set에 대입했을 때나오는 ACER
  
