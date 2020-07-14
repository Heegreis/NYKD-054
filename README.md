# NYKD-054

## Donwload BERT NER pre-trained model

Link: https://drive.google.com/file/d/14RyCIGGXZFuS_EaGqV-11pCQGnuvpQ5J/view?usp=sharing

## Usage

```ruby
from transformers import AutoModelForTokenClassification, AutoTokenizer
import torch

model = AutoModelForTokenClassification.from_pretrained("./finetune")
tokenizer = AutoTokenizer.from_pretrained("bert-base-chinese")

label_list = ['B-LOC', 'I-LOC', 'O', 'B-PER', 'I-PER', 'B-ORG', 'I-ORG']

sequence = "自称房产幽默大师的王派宏，涉吸金卷款25亿落跑！"
# Bit of a hack to get the tokens with the special tokens
tokens = tokenizer.tokenize(tokenizer.decode(tokenizer.encode(sequence)))
inputs = tokenizer.encode(sequence, return_tensors="pt")
outputs = model(inputs)[0]
predictions = torch.argmax(outputs, dim=2)

print([(token, label_list[prediction]) for token, prediction in zip(tokens, predictions[0].detach().numpy())])

```
