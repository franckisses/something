# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     handler_error
   Description :
   Author :       gongyan
   date：          2019/1/21
   Change Activity:2019/1/21 18:15:
-------------------------------------------------
"""
from selenium import webdriver
from selenium.common.exceptions import TimeoutException,NoSuchElementException

web = webdriver.Chrome()

try:
    web.get('http://www.google.com')
except TimeoutException:
    print('Time out')

try:
    web.find_element_by_id("hello")
except NoSuchElementException:
    print("No Element")
finally:
    web.close()