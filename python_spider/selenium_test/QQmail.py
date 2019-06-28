# _*_ coding: utf-8 _*_
"""
-------------------------------------------------
   File Name：     QQmail
   Description :   qqmail login
   Author :       gongyan
   date：          2019/1/9
   Change Activity:2019/1/9 11:17:
-------------------------------------------------
"""
from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://mail.qq.com/')
# switch_to_login = browser.find_element_by_class_name('switch_btn_focus')
# switch_to_login.click()

iframe = browser.find_element_by_xpath('//iframe[@id="login_frame"]')# 找到“嵌套”的iframe
# print(iframe)
# browser.switch_to.frame(iframe)
browser.switch_to.frame(iframe)
switch_to_login = browser.find_element_by_class_name('switch_btn_focus')
switch_to_login.click()
# time.sleep(10)
# browser.close()