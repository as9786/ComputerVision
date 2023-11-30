# TransUNet : Transformers Make Strong Encoders for Medical Image Segmentation

![image](https://github.com/as9786/ComputerVision/assets/80622859/939f16a7-ab6d-4144-abc4-7b0c4fdc9b03)

- ResNet-50 구조를 이용한 후, transformer에 넣은 다음에 U-Net 구조로 upsampling
1. ResNet-50 구조를 가진 합성곱 신경망을 통해 feature map 만듦
2. Feature map을 ViT 구조처럼, patch를 만든 후 linear project
3. 2번에서 나온 결과를 transformer에 입력
4. 3번의 결과의 모양을 1D에서 2D로 바꿈
5. U-Net 구조를 통해 upsampling
- Skip connection
- CNN에서 나온 hidden feature map도 사용
