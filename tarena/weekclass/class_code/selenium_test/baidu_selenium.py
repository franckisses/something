# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     baidu_selenium
   Description :
   Author :       gongyan
   date：          2019/1/21
   Change Activity:2019/1/21 11:14:
-------------------------------------------------
"""
from selenium import webdriver
import time


web = webdriver.Chrome()
web.get('http://cn.bing.com')

#查找输入框事件
#通过id属性来查找
inputElement = web.find_element_by_id('sb_form_q')
#通过name属性来查找
# inputElement = web.find_element_by_name('q')

#填充查找内容事件
inputElement.send_keys('百度指数')

time.sleep(3)
#清空输入的内容
inputElement.clear()
#填充新的内容
inputElement.send_keys('python')

# 模拟点击事件
clickElement = web.find_element_by_name('go')
#模拟点击
clickElement.click()