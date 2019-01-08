# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     tencent_wanted
   Description :
   Author :       gongyan
   date：          2018/11/26
   Change Activity:2018/11/26 17:20:
-------------------------------------------------
"""
import time
from bs4 import BeautifulSoup
import requests


def get_page(url,headers):
    response = requests.get(url,headers)
    html = response.text
    soup = BeautifulSoup(html,'lxml')
    print(html)
    position = soup.select('.even')
    position1 = soup.select('.odd')



if __name__ == '__main__':
    url = 'https://hr.tencent.com/position.php?&start={}#a'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }
    for i in range(0,2861,10):
        page_url = url.format(i)
        time.sleep(1)
        get_page(url,headers)
        break
