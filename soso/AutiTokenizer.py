import json
from transformers import AutoTokenizer

with open('./soso/data/dacon_data.json', 'r', encoding='UTF8') as f:
    json_data = json.load(f)

print(json_data)

tokenizer = AutoTokenizer.from_pretrained('bert-base-cased')
read_jsond_data = json_data['instruction']
tokens = tokenizer.tokenize(read_jsond_data)