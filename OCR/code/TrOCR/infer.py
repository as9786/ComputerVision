import argparse
from omegaconf import OmegaConf

from glob import glob
from PIL import Image
from tqdm import tqdm
import pandas as pd

import torch
from transformers import VisionEncoderDecoderModel, AutoTokenizer, TrOCRProcessor

def main(configs):

    # 장치
    device = torch.device(configs['device'])

    # 모형
    model = VisionEncoderDecoderModel.from_pretrained("team-lucid/trocr-small-korean").to(device)

    # 전처리
    processor = TrOCRProcessor.from_pretrained("team-lucid/trocr-small-korean")
    tokenizer = AutoTokenizer.from_pretrained('team-lucid/trocr-small-korean')

    # 가중치 불러오기
    if configs['checkpoint'] is not None:
        model.load_state_dict(torch.load(configs['checkpoint']))

    # 추론할 사진
    if not configs['infer_dir'].endswith('/'):
        infer_dir = configs['infer_dir'] + '/'
    else:
        infer_dir = configs['infer_dir']

    imgs = sorted(glob(infer_dir+'*'))

    results = []
    print('추론을 시작합니다.')
    for img_path in tqdm(imgs):
        img = Image.open(img_path).convert('RGB')
        pixel_values =(processor(img,return_tensors='pt').pixel_values).to(device)
        generated_ids1 = model.generate(pixel_values)
        generated_text1 = tokenizer.batch_decode(generated_ids1, skip_special_tokens=True)[0]
        results.append(generated_text1)

    print('결과를 저장합니다.')

    df = pd.DataFrame({'img_path' : imgs, 'preds' : results})
    df.to_csv(configs['output_path'],index=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str, default='./configs/infer.yaml')
    args = parser.parse_args()
    with open(args.config, 'r') as f:
        configs = OmegaConf.load(f)
    main(configs=configs)

    

    