# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     wait_sele
   Description :
   Author :       gongyan
   date：          2019/1/21
   Change Activity:2019/1/21 17:02:
-------------------------------------------------
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

web = webdriver.Chrome()
web.get('http://www.taobao.com/')
wait = WebDriverWait(web,10)
input_ = wait.until(EC.presence_of_element_located((By.ID,'q')))
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.btn-search')))
print(input_,'###',button)



等待条件                                     含义
title_is                                 标题是什么内容
tiele_contains                           标题包含什么内容
presence_of_element_located              节点加载出来，传入定位元祖，如（By.ID,'p'）
visibility_of_element_located            节点课间，传入定位元祖
visibility_of                            可见。传入节点对象
presence_of_all_elements_located         所有节点加载出来
text_to_be_present_in_element            某个节点文本包含某文字
text_to_be_present_in_element_value      某个节点值包含某文字
frame_to_be_avaliable_and_switch_to_it   加载并切换
invisibility_of_element_located          节点不可见
element_to_be_clickable                  节点可点击。
staleness_of                             判断一个节点是否仍存在DOM，可判断页面是否已经刷新
element_to_be_selected                   节点可选择，传节点对象
element_located_to_be_selected           节点可选择，传入定位元祖
element_selection_state_to_be            传入节点对象以及状态，相等返回True，否则返回False
element_located_sekection_state_to_be    传入定位元祖以及状态，相等返回True，否则返回False
alert_is_present                         是否出现警告
