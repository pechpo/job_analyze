from transformers import AutoTokenizer, AutoModel
from tqdm import tqdm

tokenizer = AutoTokenizer.from_pretrained("../../model", trust_remote_code=True)
model = AutoModel.from_pretrained("../../model", trust_remote_code=True, device='cuda')
model = model.eval()

f = open("data2.txt", "r", encoding="utf-8")
raw_data = f.read().split("\n")
f.close()
data = []

for text in tqdm(raw_data):
    #prompt = '阅读这段话：“' + text + '”，请问这段话是否与中国当今大学生就业问题相关？用一个字是/否回答，不要输出多余信息'
    #prompt = '阅读这段话：“' + text + '”，请问这段话是否是广告？用一个字是/否回答，不要输出多余信息'
    #prompt = '阅读这段话：“' + text + '”，请问这段话是否是通知？用一个字是/否回答，不要输出多余信息'
    prompt = '阅读这段话：“' + text + '”，请问这段话是否采用了正式的口吻？用一个字是/否回答，不要输出多余信息'
    response, history = model.chat(tokenizer, prompt, history=[])
    if response[0] != "否":
        continue
    data.append(text + "\n")

f = open("data3.txt", "w", encoding="utf-8")
f.writelines(data)
f.close()