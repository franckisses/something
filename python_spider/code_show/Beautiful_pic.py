# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Beautiful_pic
   Description :
   Author :       gongyan
   date：          2018/11/16
   Change Activity:2018/11/16 11:03:
-------------------------------------------------
"""
from bs4 import BeautifulSoup

html = '<img src="/az/hprichbg/rb/AliceCentralPark_ZH-CN9031006021_1920x1080.jpg" style="display:none" onload="sc_lI();>'

soup = BeautifulSoup(html,'lxml')
print(soup.img.attrs['src'])