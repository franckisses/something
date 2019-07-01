# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     try
   Description :   this file is for selenium show!
   Author :       gongyan
   date：          2019/1/21
   Change Activity:2019/1/21 9:59:
-------------------------------------------------
"""
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote

web = webdriver.Chrome()
wait = WebDriverWait(web,10)
KEY = 'iphone'

def index_page(page):
    """
    抓取索引页
    :param page:页码
    :return:
    """
    print('正在抓取第%d页'%page)
