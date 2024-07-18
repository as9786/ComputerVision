import pickle
from tqdm import tqdm
import os
import os.path as osp
from argparse import ArgumentParser

from east_dataset import EASTDataset
from dataset import SceneTextDataset

import albumentations as A

def parse_args():
    parser = ArgumentParser()

    # Conventional args
    parser.add_argument('--data_dir', type=str,default='/workspace/ojt/OCR/dataset/data/add/')
    parser.add_argument('--pkl_dir', type=str, default='pickle')
   
    args = parser.parse_args()

    return args

def main(data_dir,pkl_dir):

    ignore_tags = ['masked', 'excluded-region', 'maintable', 'stamp']
    
    os.makedirs(osp.join(data_dir, pkl_dir), exist_ok=True)

    train_dataset = SceneTextDataset(
                root_dir=data_dir,
                split='train',
                image_size=4800,
                crop_size=4800,
                ignore_tags=ignore_tags,
                color_jitter=False,
                normalize=True
            )

    train_dataset = EASTDataset(train_dataset)

    ds = len(train_dataset)
    for k in tqdm(range(ds)):
        data = train_dataset.__getitem__(k)
        with open(file=osp.join(data_dir, pkl_dir, f"{k}.pkl"), mode="wb") as f:
            pickle.dump(data, f)

if __name__ == '__main__':
    args = parse_args()
    main(args.data_dir, args.pkl_dir)