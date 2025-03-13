# LayoutReader : Pre-training of Text and Layout for Reading Order Detection

## 초록
- 읽는 순서를 검출하는 것은 영수증과 같이 시각 정보로 구서오딘 문서를 이해하기 위한 필수적 기술
- 하지만 dataset이 없음
- 그래서 ReadingBank라는 500,000개의 문서로 이루어진 dataset 구성

## 서론
- 읽는 순서 검출은 word sequence를 구성하는 것
- 읽는 순서는 제각각

![image](https://github.com/user-attachments/assets/a1a46e1c-6eb5-42f8-a78f-1be4b46fb9b1)

- MS Word는 XML로 이루어져 있고, XML은 읽는 순서대로 구성되어 있는 점을 활용하여 대용량 dataset 구축
- LayoutReader : Seq2Seq
- 글자와 layout information을 encoding. Reading order sequence를 생성

## Problem Formulation

![image](https://github.com/user-attachments/assets/f60e95c6-aeae-4ad6-b437-1bd2c6a58acc)

- 
