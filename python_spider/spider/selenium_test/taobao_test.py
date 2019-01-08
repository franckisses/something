# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     taobao_test
   Description :
   Author :       gongyan
   date：          2018/12/24
   Change Activity:2018/12/24 19:51:
-------------------------------------------------
"""
from selenium import webdriver

wb = webdriver.Chrome()

wb.get("http://www.jd.com")

# get_input = wb.find_element_by_id("q")
get_input = wb.find_element_by_id("key")
# get_input.send_keys("拉链")
get_input.send_keys("拉链")

# wb.find_element_by_class_name("btn-search tb-bg").click()
wb.find_element_by_css_selector(".button").click()

ok = wb.find_element_by_xpath("//div[@class='p-img']/a/@title/text()")
print(ok)