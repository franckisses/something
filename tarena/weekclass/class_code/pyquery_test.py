# -*- coding:utf-8 -*-
from pyquery import PyQuery as pq
#this file just for the test the pyquery

html = '''
<div class=‘content’>
    <ul id = 'haha'>
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
</div>'''

#初始化
doc = pq(html)

#查找标签
# print(doc('li'))
# print(doc('ul'))


# url初始化
# doc1 = pq(url='http://www.cn.bing.com')
# print(doc1('title'))

# 文件初始化
# doc2 = pq(filename='index.html')
# print(doc2('title'))

# 基本的CSS选择器
# 1 根据id去选择
# idElement = doc('#haha')
# print(idElement)

#根据class属性去选择
# classElement = doc(".item-0")
# print(classElement)

#根据标签的关系去选择
# sons = doc("#haha li")
# print(sons)

# 多个元素的查找
# lilist = doc('li').items()
# print(type(lilist))
# for i  in lilist:
#     print(i)
# 
#获取属性
# aElement = doc('.item-0.active a')
# print(aElement.attr('href'))
# print(aElement.attr.href)

# 获取文本
# text = doc('.item-0.active a span')
# print(text.html())
# text的方法是将此标签下的所有的文本都能匹配出来
# print('===='*20)
# print(text.text())


#根据固定的内容去找标签
#找到含有second的li标签
print(doc("li:contains('second')"))
