# _*_ coding: utf-8 _*_
"""
-------------------------------------------------
   File Name：     xpath_show
   Description :
   Author :       gongyan
   date：          2019/1/4
   Change Activity:2019/1/4 17:02:
-------------------------------------------------
"""
import requests
from bs4 import BeautifulSoup


def get_page(page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    url = "https://www.gushiwen.org/default_{}.aspx".format(page)
    response = requests.get(url,headers=headers)
    text = response.text
    soup = BeautifulSoup(text,'lxml')
    title_tags = soup.find_all(name='b')
    some_info = soup.find_all(name='p',attrs={'class':'source'})
    poems_tags = soup.find_all(name='div', attrs={'class': 'contson'})
    title = []
    dynasty = []
    author = []
    poems = []
    for head in title_tags:
        title.append(head.text)

    for i in some_info:
        dynasty.append(i.find_all('a')[0].text)
        author.append(i.find_all('a')[1].text)

    for poem in poems_tags:
        poems.append(poem.text.strip())


    for i in range(10):
        poem = title[i]+'#'+dynasty[i]+'#'+author[i]+'#'+poems[i]
        with open('poems.txt','a+',encoding='utf-8') as f:
            f.write(poem+'\n')
    print("the page %s is download over!"%page)

if __name__ == '__main__':
    for i in range(1,20):
        get_page(i)
