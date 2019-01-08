# _*_ coding: utf-8 _*_
"""
-------------------------------------------------
   File Name：     dongqiudi
   Description :
   Author :       gongyan
   date：          2019/1/7
   Change Activity:2019/1/7 19:54:
-------------------------------------------------
"""
import requests


url = 'http://www.dongqiudi.com/#'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
response = requests.get(url,headers=headers)
print(response.text)