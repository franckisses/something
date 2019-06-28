# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 11:13:11 2018

@author: gongyan
"""

import urllib.parse as p

result = p.urlparse('https://blog.csdn.net/jk110333/article/details/9110375')
print(type(result))
print(result[1])
print(result[2])

result1 = p.urlparse('https://www.baidu.com/s?wd=ok&rsv_spt=1&rsv_iqid=0xc24529bd0001a07f&issp=1&f=8&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=98012088_9_dg&rsv_enter=1&rsv_sug3=3&rsv_sug1=3&rsv_sug7=101&rsv_sug2=0&inputT=456&rsv_sug4=1051')
print(result1)

data = ['https','www.baidu.com','index.html','user','a=6','comment']
print(p.urlunparse(data))

print(p.urljoin('https://www.baidu.com','FAQ.html'))


keyword = '壁纸'
url = 'https://www.baidu.com/s?wd='+p.quote(keyword)
print(url)