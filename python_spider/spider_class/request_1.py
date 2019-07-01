# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 16:23:49 2018

@author: gongyan
"""

import requests

data = {
        'name':'xiaozhang',
        'age':'24'
        }
response = requests.get('http://httpbin.org/get',params=data)
print(response.text)
print(type(response.text))

