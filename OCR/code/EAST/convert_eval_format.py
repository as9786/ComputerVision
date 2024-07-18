import json
from tqdm import tqdm
from collections import defaultdict

# Convert data for evaluating
def convert_data(preds, answers):
    # Image name

    with open(preds, 'r') as f:
        preds = json.load(f)

    with open(answers, 'r') as t:
        ans = json.load(t)

    imgs_name = list(preds['images'].keys())

    new_preds = defaultdict(list)

    for img_name in tqdm(imgs_name):
        for _, bboxes in preds['images'][img_name]['words'].items():
            new_preds[img_name].append(bboxes['points'])

    
    new_ans = defaultdict(list)

    for img_name in tqdm(imgs_name):
        for _, bboxes in ans['images'][img_name]['words'].items():
            new_ans[img_name].append(bboxes['points'])

    return new_preds, new_ans
