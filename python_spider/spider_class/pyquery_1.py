# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     pyquery_1
   Description :
   Author :       gongyan
   date：          2018/11/13
   Change Activity:2018/11/13 17:08:
-------------------------------------------------
"""
from pyquery import PyQuery as pq

html = """
<div id='container'>
    <ul class='list'>
        <li class="item-0">first item</li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
        <li class="item-1 active"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a></li>
    </ul>
</div>
"""
#完成html字符串的初始化。
# doc = pq(html)
# print(doc('li'))
# print(type(doc('li')))

# 完成对URl的初始化
# doc = pq(url='https://baidu.com',encoding='utf-8')
# print(doc('title'))

# 对文件的初始化
# doc = pq(filename='new.html')
# print(doc('li'))

# 基本CSS选择器
# doc = pq(html)
# print(doc('#container .list li'))
# print(type(doc('#container .list li')))

# 查找节点
# 1.查找子节点
# doc = pq(html)
# items = doc('.list')
# print(items)
# # lis = items.find('li')
# lis = items.children()
# print(lis)

# 2.查找父节点 parent()查找父节点 parents()返回所有的祖先节点
# doc = pq(html)
# items = doc('.list')
# container = items.parent()
# print(container)

# 兄弟节点sibling兄弟节点 siblings()兄弟节点


# 获取属性 只能查找一个
# doc = pq(html)
# a = doc('a')
# print(a.attr.href)

#获取所有的属性要用到遍历
# doc = pq(html)
# a = doc('a')
# for item in a.items():
#     print(item.attr('href'))


# 获取文本
# doc = pq(html)
# a = doc('span')
# print(a.text())