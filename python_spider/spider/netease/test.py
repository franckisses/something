# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test
   Description :
   Author :       gongyan
   date：          2018/10/9
   Change Activity:2018/10/9 19:32:
-------------------------------------------------
"""
#
# var1 = 'i love linux'
# print(var1)
# print(len(var1))
# print(var1[0:-1])
# print(var1[0])

# a= [1,2,3,4,5,6,7,8,9],
# b =[1,4,9,16,25,....]

# 1.有一个列表a= [1,2,3,4,5,6,7,8,9],生成一个新列表b，
# 要求b中的每个元素是a中对应的平方。
# a= [1,2,3,4,5,6,7,8,9]
# b = []
# 1.先将a列表中的每个元素拿出来
# 2.在将每个元素进行平方
# 3.把经过运算后的元素，加入到b中

list1= [1,2,3,4,5,6,7,8,9]
list2 = []
# 1.先将列表1中的元素进行遍历
# 2.将遍历后的每一个元素进行平方运算 i**2
# 3.将进行运算之后的列表中的元素追加到列表2中
for i in list1:
    list2.append(i**2)
print(list2)

# [ 表达式 for 变量 in 列表 ]
list2 = [i**2 for i in list1]
print(list2)
print(2**3)

list3 =["a","b","c","d","e","f","g"]
list4= [i.upper() for i in list3]
print(list4)

a = ["tmooc.cn","sina.cn","hupu.com"]
b = ["http://www."+i for i in a ]
print(b)









