# _*_ coding: utf-8 _*_
"""
-------------------------------------------------
   File Name：     requests_post
   Description :
   Author :       gongyan
   date：          2019/1/4
   Change Activity:2019/1/4 16:58:
-------------------------------------------------
"""

import requests


data = {
    'name': 'bob'
}

resp = requests.post('http://httpbin.org/post', data=data)
print(resp.text)
