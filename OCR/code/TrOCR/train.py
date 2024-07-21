import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"

import argparse
from omegaconf import OmegaConf
import random
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
from pynvml import *

import torch
from torch.utils.data import Dataset, DataLoader
from PIL import Image
from transformers import VisionEncoderDecoderModel, AutoTokenizer, TrOCRProcessor
from dataset import OCRDataset
from datasets import load_metric
import evaluate
from transformers import AdamW
from tqdm import tqdm
import gc
gc.collect()


def main(configs):

    # 사전 학습 모형 불러오기
    model = VisionEncoderDecoderModel.from_pretrained("team-lucid/trocr-small-korean")
    tokenizer = AutoTokenizer.from_pretrained("team-lucid/trocr-small-korean")
   
    # 장치
    device = torch.device(configs['device'] if torch.cuda.is_available() else 'cpu') 

    # Load dataframe
    df=pd.read_csv(configs['data']['train_csv_dir'])
    df.drop(['id'],axis=1,inplace=True)
    df.img_path=df.img_path.apply(lambda x: x.lstrip('./'))

    # Holdout
    df['len'] = df['label'].str.len()
    train_v1 = df[df['len']==1]

    df = df[df['len']>1]
    train_v2, val, _, _ = train_test_split(df, df['len'], test_size=configs['data']['valid_rate'])
    train = pd.concat([train_v1, train_v2])

    train_df=train.drop('len',axis=1)
    test_df=val.drop('len',axis=1)

    train_df.reset_index(drop=True, inplace=True)
    test_df.reset_index(drop=True, inplace=True)

    # 전처리
    processor = TrOCRProcessor.from_pretrained("team-lucid/trocr-small-korean")
    # 문장 최대 길이
    max_length = configs['max_length']
    # Dataset
    trainset = OCRDataset(
        df=train_df,
        tokenizer=tokenizer,
        processor=processor,
        max_target_length=max_length
    )
    testset = OCRDataset(
        df=test_df,
        tokenizer=tokenizer,
        processor=processor,
        max_target_length=max_length
    )

    print("Number of training examples:", len(trainset))
    print("Number of validation examples:", len(testset))

    # 모형 초매개변수
    model.config.decoder_start_token_id = tokenizer.cls_token_id
    model.config.pad_token_id = tokenizer.pad_token_id
    model.config.vocab_size = model.config.decoder.vocab_size


    model.config.eos_token_id = tokenizer.sep_token_id
    model.config.max_length = max_length
    model.config.early_stopping = True
    model.config.no_repeat_ngram_size = 3
    model.config.length_penalty = 2.0
    model.config.num_beams = 4

    model.tokenizer = tokenizer
    model.to(device)
   
    # 평가 지표
    cer_metric = load_metric("cer")

    train_dataloader = DataLoader(trainset, batch_size=configs['train']['batch_size'], shuffle=True)
    eval_dataloader = DataLoader(testset, batch_size=configs['train']['batch_size'])

    # 학습 인자
    epochs = configs['train']['epochs']
    learning_rate = configs['train']['learning_rate']
    optimizer = AdamW(model.parameters(), lr=learning_rate)
    model.load_state_dict(torch.load('/workspace/ojt/OCR/TrOCR/save_point_10.pth'))
    best_loss = float('inf')
    for epoch in range(1,epochs+1):  # loop over the dataset multiple times
        # train
        model.train()
        train_loss = 0.0
        for i, batch in enumerate(tqdm(train_dataloader)):
            # get the inputs
            for k,v in batch.items():
                batch[k] = v.to(device)

            # forward + backward + optimize
            outputs = model(**batch)
            loss = outputs.loss
            loss.backward()
            optimizer.step()
            optimizer.zero_grad()

            train_loss += loss.item()
            if i % 100 == 0: print(f"Loss: {loss.item()}") 

        if train_loss < best_loss:
            best_loss = train_loss
            torch.save(model.state_dict(), f'./save_point_{epoch+10}.pth')
            print('모형 저장')
        print(f"Loss after epoch {epoch}:", train_loss/len(train_dataloader))

    
    



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str, default='./configs/train.yaml')
    args = parser.parse_args()
    with open(args.config, 'r') as f:
        configs = OmegaConf.load(f)
    main(configs=configs)