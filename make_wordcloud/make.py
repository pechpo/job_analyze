from wordcloud import WordCloud

f = open("word_count.txt", "r", encoding="utf-8")
a = f.read().splitlines()
f.close()
data = {}
for line in a:
    word, count = line.split(" ")
    count = int(count)
    if count < 6:
        break
    data[word] = count
#print(data)
wordcloud = WordCloud(font_path="./shs.ttc", background_color="white"
                    , width=2000, height=1000
                    , min_font_size=30, max_font_size=100
                    , relative_scaling=0.1, max_words=216).fit_words(data)
wordcloud.to_file("./image.png")