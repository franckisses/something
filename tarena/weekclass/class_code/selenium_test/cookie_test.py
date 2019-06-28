# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      cookie_test
   Description :    对于cookie的操作
   Author :         gongyan
   Date：           2019/2/28
   Change Activity: 2019/2/28 19:45
-------------------------------------------------
"""
from selenium import webdriver


browser = webdriver.Chrome()

browser.get('http://www.zhihu.com/explore')

print(browser.get_cookies())
browser.delete_all_cookies()
print(browser.get_cookies())