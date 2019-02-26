# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      bs4_test
   Description :    这个文件用来展示bs4提取网页文档的信息
   Author :         gongyan
   Date：           2019/2/26
   Change Activity: 2019/2/26 13:45
-------------------------------------------------
"""
from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<img src="https://img1.qunliao.info/fastdfs3/M00/14/9B/ChONolx0zkiAMjojAAEswjWQa3g694.jpg">
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

#创建soup对象
soup = BeautifulSoup(html_doc, 'lxml')
# print(soup)

#可以使代码变得美观，格式化的方法
# print(soup.prettify())

#匹配标签的方法 .匹配即停止
# title =soup.title
# print(title)
#匹配p标签
# print(soup.p)
#匹配head标签
# print(soup.head)


#匹配标签中的文字 1.string 2.text 3.get_text()
# word = soup.title.string
# print(word)
# word1 = soup.title.text
# print(word1)
# word2 = soup.title.get_text()
# print(word2)

#contents 属性 所匹配的标签中包含什么元素都会匹配出来。不管是文本，还是标签
# print(soup.p.contents)

#父节点属性,祖先节点属性
#匹配父节点
# p_parent = soup.p.parent
# print(p_parent)
# print('-'*20)

#匹配祖先节点,包括父节点
# p_parents = soup.p.parents
# print(p_parents)
# for i in p_parents:
#     print(i)

#匹配属性
#匹配图片的属性
# imgurl = soup.img.attrs['src']
# print(imgurl)

#匹配标签的属性
# aurl = soup.a.attrs['href']
# aclass = soup.a.attrs['class']
# aid = soup.a.attrs['id']
# print(aurl)
# print(aclass)
# print(aid)

#匹配所有相同的标签
# ps = soup.find_all('p')
# print(ps)
# print('_'*15)
# aes = soup.find_all('a')
# print(aes)

#选择器去匹配
# a = soup.select('#link1')
# print(a)
# a1 = soup.select('.sister')
# print(a1)

#select 根据标签去选择
title = soup.select('p b')
print(title)