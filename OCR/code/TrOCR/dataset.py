from PIL import Image
import torch
from torch.utils.data import Dataset


class OCRDataset(Dataset):
    def __init__(self, df, processor, tokenizer, max_target_length=32):
        self.df = df
        self.processor = processor
        self.max_target_length = max_target_length
        self.tokenizer = tokenizer

    def __len__(self):
        return len(self.df)

    def __getitem__(self, idx):
        # get file name + text
        text = self.df['label'][idx]
        # prepare image (i.e. resize + normalize)
        image = Image.open('./dataset/TextRecognition/ori/' + self.df['img_path'][idx]).convert("RGB")
        pixel_values = self.processor(image, return_tensors="pt").pixel_values
        # add labels (input_ids) by encoding the text
        labels = self.tokenizer(text, padding="max_length",
                                stride=10,
                                truncation=True,
                                max_length=self.max_target_length).input_ids

        # important: make sure that PAD tokens are ignored by the loss function
        #labels = self.tokenizer.encode(text)
        labels = [label if label != self.tokenizer.pad_token_id else -100 for label in labels]

        encoding = {"pixel_values": pixel_values.squeeze(), "labels": torch.tensor(labels)}
  
        return encoding