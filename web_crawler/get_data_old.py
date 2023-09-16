import requests
from bs4 import BeautifulSoup as bs
from time import sleep
from tqdm import tqdm

headers = {
    'authority': 's.weibo.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'max-age=0',
    'cookie': 'login_sid_t=5369389c56800e979409c3fc6e2899ff; cross_origin_proto=SSL; _s_tentry=passport.weibo.com; Apache=343782081940.3803.1694690460594; SINAGLOBAL=343782081940.3803.1694690460594; ULV=1694690460598:1:1:1:343782081940.3803.1694690460594:; SUB=_2A25IBpyCDeRhGeFK7lcS8SbIwziIHXVrdYlKrDV8PUNbmtAGLUTAkW9NQ1GpjUvatNiRW06rn_fqb8tIQlZNftjg; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWN_5AfT4BnvsmrwCWGcdez5JpX5KzhUgL.FoMXSK-0eKnX1hB2dJLoI7979gSQMsYt; ALF=1726226514; SSOLoginState=1694690516',
    'referer': 'https://s.weibo.com/realtime?q=%E6%89%BE%E5%B7%A5%E4%BD%9C&rd=realtime&tw=realtime&Refer=weibo_realtime&page=50',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Microsoft Edge";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.81',
}

params_template = (
    ('q', '211 \u5C31\u4E1A'),
    ('rd', 'realtime'),
    ('tw', 'realtime'),
    ('Refer', 'weibo_realtime'),
    ('page', '1'),
)

texts = []

for page in tqdm(range(1, 51)):
    params = params_template[0:4] + (('page', str(page)), )
    #print(params)
    response = requests.get('https://s.weibo.com/realtime', headers=headers, params=params)
    #print(response.status_code)
    #print(response.headers)
    f = open("data.html", "wb")
    f.write(response.content)
    f.close()
    soup = bs(open("data.html", "r", encoding="utf-8"), features="html.parser")
    main_div = soup.html.body.find("div", class_="m-main")
    msg_list = main_div.div.find("div", class_="woo-box-flex").div.div
    #msg_list = main_div.div.find("div", class_="woo-box-flex").div.find_all("div")[1]
    for panel in msg_list.contents:
        if panel is None:
            continue
        #print(str(type(panel)))
        if (str(type(panel))=="<class 'bs4.element.NavigableString'>"):
            continue
        if (str(type(panel))=="<class 'bs4.element.Comment'>"):
            continue
        #print(panel)
        content = panel.div.div.find("div", class_="content").find_all("p")
        if len(content) == 2:
            content = content[1]
        else:
            content = content[0]
        #print(content)
        text = ""
        for part in content:
            if (part.name == "br"):
                text += "。"
            if (str(type(part))!="<class 'bs4.element.NavigableString'>"):
                continue
            text += part
        text = text.strip()
        if len(text) == 0:
            continue
        if text[0] == "。":
            text = text[1:]
        text = text.replace(" ", "，") 
        texts.append(text+"\n")
    sleep(2)
f = open("data_old.txt", "w", encoding="utf-8")
f.writelines(texts)
f.close()