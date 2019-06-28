# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     pyquery_test
   Description :
   Author :       gongyan
   date：          2018/12/24
   Change Activity:2018/12/24 4:18:
-------------------------------------------------
"""
from pyquery import PyQuery as pq

html = """
<tr class="even">
    <td class="l square"><a target="_blank" href="position_detail.php?id=46576&amp;keywords=&amp;tid=0&amp;lid=0">TEG14-云数据库高级研发工程师（深圳/北京/武汉）</a></td>
    <td>技术类</td>
    <td id="num">2</td>
    <td>深圳</td>
    <td>2018-12-23</td>
    <img src="http://www.baidu.com">
</tr>
<tr class="odd">
    <td class="l square"><a target="_blank" href="position_detail.php?id=46576&amp;keywords=&amp;tid=0&amp;lid=0">TEG14-云数据库高级研发工程师（深圳/北京/武汉）</a></td>
    <td>技术类</td>
    <td id="num">2</td>
    <td>深圳</td>
    <td>2018-12-23</td>
    <img src="http://www.baidu.com">
</tr>
"""


doc = pq(html)
# print(html)
# print(doc("tr"))
# print(doc.tr.attr)
# doc=pq(filename='new.html')
# print(doc(".even").text())
# print(doc('#num').text())
# a_tag = doc('a')
# print(a_tag)
# print(a_tag.attr('href'))
# img_tag = doc('img')
# print(img_tag.attr('src'))
td_tags = doc('.even').items()
for tag in td_tags:
    print(tag('td').text())
