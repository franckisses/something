# _*_ coding: utf-8 _*_
"""
-------------------------------------------------
   File Name：     qiushibaike
   Description :
   Author :       gongyan
   date：          2019/1/7
   Change Activity:2019/1/7 19:29:
-------------------------------------------------
"""
import requests
import time
import sys,io
from lxml import etree


sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='GB18030')


def get_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'

    }
    response = requests.get(url,headers=headers)
    text = response.text
    html = etree.HTML(text)
    content = html.xpath('//div[@class="content"]/span/text()')
    for each_content in content:
        print(each_content)


if __name__ == '__main__':
    for i in range(10):
        url = 'https://www.qiushibaike.com/text/page/{}/'.format(i+1)
        get_page(url)
        break