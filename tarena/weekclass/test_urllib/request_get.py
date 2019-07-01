# _*_ coding: utf-8 _*_
"""
-------------------------------------------------
   File Name：     request_get
   Description :
   Author :       gongyan
   date：          2019/1/7
   Change Activity:2019/1/7 9:24:
-------------------------------------------------
"""
import requests
import os,sys
from urllib import request,parse

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
R = requests.get('http://www.baidu.com', headers=headers)
# print(R.text)


key = '壁纸'

url = 'http://www.baidu.com/s?wd='+parse.quote(key)
print(url)