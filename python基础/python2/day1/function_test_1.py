#coding:utf-8
# 函数被调用之后会有一个返回值，函数的引用会返回一个引用对象
# def name(num):
#     print(num)
#     return "ok"
#
# print(name(3))

# 1. 随机生成两个100以内的数字
# 2. 随机选择加法或是减法
# 3. 总是使用大的数字减去小的数字
# 4. 如果用户答错三次，程序给出正确答案
import random

num_1 = random.randint(1,100)
num_2 = random.randint(1,100)
operator = ['加','减']
operation = random.choice(operator)
i = 0
while i<3:
    num = input("please enter your guess")
    if operation=='加':
        result = num_1 + num_2
        if result == num:
            print("you did a good job!")
            break
    if operation =='减':
        if num_1-num_2>0:
            result = num_1-num_2
            if result == num:
                print("you did a good job!")
                break
        result = num_2-num_1
        if result == num:
            print("you did a good job!")
            break
    i+=1

