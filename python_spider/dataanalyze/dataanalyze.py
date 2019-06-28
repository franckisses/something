# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     dataanalyze
   Description : this file is put the data into mysql
   Author :       gongyan
   date：          2018/12/17
   Change Activity:2018/12/17 10:00:
-------------------------------------------------
"""
from MysqlHelper import DbHelper

def read_csv(filename):
    with open(filename,'r',encoding='utf-8') as f:
        data = f.readlines()
    # print(data)
    write2sql(data)


# index location department type dis2sub area floor tag rent
def write2sql(item):
    dbhelper = DbHelper()
    for x in item:
        x= x.split(" ")
        index = x[0]
        location = x[1]
        department = x[2]
        huxing= x[3]
        dis2sub = x[4]
        area = x[5]
        floor = x[6]
        tag = x[7]
        rent = x[8].strip()
        sql = "INSERT INTO newdatabase.danke(index,location,department,huxing,dis2sub,area,floor,tag,rent) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        params = (index,location,department,huxing,dis2sub,area,floor,tag,rent)
        result = dbhelper.execute(sql, params)
        if result == True:
            print("插入成功")
        else:
            print("插入失败", params)

if __name__ == '__main__':
    read_csv("new.txt")