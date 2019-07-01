# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Beautiful_str
   Description :
   Author :       gongyan
   date：          2018/11/16
   Change Activity:2018/11/16 11:03:
-------------------------------------------------
"""
from bs4 import BeautifulSoup


single_str = '<h1 class="l info-h3">大数据运维工程师</h1>'

soup = BeautifulSoup(single_str,'lxml')
print(soup.h1.text)