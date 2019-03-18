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
import time


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
        url = 'https://s.taobao.com/search?q='
        webElement.get(url)
        webElement.find_element_by_id('J_Quick2Static').click()
        webElement.find_element_by_id('TPL_username_1').send_keys('18667018590')
        webElement.find_element_by_id('TPL_password_1').send_keys('tb842549758')
        time.sleep(5)
        webElement.find_element_by_id('J_SubmitStatic').click()
        time.sleep(12345)
    except TimeoutException as e:
        print('hhaha')

        # if page > 1:
        #     input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#q')))
        #     submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.btn-search.tb-bg')))
        #     input.clear()
        #     input.send_keys(page)
        #     submit.click()
    # except TimeoutException:
    #     print('Time out ')


if __name__ == '__main__':
    for i in range(1,10):
        index_page(1)