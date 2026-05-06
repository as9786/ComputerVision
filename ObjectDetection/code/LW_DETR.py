# Library
from transformers import pipeline
import requests
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt

# 모형
model = pipeline('object-detection', model='AnnaZhang/lwdetr_small_60e_coco', device_map=0)

# 추론
url = "http://images.cocodataset.org/val2017/000000039769.jpg"
results = model(url)

# 사진 열기
image = Image.open(requests.get(url, stream=True).raw).convert("RGB")
draw = ImageDraw.Draw(image)

# 시각화
for obj in results:
    box = obj["box"]
    label = obj["label"]
    score = obj["score"]

    xmin, ymin, xmax, ymax = box["xmin"], box["ymin"], box["xmax"], box["ymax"]

    # 박스
    draw.rectangle([xmin, ymin, xmax, ymax], outline="red", width=3)

    # 텍스트
    text = f"{label}: {score:.2f}"
    draw.text((xmin, ymin), text, fill="red")

# 출력
plt.imshow(image)
plt.axis("off")
plt.show()
