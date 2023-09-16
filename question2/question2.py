from transformers import AutoTokenizer, AutoModel
from tqdm import tqdm

tokenizer = AutoTokenizer.from_pretrained("../../model", trust_remote_code=True)
model = AutoModel.from_pretrained("../../model", trust_remote_code=True, device='cuda')
model = model.eval()

f = open("../data.txt", "r", encoding="utf-8")
data = f.read().split("\n")
f.close()

#m = {}

f = open("anxiety_val.txt", "w", encoding="utf-8")
for text in tqdm(data):
    prompt = '阅读这段话：“' + text + '”，这段话对于就业的焦虑度为多少？输出一个1到5的数字，只输出数字本身'
    #print(prompt)
    response, history = model.chat(tokenizer, prompt, history=[])
    #print(response)
    flag = "-1"
    for ch in response:
        if ch.isdigit() == True:
            #m[int(ch)] = m.get(int(ch), 0) + 1
            flag = ch
            break
    f.write(flag + "\n")

f.close()