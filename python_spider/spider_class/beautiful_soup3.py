# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     beautiful_soup3
   Description :
   Author :       gongyan
   date：          2018/11/13
   Change Activity:2018/11/13 11:14:
-------------------------------------------------
"""
from bs4 import BeautifulSoup
import re

html = """
<div class="panel">
        <div class="panel-heading">
            <h4>hello</h4>
        </div>
        <div class="panel-body">
            <ul class="list" id="list-1" name="elements">
                <li class="element">Foo</li>
                <li class="element">Bar</li>
                <li class="element">Jay</li>
            </ul>
            <ul class="list list-small" id="list-2">
                <li class="element">Foo</li>
                <li class="element">Bar</li>
            </ul>
            <a> hello.this is a link</a>
        </div>
</div>

"""

soup = BeautifulSoup(html,'lxml')
print(type(soup))
# 提取信息
# 方法选择器find_all（） 匹配所有的
# 查找节点

# print(soup.find_all(name='ul'))  #查找所有的ul标签
# print(type(soup.find_all(name='ul')[0])) #查看元素的类型

# 查找属性
# print(soup.find_all(attrs={'id':'list-1'}))
# print(soup.find_all(attrs={'class':'element'}))

# 匹配文本 会匹配出包含所有检索内容的所有文本
# print(soup.find_all(text=re.compile('link')))


# 方法find（） 返回的不在是列表的形式，而是一个（单个元素）节点元素，类型依然是tag类型的
# print(soup.find(id='list-2'))

# 其他的补充：
# find_parents()   返回所有的祖先节点 find_parent() 返回直接的父节点
# find_next_siblings()  返回后面所有的兄弟节点  find_next_sibling() 返回后面第一个兄弟节点
# find_previous_siblings() 返回前面所有的兄弟节点  find_previous_sibling()  返回前面的第一个兄弟节点

# CSS选择器 通过select方法来实现
# 获取前一个选择器之下的选择器 两者是包含关系
# print(soup.select('.panel .panel-heading'))
# print(soup.select('ul li'))
# print(soup.select('#list-2 .element'))

# 获取属性
# for ul in soup.select('ul'):
#     print(ul['id'])  #可以直接的去输入标签然后再去选择属性
#     print(ul.attrs['id'])  #可以去通过attrs来选择属性

# 获取文本
# for li in soup.select('li'):
#     print("get_text():",li.get_text())
#     print('string:',li.string)
