"""
# -*- coding: utf-8 -*-
# @Time    : 2018/8/15 9:33
# @Author  : franck
# @Email   : franck_gxu@outlook.com
"""
import pymysql


class DbHelper:
    """
    完成所有对mysql数据库的处理
    """
    def __init__(self, host="localhost", port=3306, user="root",
                 password="123456", database="jdlipstick", charset="utf8"):
        self.host = host
        self.port = port
        self.password = password
        self.user = user
        self.db = database
        self.charset = charset
        self.conn = None
        self.cur = None

    def connectData(self):
        try:
            self.conn = pymysql.connect(host=self.host,
                                        user=self.user,
                                        port=self.port,
                                        passwd=self.password,
                                        database=self.db,
                                        charset=self.charset
                                        )
        except:
            print("conn error")
            return False
        self.cur = self.conn.cursor()
        return True

    def close(self):
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()
        return True

    def execute(self,sql,params = None):
        if self.connectData() == False:
            return False
        try:
            if self.conn and self.cur:
                self.cur.execute(sql,params)
                self.conn.commit()
        except:
            print("execute:"+sql+"error")
            return False
        return True

if __name__ == "__main__":
    dbhelper = DbHelper()
    print(dbhelper.connectData())
#     title = "英雄本色"
#     actor = "周润发"
#     time = "2010-08-17"
#     sql = "INSERT INTO newdatabase.maoyan(title,actor,time) VALUES(%s,%s,%s)"
#     params = (title, actor, time)
#     result = dbhelper.execute(sql, params)
#     if (result == True):
#         print("Insert Ok")
#     else:
#         print("Insert Failed")
#     print(dbhelper.close())
#
#     title = '五证齐全 可按揭可贷款 随时可看 带西工大锦园xiao学'
#     department = '西安锦园 '
#     style = ' 3室2厅 '.strip()
#     area = ' 141.64平米 '.strip()
#     towards = ' 南 北 '.strip()
#     district = '城西'
#     specialty = '房本满五年随时看房'
#     total_floor = '板塔结合'
#     build_type = '11'
#     total_price = '320'
#     average_price = '10'
#     release_time = ' 其他'.strip()
#     show_time = '1人关注 '
#     focus = '中楼层'
#     high_low = '22593'
#     decorate = ' 26天以前发布'.strip()
#
#     sql = "INSERT INTO newdatabase.lianjia_ershou(title, department,style, area, towards, district,specialty, build_type,total_floor,total_price,show_time,decorate,focus,high_low,average_price,release_time) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
#     params = (title, department,style, area, towards, district,specialty, build_type,total_floor,total_price,show_time,decorate,focus,high_low,average_price,release_time
#               )
#     result = dbhelper.execute(sql, params)
#     if result == True:
#         print("插入成功")
#     else:
#         print("插入失败", params)
