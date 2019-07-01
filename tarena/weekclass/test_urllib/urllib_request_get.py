# _*_ coding: utf-8 _*_
"""
-------------------------------------------------
   File Name：     urllib_request_get
   Description :   this is for the get request！
   Author :       gongyan
   date：          2019/1/4
   Change Activity:2019/1/4 15:12:
-------------------------------------------------
"""

import urllib.request

url = 'http://httpbin.org/get'
Request = urllib.request.Request(url)

response = urllib.request.urlopen(Request)
print(response.read().decode('utf-8'))
