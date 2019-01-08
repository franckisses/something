# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     zhihu_sele
   Description :
   Author :       gongyan
   date：          2018/12/26
   Change Activity:2018/12/26 22:13:
------------------------------------------------
"""
import sys,io
from selenium import webdriver
from time import sleep

# reload(sys)
# sys.setdefaultencoding('utf-8')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
db = webdriver.Chrome()

db.get("https://www.lagou.com/jobs/list_linux?labelWords=&fromSearch=true&suginput=")

print(db.find_element_by_css_selector(".con_list_item default_list").text)
sleep(5)

db.close()
