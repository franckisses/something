# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     show
   Description :
   Author :       gongyan
   date：          2018/10/10
   Change Activity:2018/10/10 12:29:
-------------------------------------------------
"""

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = []
# 1。将列表遍历
# 2.算术运算
# 3.追加
# for i in a:
#     b.append(i**2)
# print(b)

c = [i ** 2 for i in a]
print(c)

d = [i ** 3 for i in a]
print(d)

e = [ 'tmooc.cn', 'sina.cn']
f = [ 'http://www.' + s for s in e ]
print(f)
