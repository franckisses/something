# _*_ coding: utf-8 _*_
"""
-------------------------------------------------
   File Name：     manage_browser
   Description :   manage_browser_test
   Author :       gongyan
   date：          2019/1/9
   Change Activity:2019/1/9 15:38:
-------------------------------------------------
"""

from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('http://www.baidu.com')
browser.execute_script('window.open()')
print(browser.window_handles)
browser.switch_to_window(browser.window_handles[1])
browser.get('http://www.taobao.com')
time.sleep(1)
browser.switch_to_window(browser.window_handles[0])
browser.get('http://python.org')