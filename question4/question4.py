from transformers import AutoTokenizer, AutoModel
from tqdm import tqdm

tokenizer = AutoTokenizer.from_pretrained("../../model", trust_remote_code=True)
model = AutoModel.from_pretrained("../../model", trust_remote_code=True, device='cuda')
model = model.eval()

f = open("../data.txt", "r", encoding="utf-8")
data = f.read().split("\n")
f.close()

#m = {}

f = open("help_val.txt", "w", encoding="utf-8")
for text in tqdm(data):
    prompt = '阅读这段话：“' + text + '”，用长度<=4的词语总结其中对于就业产生焦虑的因素，不要输出句子。'
    #print(prompt)
    response, history = model.chat(tokenizer, prompt, history=[])
    #print(response)
    f.write(response + "\n")

f.close()