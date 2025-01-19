# A Survey of Deep Learning Approaches for OCR and Document Understanding

## Document processing & understanding 

- 문서 사진으로부터 글자를 추출하여 원하는 정보를 가져와 사용하는 것은 가치가 높음
- Computer vision + NLP
- 3가지 과정
1. 문서 사진 내에서 영역 분할
2. 문서 사진 -> 글자 추출(광학 문자 인식)
3. 추출된 글자 -> 원하는 정보(IE, Information Extraction)

## Step 1 : Document Layout Analysis(DLA)

![image](https://github.com/user-attachments/assets/ba65a94c-c2b3-47a1-89a7-4b9908e2614f)

- 문서 사진 내 그림, 표, 제목, 단락 등의 다양한  구획으로 분할
- 이들을 정확하게 분리하는 것이 이후 단계를 위해 중요 
