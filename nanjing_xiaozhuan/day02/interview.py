# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      interview
   Description :     
   Author :         gongyan
   Date：           2019/2/26
   Change Activity: 2019/2/26 6:21
-------------------------------------------------
"""
"""
题目：
一辆卡车违反交通规则,撞人后逃跑.现场有三人目击事件,
但都没有记住车号,只记下车号的一些特征.
甲说：牌照的前两位数字是相同的；
乙说：牌照的后两位数字是相同的,但与前两位不同；
丙是数学家,他说：四位的车号所构成的数字正好等于某一个整数的平方.
请根据以上线索求出车号. 
"""


from math import sqrt

#第一种方法：
for i in range(1, 10):
    for j in range(1, 10):
        num = 1000*i+100*i+10*j+j
        if sqrt(num) == int(sqrt(num)):
            print("第一种算法")
            print(num)
#第二种方法：
for i in range(32, 100):
    num = i**2
    a, b, c, d = num // 1000, (num % 1000)//100, (num % 100) // 10, num % 10
    if a == b != c ==d:
        print('第二种算法')
        print(num)
