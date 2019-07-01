# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 14:27:15 2018

@author: gongyan
"""

import urllib.request


#我们在这里设置的请求超时为1秒，即时间超过1秒之后，服务器没有给出响应，则会抛出异常。

#应用：我们可以用超时来设置控制一个网页的访问时间，如果没有响应我们可以跳过这个区抓取
#其他的
response = urllib.request.urlopen('http://httpbin.org',timeout=1)
print(response.read())