# -*- coding:utf-8 -*-
#'''这是一个查询数据库的模块''
# e-mail:franck_gxu@outlook.com

import sqlite3

class WeatherDate:
    def __init__(self):
        self.conn = sqlite3.connect('weather.db')
        self.cursor = self.conn.cursor()

    def create_table(self):
        create = "CREATE TABLE City (user_ID integer PRIMARY KEY\
         autoincrement,user_mail  TEXT,user_name TEXT,user_city TEXT,mian_city INTEGER )"
        self.cursor.execute(create)
        self.conn.commit()

    def get_main(self,):
        a=self.cursor.execute("select user_city from City where main_city=1")
        mainCity=a.fetchone()
        return  mainCity


    def set_main(self,mail):
        self.cursor.execute("UPDATE City SET main_city=0")
        main="UPDATE City SET main_city=1 where user_mail='%s'"%mail
        self.cursor.execute(main)
        self.conn.commit()

    def write_date(self, user_mail, user_name, user_city,main_city):
        write = 'insert into City values(null,"%s","%s","%s","%d")' % (
            user_mail, user_name, user_city,main_city)
        self.cursor.execute(write)
        self.conn.commit()

    def read_date(self):
        a = self.cursor.execute('select * from City')
        all_recode = a.fetchall()
        return all_recode

    def read_email(self):
        a=self.cursor.execute('select user_mail from City')
        all_email = a.fetchall()
        return all_email

    def modify_name(self, new_name, old_name):
        modify = 'update City set user_name="%s" where user_name="%s"' % (
            new_name, old_name)
        self.cursor.execute(modify)
        self.conn.commit()

    def modify_mail(self, new_mail, old_mail):
        modify = 'update City set user_mail="%s" where user_mail="%s"' % \
            (new_mail, old_mail)
        self.cursor.execute(modify)
        self.conn.commit()

    def modify_city(self, new_city, old_city):
        modify = 'update City set user_city="%s" where user_city="%s"' % \
            (new_city, old_city)
        self.cursor.execute(modify)
        self.conn.commit()

    def remove_info(self,name,mail):
        remove='delete from City where user_name="%s" and user_mail="%s"'%(name,mail)
        self.cursor.execute(remove)
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()

# 测试一下获取邮件的信息
a=WeatherDate()
a.set_main('842549758@qq.com')
# b=a.read_date()
# b=a.get_main()
# mail="842549758@qq.com"
# user_mail, user_name, user_city,main_city
# c=a.write_date("192081984@qq.com","小鱼","延安",0)
# print(a)
# print(c)

# print(c)
# # x=a.modify_city("渭南","杨凌")
# print(b)
# c=[]
# for email in b:
#     c.append(email[0])
# print(c)   #返回的类型是字符串