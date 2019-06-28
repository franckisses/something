# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     phantomJS_test
   Description :
   Author :       gongyan
   date：          2019/1/21
   Change Activity:2019/1/21 18:30:
-------------------------------------------------
"""

from selenium import webdriver

web = webdriver.PhantomJS()

web.get('http://www.baidu.com')
print(web.current_url)