# _*_ coding: utf-8 _*_
"""
-------------------------------------------------
   File Name：     jianshu_test
   Description :   this is for test jianshu
   Author :       gongyan
   date：          2019/1/9
   Change Activity:2019/1/9 14:30:
-------------------------------------------------
"""

from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://www.zhihu.com/explore')

logo = browser.find_element_by_id('zh-top-link-logo')
print(logo)
print(logo.get_attribute('class'))

head_text = browser.find_element_by_id('zh-top-link-home')
print(head_text.text)
input = browser.find_element_by_class_name('zu-top-add-question')
print(input.id)
print(input.location)
print(input.tag_name)
print(input.size)
# browser.close()