# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     easy_spider
   Description :
   Author :       gongyan
   date：          2019/2/25
   Change Activity:2019/2/25 9:03:
-------------------------------------------------
"""
import requests

response = requests.get('http://www.baidu.com')

#查看网站的响应码
print(response.status_code)
#查看网站的代码
# print(response.content)

# [response 200]