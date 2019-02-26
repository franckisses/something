# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      china_poem
   Description :     
   Author :         gongyan
   Date：           2019/2/26
   Change Activity: 2019/2/26 16:15
-------------------------------------------------
"""
import json
import random

import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup


def getpage(url,num):
    headers = {
        'User-Agent': UserAgent().chrome
    }
    response = requests.get(url, headers=headers)
    text = response.text
    soup = BeautifulSoup(text, 'lxml')
    titles = soup.select('p a b')
    author_dynasty = soup.find_all('p', attrs={'class': 'source'})
    poems = soup.find_all('div',attrs={'class': 'contson'})
    for i in range(10):
        item = {}
        item['title'] = titles[i].text
        item['dynasty'], item['author'] = author_dynasty[i].text.split("：")
        item['poem'] = poems[i].text.strip()
        with open('poem.json','a+',encoding='utf-8')as f:
            f.write(json.dumps(item,ensure_ascii=False)+"\n")
            print(item)
    print('完成了第%d页抓取'%num)


def main():
    for i in range(2, 11):
        baseurl = 'https://www.gushiwen.org/default_{}.aspx'
        url = baseurl.format(i)
        print('现在开始准备抓取第%d页古诗'%i)
        getpage(url,i)



if __name__ == '__main__':
    main()