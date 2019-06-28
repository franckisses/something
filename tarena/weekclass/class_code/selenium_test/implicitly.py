# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     implicitly
   Description :  this file just for implicitly!
   Author :       gongyan
   date：          2019/1/21
   Change Activity:2019/1/21 16:47:
-------------------------------------------------
"""
from selenium import webdriver

web = webdriver.Chrome()
#隐式等待，在执行selenium测试的时候。将会在一直等待。如果selenium没有找到对应的dom对象。
# 将继续等待，超出设定的时间后，则抛出找不到节点的异常。
web.implicitly_wait(10)
web.get('http://www.zhihu.com/explore')
input_ = web.find_element_by_class_name('zu-top-add-questio')
print(input_)