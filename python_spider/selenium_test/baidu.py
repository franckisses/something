# _*_ coding: utf-8 _*_
"""
-------------------------------------------------
   File Name：     baidu
   Description :
   Author :       gongyan
   date：          2019/1/9
   Change Activity:2019/1/9 10:45:
-------------------------------------------------
"""
from selenium  import webdriver
import time

dirver = webdriver.Chrome()
dirver.get('http://www.baidu.com')
input = dirver.find_element_by_id('kw')
input.send_keys('python')
time.sleep(0.5)
input.clear()
input.send_keys('iPad')
button = dirver.find_element_by_id('su')
button.click()