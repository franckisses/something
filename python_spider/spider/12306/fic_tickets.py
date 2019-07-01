# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     fic_tickets
   Description :   get tickets
   Author :       gongyan
   date：          2019/1/3
   Change Activity:2019/1/3 9:09:
-------------------------------------------------
"""

from selenium import webdriver
import requests,time

web = webdriver.Chrome()
cookdict = {
    'Cookie':'JSESSIONID=6DB164C36AE51A384F93E5CEBC38B297; tk=A3uZzqFkjIh0tRWhaow4Q1zy-aL8fxINrCazR6F6DyAy01210; _jc_save_fromStation=%u5317%u4EAC%2CBJP; _jc_save_wfdc_flag=dc; RAIL_EXPIRATION=1546718901812; RAIL_DEVICEID=ZWJzCbtfcN67cAzry4rPaCUYJ3BJg3QgUxw8d9kS36wzfKpjTa6HfxbrBpmjUtCGtBDoHJ8S26CYZFNv8QXDYrmzCGs5likHfJupMKExmH3TUym1IQV8VGlUxLWYRWzKBeYDkkVkP-BV1m12vl-OErNf8d1hWjd7; _jc_save_showIns=true; BIGipServerotn=1206911498.64545.0000; BIGipServerpool_passport=250413578.50215.0000; _jc_save_toDate=2019-01-03; route=c5c62a339e7744272a54643b3be5bf64; _jc_save_fromDate=2019-01-03; current_captcha_type=Z; _jc_save_toStation=%u4E0A%u6D77%2CSHH'
}
web.get('https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E5%8C%97%E4%BA%AC,BJP&ts=%E9%95%BF%E6%B2%BB%E5%8C%97,CBF&date=2019-01-03&flag=N,N,Y')
a = web.get_cookie('Cookie')
print(a)
web.get('https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E5%8C%97%E4%BA%AC,BJP&ts=%E9%95%BF%E6%B2%BB%E5%8C%97,CBF&date=2019-01-03&flag=N,N,Y')

time.sleep(5)
web.close()