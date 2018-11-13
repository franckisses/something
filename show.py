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
a = [1,2,3,4,5,6,7,8,9]
# b = []
# for i in a:
#     b.append(i**2)
# print(b)
# [表达式  for  变量  in  列表]
b = [i**2 for i in a]
print(b)
c = [i**3 for i in a]
print(c)

ipname= ["tmooc.cn","sina.cn","hupu.com"]
new_ipname = ["http://www."+s for s in ipname]
print(new_ipname)

word = ["a","b","c","d","e"]
new_word = [s.upper() for s in word]
print(new_word)

