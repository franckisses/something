# _*_ coding: utf-8 _*_
"""
-------------------------------------------------
   File Name：     maoyan
   Description :   this is for maoyan spider.
   Author :       gongyan
   date：          2019/1/9
   Change Activity:2019/1/9 17:48:
-------------------------------------------------
"""
import requests
from lxml import etree
import json,time


def get_page(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    response = requests.get(url,headers=headers)
    text = response.text
    html = etree.HTML(text)
    title = html.xpath('//dd/div/div/div[1]/p[1]/a/text()')
    actor = html.xpath('//dd/div/div/div[1]/p[2]/text()')
    pub_time = html.xpath('//dd/div/div/div[1]/p[3]/text()')
    first_num = html.xpath('//dd/div/div/div[2]/p/i[1]/text()')
    last_num = html.xpath('//dd/div/div/div[2]/p/i[2]/text()')
    print(actor)
    print(pub_time)

    for i in range(10):
        items = {}
        items['title'] = title[i]
        items['score'] = first_num[i]+last_num[i]
        items['actor'] = actor[i].strip()
        items['pub_time'] = pub_time[i]
        with open('maoyan.json', 'a+') as f:
            f.write(json.dumps(items, ensure_ascii=False) + '\n')



if __name__ == '__main__':
    for i in range(0,100,10):
        url = 'https://maoyan.com/board/4?offset={}'.format(i)
        get_page(url)
        time.sleep(5)
        # save_data(items)