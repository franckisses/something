# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     qq_qonze
   Description :
   Author :       gongyan
   date：          2019/1/25
   Change Activity:2019/1/25 10:44:
-------------------------------------------------
"""
from selenium import webdriver
import time
import io,sys


sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

class qqZone:
    def __init__(self):
        self.web = webdriver.Chrome()
        self.web.get('https://qzone.qq.com/')
        self.web.switch_to.frame('login_frame')

    def login(self):
        self.web.find_element_by_id('switcher_plogin').click()
        time.sleep(15)
        self.web.find_element_by_id('login_button').click()

    def get_data(self):
        print(self.web.page_source)




if __name__ == '__main__':
    q = qqZone()
    q.login()
    time.sleep(3)
    q.get_data()
