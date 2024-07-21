import argparse
from omegaconf import OmegaConf

from glob import glob
import matplotlib.pyplot as plt
from PIL import Image
import cv2
import numpy as np
from tqdm import tqdm
from sklearn.model_selection import train_test_split
import json
import os

from ultralytics import YOLO

def main(configs):

    if configs['resume'] == False:

        # 모형 불러오기
        model = YOLO(configs['model_name'])

        #학습
        results = model.train(
            data=configs['data_yaml'],
            epochs=configs['train']['epochs'],
            imgsz=configs['train']['image_size'],
            batch=configs['train']['batch_size'],
            name=configs['save_name'],
            optimizer="Adam",
            device=3,
            momentum=0.99,
            save_period=1,
            patience=configs['train']['patience'],
            amp=True,
            lr0=configs['train']['learning_rate'],
            exist_ok=True,
            cls=1,
            workers=0,
            degrees = 90,
            shear = 30,
            flipud = 0.5,
            mixup = 0.5,
            copy_paste = 0.5
        )

    else:
        # 학습 중이던 모형 불러오기
        model = YOLO('/workspace/ojt/OCR/YOLO/runs/detect/best_yolov8n_add/weights/last.pt')
        # 이어서 학습
        results = model.train(resume=True)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str, default='./configs/train.yaml')
    args = parser.parse_args()
    with open(args.config, 'r') as f:
        configs = OmegaConf.load(f)
    main(configs=configs)