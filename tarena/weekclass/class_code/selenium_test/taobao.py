# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     try
   Description :   this file is for selenium show!
   Author :       gongyan
   date：          2019/1/21
   Change Activity:2019/1/21 9:59:
-------------------------------------------------
"""
from selenium import webdriver
import io,sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

web = webdriver.Chrome()
url = 'http://www.taobao.com'
web.get(url)
input_first = web.find_element_by_id('q')
input_second = web.find_element_by_css_selector('#q')
input_third = web.find_elements_by_xpath('//*[@id="q"]')
print(input_first)
print(input_second)
print(input_third)

web.close()