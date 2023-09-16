from transformers import AutoTokenizer, AutoModel
from tqdm import tqdm
import re

tokenizer = AutoTokenizer.from_pretrained("../../model", trust_remote_code=True)
model = AutoModel.from_pretrained("../../model", trust_remote_code=True, device='cuda')
model = model.eval()

f = open("../data.txt", "r", encoding="utf-8")
data = f.read().split("\n")
f.close()

m = {}
for i in range(1, 11):
    m[i] = 0

for text in tqdm(data):
    prompt = '''就业方向包括：
1.国企（烟草、电网、电信局、自来水厂、邮政等）
2.国内私企（阿里、腾讯、华为、京东等）
3.事业单位（医院、学校、研究所等）
4.公务员（通过国考、省考、选调等）
5.外企 (微软、亚马逊、paypal等)
6.升学（读硕士、读博士）
7.创业
8.待业
9.自由职业
10.其他
11.未知
阅读这段话:"''' + text + '"，这段话更偏向于哪种就业方向？只需要回答类别数字。如果不确定，请输出数字11'''
    response, history = model.chat(tokenizer, prompt, history=[])
    a = re.findall("\d+", response)
    #print(a)
    for num in a:
        if int(num) < 1 or int(num) > 10:
            continue
        m[int(num)] += 1

print(m)