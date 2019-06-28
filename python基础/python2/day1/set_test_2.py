#coding:utf-8
# 1. 编写第一个函数，函数接收姓名和年龄，如果年龄不在1到120之间，产生ValueError异常
# 2. 编写第二个函数，函数接收姓名和年龄，如果年龄不在1到120之间，产生断言异常

# def age_range(age):
#     1<age<120
# try:
#     age_range(3432)
# except ValueError:
#     print("you are too old or too young")
# else:
#     print("nothing")

# def age_name(age,name):
#     if age>120 and age<1:
#         raise ValueError("这里需要传入一个大于1小于120的整数")
#     else:
#         print(int(age))
# try:
#     age_name(0,"xiaowang")
# except ValueError as e:
#     print(e)

def foo(s):
    if not isinstance(s, int):
        raise ValueError('这里需要传入一个整数类型')
    else:
        print(int(s))
try:
    foo(12)
    foo('hello')
except ValueError as e:
    print(e)

