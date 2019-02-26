# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     taobao_selenium
   Description :   this file just for taobao!
   Author :       gongyan
   date：          2019/1/23
   Change Activity:2019/1/23 9:50:
-------------------------------------------------
"""
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote


webElement = webdriver.Chrome()
wait = WebDriverWait(webElement,10)
KEYWORD = 'iPad'


def index_page(page):

    """
    抓取索引页
    :param page:页码
    :return:
    """
    print("正在获取第",page,'页')
    try:
        url = 'http://taobao.com/'
        webElement.get(url)
        # if page > 1:
        #     input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#q')))
        #     submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.btn-search.tb-bg')))
        #     input.clear()
        #     input.send_keys(page)
        #     submit.click()
    except TimeoutException:
        print('Time out ')


if __name__ == '__main__':
    for i in range(1,10):
        index_page(1)