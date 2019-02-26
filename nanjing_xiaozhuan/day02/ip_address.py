# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      ip_address
   Description :     
   Author :         gongyan
   Date：           2019/2/26
   Change Activity: 2019/2/26 15:53
-------------------------------------------------
"""
import requests

# 本地ip ip =58.213.152.85
# 194.156.230.164
#47.100.252.189
#114.24.129.141

url = 'https://www.httpbin.org/get'

response = requests.get(url)

print(response.text)
