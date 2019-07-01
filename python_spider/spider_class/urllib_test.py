# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 11:06:04 2018

@author: gongyan
"""

import urllib.parse
import urllib.request

data = bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf-8')
response = urllib.request.urlopen('http://httpbin.org/post',data=data)

print(response.read())
print(type(response.read()))
