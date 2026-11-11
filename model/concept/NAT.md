# Neighborhood Attention Transformer(NAT)

## 초록
- 각 pixel이 자기 주변 가장 가까운 k x k neighbor pixel에만 attnetion을 수행하는 방법
- Self-Attention 시간 복잡도 $O(N^2)$ -> O(N)
- Swin transformer처럼 영상을 격자로 강제 분할하거나 pixel shift를 하지 않아도 수용 영역이 넓어짐.
- Winodw attention보다 최대 40% 빠르고 memory를 25% 덜 사용

## 1. 서론
- Stand-Alone Self-Attention(SASA)의 한계 : 합성곱 신경망처럼 sliding winodw 방식으로 local attention을 수행하려고 했으나, GPU에서 병렬화하기 까다로움. 속도가 느리고 영상 가장자리 pixel에서 상호작용 개수가 줄어드는 대칭점 깨짐 문제.
- 
