# Fast Fourier Convolution

## 서론
- 두 가지 고려
1. 합성곱 신경망에서 중요한 수용 영역
2. Chain-like topology
- Non-local receptive field를 가지면 multi-scale information을 사용할 수 있는 방법 고안
- 이 때, 중요한 것은 spectral transform theory
- Fourier transform을 이용한 non-local을 만듦
- FFC는 아무것도 수정하지 않고 기존의 합성곱을 대체할 수 있음
- 
