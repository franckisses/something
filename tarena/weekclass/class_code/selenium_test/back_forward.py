# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     back_forward
   Description :
   Author :       gongyan
   date：          2019/1/21
   Change Activity:2019/1/21 17:51:
-------------------------------------------------
"""
from selenium import webdriver
import time

web = webdriver.Chrome()
web.get('http://www.baidu.com')
web.get('http://www.jianshu.com')
web.get('http://www.zhihu.com')
web.back()
time.sleep(1)
web.forward()
web.close()

