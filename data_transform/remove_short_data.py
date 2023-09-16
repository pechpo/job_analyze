from transformers import AutoTokenizer, AutoModel
from tqdm import tqdm

f = open("data3.txt", "r", encoding="utf-8")
raw_data = f.read().split("\n")
f.close()
data = []

for text in tqdm(raw_data):
    if len(text) <= 8:
        continue
    data.append(text + "\n")

f = open("data4.txt", "w", encoding="utf-8")
f.writelines(data)
f.close()