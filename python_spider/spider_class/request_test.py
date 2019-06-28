# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 14:47:36 2018

@author: gongyan
"""

from urllib import request,parse

url = 'http://httpbin.org/post'
headers = {
        "User-Agent":"",
        "Host":"httpbin.org"
        }
keyword = {
        "name":"Germany"
        }
data = bytes(parse.urlencode(keyword),encoding='utf-8')
req = request.Request(url=url,data=data,headers=headers,method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8')) 

#另外我们可以用比较高级的方法去添加请求头
req.add_header('User-Agent','Mozilia/4.0(compatible;MSIE 5,5;windows NT)')
