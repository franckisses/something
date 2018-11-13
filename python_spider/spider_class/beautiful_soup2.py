# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     beautiful_soup2
   Description :
   Author :       gongyan
   date：          2018/11/13
   Change Activity:2018/11/13 10:17:
-------------------------------------------------
"""

from bs4 import BeautifulSoup

html = """
<html><head><title>The dormouse's story</title></head>
<body>
<p class='story'>once upon a time there were three little sisters,and there name were
<a href='http://example.com/elise' class='sister' id='link1'><!-- elsie--></a>
<a href='http://example.com/lacie' class='sister' id='link2'>lacie</a>and
<a href='http://example.com/title' class='sister' id='link3'>Tillie</a>
and they lived at the bottom of a well.</p>
<p class='story'>...</p>
"""
soup = BeautifulSoup(html,'lxml')

# 关联选择 选择包含的所有的子节点  contents
# print(soup.p.contents)
# for i,child in enumerate(soup.p.contents):  #只要包含在标签内的元素都算 空格也算
#     print(i,child)

# 查找所有的子孙节点 descendants
# print(soup.p.descendants)
# for i,children in enumerate(soup.p.descendants):
#     print(i,children)

# 查找父节点和祖先节点
# print(soup.a.parent)  #查找a的父节点

# 查找a节点的祖先节点
# print(soup.a.parents) #<generator object parents at 0x00000000035CB678> 是一个迭代器
# print(list(enumerate(soup.a.parents)))

# 查找兄弟节点
# print(soup.a.next_sibling)  #查找a节点的下一个弟弟节点
# print(soup.a.previous_sibling) #查找a节点的上一个哥哥节点

# next_siblings 和previous_siblings 分别查找其所有的兄弟节点


