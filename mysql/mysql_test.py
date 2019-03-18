# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      mysql_test
   Description :     
   Author :         gongyan
   Date：           2019/2/26
   Change Activity: 2019/2/26 20:15
-------------------------------------------------
"""
import pymysql

# 建立数据库连接
db = pymysql.connect(host='localhost', user='root',password='123456', charset='utf8')
# 建立游标对象
cur = db.cursor()

# 创建一个mysqltest的库
cur.execute('create database if not exists mysqltest;')
#使用mysqltest这个库
cur.execute('use mysqltest;')

#创建一个表
cur.execute('create table if not exists tmooc(id int primary key ,\
                  name varchar(20), score tinyint unsigned);')

#向数据库中插入数据
cur.execute('insert into tmooc values (1,"xiaowang",44),(2,"hou",88);')
db.commit()

cur.close()  #关闭游标对象
db.close()   #再关闭连接