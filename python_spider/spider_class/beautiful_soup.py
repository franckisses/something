# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     beautiful_soup
   Description :
   Author :       gongyan
   date：          2018/11/13
   Change Activity:2018/11/13 9:43:
-------------------------------------------------
"""
from bs4 import BeautifulSoup

html = """
<html><head><title>The dormouse's story</title></head>
<body>
<p class='tilte' name='dromouse'><b>The dormouse's story</b></p>
<p class='story'> once upon a time there were three little sisters,and there name were 
<a href='http://example.com/elise' class='sister' id='link1'><!-- elsie--></a>
<a href='http://example.com/lacie' class='sister' id='link2'>lacie</a>and
<a href='http://example.com/title' class='sister' id='link3'>Tillie</a>
and they lived at the bottom of a well.</p>
<p class='story'>...</p>
"""


soup = BeautifulSoup(html,'lxml')
# 进行对不标准的字符串进行自动更正,生成完整的html格式
# print(soup.prettify())
# 提取title标签里边的字符串
# print(soup.title.string)

# 选择元素
# print(soup.title)   #打印title的标签的元素
# print(soup.head)    #打印head标签的元素的元素

# 提取信息
# print(soup.title.name) #获取节点的名称

# 获取属性
# print(soup.p.attrs)   #只会提取找到的第一个元素
# print(soup.p['name'])
# print(soup.p['class'])


# 嵌套选择
# <head><title>The dormouse's story</title></head>
# print(soup.head.title)
# print(soup.head.title.string)  #嵌套的选择可以依次去向下选择

