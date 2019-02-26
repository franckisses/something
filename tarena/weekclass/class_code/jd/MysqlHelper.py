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
    # print(dbhelper.connectData())
    id = '12351979075'
    content = '此用户未填写评价内容'
    referenceName = '【专柜正品】Dior迪奥口红女士唇膏烈艳蓝金999  # 哑光赠礼盒礼袋'
    referenceTime = '2019-01-05 22:23:01'
    nickname = 'j***6'
    productColor = '烈艳蓝金999#滋润赠礼盒礼袋'
    userLevelName = '铜牌会员'
    userLevelId = '56'
    userClientShow = '来自京东Android客户端'
    mobileVersion = '7.3.2'
    isMobile = 'True'
    sql = "INSERT INTO jdlipstick.contents(id,content,referenceName,referenceTime,nickname,productColor,userLevelName,userLevelId,userClientShow,mobileVersion,isMobile) VALUES(%s,%s,%s.%s,%s,%s,%s,%s,%s,%s,%s)"
    params = (id,content,referenceName,referenceTime,nickname,productColor,userLevelName,userLevelId,userClientShow,mobileVersion,isMobile)
    result = dbhelper.execute(sql, params)
    if result == True:
        print("Insert Ok")
    else:
        print("Insert Failed")
    print(dbhelper.close())
