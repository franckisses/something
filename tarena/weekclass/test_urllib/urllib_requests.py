# _*_ coding: utf-8 _*_
"""
-------------------------------------------------
   File Name：     urllib_requests
   Description :   this file is for test the urllib,and this is a post request
   Author :       gongyan
   date：          2019/1/4
   Change Activity:2019/1/4 14:49:
-------------------------------------------------
"""

import urllib.request,urllib.parse


url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/71.0.3578.98 Safari/537.36',
    'Host': 'httpbin.org'
}

dict = {
    'name': 'bob'
}
data = bytes(urllib.parse.urlencode(dict),encoding="utf8")
req = urllib.request.Request(url=url,data=data,headers=headers,method='POST')
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))
