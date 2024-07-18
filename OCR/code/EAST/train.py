import os
import os.path as osp
import time
import math
from datetime import timedelta
from argparse import ArgumentParser

import torch
from torch import cuda
from torch.utils.data import DataLoader
from torch.optim import lr_scheduler
from tqdm import tqdm

from east_dataset import EASTDataset
from dataset import SceneTextDataset, PickleDataset
from model import EAST


def parse_args():
    parser = ArgumentParser()

    # Conventional args
    parser.add_argument('--data_dir', type=str,default='/workspace/ojt/OCR/dataset/data/add/pickle')
    parser.add_argument('--model_dir', type=str, default=os.environ.get('SM_MODEL_DIR', 'trained_models'))
    parser.add_argument('--image_size', type=int, default=6400)
    parser.add_argument('--input_size', type=int, default=6400)
    parser.add_argument('--batch_size', type=int, default=16)
    parser.add_argument('--learning_rate', type=float, default=0.0001)
    parser.add_argument('--max_epoch', type=int, default=50)
    parser.add_argument('--ignore_tags', type=list, default=['masked', 'excluded-region', 'maintable', 'stamp'])

    args = parser.parse_args()

    if args.input_size % 32 != 0:
        raise ValueError('`input_size` must be a multiple of 32')

    return args


def do_training(data_dir, model_dir, image_size, input_size, batch_size, learning_rate, max_epoch, ignore_tags):

    # Dataset
    # train_dataset = SceneTextDataset(
    #     data_dir,
    #     split='train',
    #     image_size=image_size,
    #     crop_size=input_size,
    #     ignore_tags=ignore_tags,
    #     color_jitter=False
    # )
    # train_dataset = EASTDataset(train_dataset)
    train_dataset = PickleDataset(data_dir)
    num_batches = math.ceil(len(train_dataset) / batch_size)

    # DataLoader
    train_loader = DataLoader(
        train_dataset,
        batch_size=batch_size,
        shuffle=True
    )

    # 장치
    device = torch.device("cuda:1" if torch.cuda.is_available() else "cpu")
    # 모형
    model = EAST()
    #model.load_state_dict(torch.load('/workspace/ojt/OCR/EAST/trained_models/all_latest3.pth'))
    model.to(device)

    # 최적화 함수
    optimizer = torch.optim.AdamW(model.parameters(), lr=learning_rate)
    scheduler = lr_scheduler.MultiStepLR(optimizer, milestones=[max_epoch // 2], gamma=0.1)

    # 학습
    model.train()
    # 손실 초기화
    best_loss = float('inf')
    # 조기 종료
    patience = 5
    i = 1
    for epoch in range(max_epoch):
        epoch_loss, epoch_start = 0, time.time()
        with tqdm(total=num_batches) as pbar:
            for img, gt_score_map, gt_geo_map, roi_mask in train_loader:
                pbar.set_description('[Epoch {}]'.format(epoch + 1))

                # 출력
                loss, extra_info = model.train_step(img, gt_score_map, gt_geo_map, roi_mask)

                # 역전파
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()
            

                # 손실 저장
                loss_val = loss.item()
                epoch_loss += loss_val

                pbar.update(1)
                val_dict = {
                    'Cls loss': extra_info['cls_loss'], 'Angle loss': extra_info['angle_loss'],
                    'IoU loss': extra_info['iou_loss']
                }
                pbar.set_postfix(val_dict)

        scheduler.step()
        mean_loss = epoch_loss / num_batches
        print('Mean loss: {:.4f} | Elapsed time: {}'.format(mean_loss, timedelta(seconds=time.time() - epoch_start)))
        
        # Model checkpoint
        if mean_loss < best_loss:
            # If no folder, make a folder
            if not osp.exists(model_dir):
                os.makedirs(model_dir)

            # 가중치 경로
            ckpt_fpath = osp.join(model_dir, 'pickle_train_add.pth')
            # 가중치 저장
            torch.save(model.state_dict(), ckpt_fpath)
            best_loss = mean_loss
            print('가중치를 저장합니다')
            # 조기 종료 초기화
            i = 0
        # # 조기 종료
        # else:
        #     i += 1
        #     if i == patience:
        #         print('학습을 조기 종료합니다')
        #         break



def main(args):
    print('학습을 시작합니다\n')
    do_training(**args.__dict__)
    print('\n학습이 종료되었습니다')


if __name__ == '__main__':
    args = parse_args()
    main(args)
