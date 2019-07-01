# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 16:14:26 2018

@author: gongyan
"""
#设置代理
import requests

proxies = {
        'http':'http://10.10.1.10:3128',
        'htpps':'http://101.10.12.231:3219'
        }

try:
    response = requests.get('http://www.taobao.com',proxies=proxies,timeout=3)
except error as e:
    print('timeout')
print(response.text)


print('')