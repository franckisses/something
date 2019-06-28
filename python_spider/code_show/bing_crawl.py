# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     bing_crawl
   Description :
   Author :       gongyan
   date：          2018/11/17
   Change Activity:2018/11/17 14:24:
-------------------------------------------------
"""
import requests
from bs4 import BeautifulSoup
import os
import datetime


def get_page(url,headers):
    response = requests.get(url,headers=headers)
    # 由于网页中有特殊字符，将版权符号的&替换
    html = response.text.replace('&','')

    # 创建soup对象
    soup = BeautifulSoup(html,'lxml')
    # 找到文档中所有的img标签
    img_list = soup.find_all('img')
    for index,i in enumerate(img_list):
        # 匹配src属性
        src = i.attrs['src'].replace('-listpic','')
        # 调用下载图片的函数
        download_pic(index,src,headers)


def download_pic(index,src,headers):
    if not os.path.isdir('%s' % datetime.datetime.now().strftime('%Y-%m-%d')):
        os.makedirs('%s' % datetime.datetime.now().strftime('%Y-%m-%d'))
    fileName = r'.\\%s\\'% datetime.datetime.now().strftime('%Y-%m-%d')+str(index)+'.jpg'
    images = requests.get(src,headers)
    img = images.content
    if images.status_code == 200:
        with open(fileName, 'wb') as fp:
            fp.write(img)


if __name__ == '__main__':
    url = 'http://bing.plmeizi.com/?page=1'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) ' \
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
    }
    get_page(url,headers)
