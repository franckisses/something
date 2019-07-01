# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     find_element
   Description :
   Author :       gongyan
   date：          2019/1/21
   Change Activity:2019/1/21 20:49:
-------------------------------------------------
"""
from selenium import webdriver

webObject = webdriver.Chrome()

webObject.get('http://www.dongqiudi.com')

#通过xpath来查找标签
a = webObject.find_element_by_xpath('//*[@id="header"]/div/div[1]/a[2]')
#通过链接的文字来查找标签
b = webObject.find_element_by_link_text('全体起立！懂球帝本周国际赛事MVP提名揭晓')
print("b",b)
#通过链接的关键字来查找标签
c = webObject.find_element_by_partial_link_text('阿森纳官方')
print("c",c)
#通过class的属性来查找标签
d = webObject.find_element_by_class_name('header_left')
print('d',d)
#通过css选择器来查找标签
e = webObject.find_element_by_css_selector('.pc_count')
print("e",e)
#通过id来查找标签
f = webObject.find_element_by_id('live_nav')
print('f',f)
#通过name属性来查找标签
g = webObject.find_element_by_name('baidu_union_verify')
print('g',g)
#通过标签名来查找标签
h = webObject.find_element_by_tag_name('a')
print('h',h)
