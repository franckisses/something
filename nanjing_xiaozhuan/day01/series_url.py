# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      series_url
   Description :     通过字符串的格式化来生成一系列url
   Author :         gongyan
   Date：           2019/2/25
   Change Activity: 2019/2/25 14:39
-------------------------------------------------
"""
# https://nj.lianjia.com/zufang/pg100/#contentList

url = 'https://nj.lianjia.com/zufang/pg{}/#contentList'
for i in range(1,101):
    print(url.format(i))
    print('--------'*10)
    print('https://nj.lianjia.com/zufang/pg%s/#contentList'%i)
