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


db = pymysql.connect(host='localhost', user='root', database='mysqltest1',\
                     password='123456', charset='utf8')

cur = db.cursor()

# cur.execute('create database if not exists mysqltest;')
cur.execute('use mysqltest1;')

cur.execute('create table if not exists tmooc(id int primary key ,\
        name varchar(20), score tinyint unsigned);')

cur.execute('insert into tmooc values (1,"xiaowang",44),(2,"hou",88);')
db.commit()
cur.close()
db.close()