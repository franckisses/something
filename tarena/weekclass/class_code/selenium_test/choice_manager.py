# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     choice_manager
   Description :
   Author :       gongyan
   date：          2019/1/21
   Change Activity:2019/1/21 17:58:
-------------------------------------------------
"""
from selenium import webdriver
import time

web = webdriver.Chrome()

web.get('http://www.baidu.com')
web.execute_script('window.open()')
print(web.window_handles)
web.switch_to_window(web.window_handles[1])
web.get('http://www.taobao.com')
time.sleep(3)
# web.execute_script('window.open()')
# web.switch_to_window(web.window_handles[2])
# web.get('http://python.org')

web.switch_to_window(web.window_handles[0])
time.sleep(2)
web.switch_to_window(web.window_handles[1])
time.sleep(1)
web.switch_to_window(web.window_handles[0])
# web.switch_to_window(web.window_handles[2])
time.sleep(2)
web.switch_to_window(web.window_handles[0])
print(web)
# web.switch_to_window(web.window_handles[2])
print(web.window_handles)
web.close()
print(web)