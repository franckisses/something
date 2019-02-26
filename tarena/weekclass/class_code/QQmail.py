# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     QQmail
   Description :
   Author :       gongyan
   date：          2019/1/21
   Change Activity:2019/1/21 16:13:
-------------------------------------------------
"""
from selenium import webdriver
from selenium.webdriver import ActionChains
import time
import getpass


web = webdriver.Chrome()
web.get('https://mail.qq.com/')

web.switch_to.frame('login_frame')

buttonLogin = web.find_element_by_id('switcher_plogin')
buttonLogin.click()
time.sleep(2)

inputName = web.find_element_by_id('u')
inputName.send_keys('249155836')
# inputpasswd = web.find_element_by_id('p')
# password = getpass.getpass('请输入密码：')
# inputpasswd.send_keys(password)
time.sleep(6)

login = web.find_element_by_id('login_button')
login.click()