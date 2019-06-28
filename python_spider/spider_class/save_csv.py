# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     save_csv
   Description :
   Author :       gongyan
   date：          2018/11/13
   Change Activity:2018/11/13 20:33:
-------------------------------------------------
"""
import csv

# with open('data.csv','w',newline="") as csvfile:  #如果在这不加newline=“” 会出现内容之间有空行
#     writer = csv.writer(csvfile)
#     writer.writerow(['id','name','age'])
#     writer.writerow(['1','zhang','23'])
#     writer.writerow(['2','wang','43'])
#     writer.writerow(['3','xiao','23'])

# 使用writerows()可以同时写入多行
with open('data_rows.csv','w',newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id','name','age'])
    writer.writerows([['10010','Mike','23'],['10011','Bob','22'],['10003','Jordan','21']])

#爬虫爬的都是结构化的数据。对数据进行存储
# with open('data_row_head.csv','w',newline='') as csvfile:
#     fieldnames = ['id','name','age']
#     writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerow({'id':'10010','name':'Mike','age':21})
#     writer.writerow({'id':'10011','name':'Bob','age':23})
#     writer.writerow({'id':'10013','name':'Joe','age':24})

# 对数据的读取：
# with open('data.csv','r',encoding='utf-8') as csvfile:
#     reader = csv.reader(csvfile)
#     for i in reader:
#         print(i)
