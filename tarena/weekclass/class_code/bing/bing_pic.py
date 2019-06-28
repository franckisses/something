# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     bing_pic
   Description :   this is  for  python_spider for bing_crawl
   Author :       gongyan
   date：          2019/1/17
   Change Activity:2019/1/17 14:50:
-------------------------------------------------
"""

import requests
from pyquery import PyQuery as pq
import time
from urllib import request


def get_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60'
    }
    response = requests.get(url,headers=headers)
    html = response.text.replace('&','')
    doc = pq(html)
    fonts = doc('font font')
    imgs = doc("img").items()
    for img in imgs:
        src = img.attr('src').replace('-listpic','')
        alt = img.attr('alt').split(' ')[0]
        # alt = img.attr('alt')
        # print(alt)
        try:
            request.urlretrieve(src,"hahah/"+alt+'.jpg')
        except FileNotFoundError as e:
            print(e,src,alt)
        finally:
            print("successfully")
#

if __name__ == '__main__':
    for i in range(1,50):
        url = 'http://bing.plmeizi.com/?page={}'.format(i)
        print(i)
        get_page(url)
        time.sleep(2)