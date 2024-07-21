from ultralytics import YOLO
from argparse import ArgumentParser

def parse_args():
    parser = ArgumentParser()

    # Conventional args
    parser.add_argument('--model_path', type=str,required=True)
    parser.add_argument('--yaml_path', type=str,required=True)
    args = parser.parse_args()

    return args


def main(model_path, yaml_path):

    model = YOLO(model_path)
    metrics = model.val(data=yaml_path, workers=0)

if __name__ == '__main__':
    args = parse_args()
    main(**args.__dict__)

