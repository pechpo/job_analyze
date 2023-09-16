import re

f = open("raw_data.txt", "r", encoding="utf-8")
data = f.read().splitlines()
f.close()
m = {}
for text in data:
    a = re.split('\||;|,|，|；|、', text)
    s = set(a)
    for word in s:
        if len(word) == 0:
            continue
        if word[-1] == "。":
            word = word[0:-1]
        p = word.find("：")
        if p >= 0:
            word = word[p+1:]
        word = word.strip()
        m[word] = m.get(word, 0) + 1
f = open("word_count.txt", "w", encoding="utf-8")
m_order = sorted(m.items(), key=lambda x:x[1], reverse=True)
for pair in m_order:
    f.write(pair[0] + " " + str(pair[1]) + "\n")
f.close()