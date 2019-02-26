# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Data_jd_lipstick_visuable
   Description :
   Author :       gongyanthis is for jd comments visuable!
   date：          2019/1/18
   Change Activity:2019/1/18 17:11:
-------------------------------------------------
"""
import pymysql


class dbHelper:

    def __init__(self,host='localhost',port=3306,user='root',password='123456',
                database='jdlipstick',charset='utf8'):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset
        self.conn = None
        self.cur = None


    def connectData(self):
        try:
            self.conn = pymysql.connect(host=self.host,
                                        user=self.user,
                                        port=self.port,
                                        passwd=self.password,
                                        database=self.database,
                                        charset=self.charset
                                        )
        except:
            print("conn error")
            return False
        self.cur = self.conn.cursor()
        return True

    def get_data(self):
        sql = "select * from contents;"

    def close(self):
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()
        return True

if __name__ == '__main__':
    db = dbHelper()
    print(db.connectData())

