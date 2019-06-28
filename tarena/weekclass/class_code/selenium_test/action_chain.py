# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     action_chain
   Description :
   Author :       gongyan
   date：          2019/1/21
   Change Activity:2019/1/21 16:04:
-------------------------------------------------
"""

from selenium import webdriver
from selenium.webdriver import ActionChains


web = webdriver.Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
web.get(url)

web.switch_to.frame('iframeResult')

source = web.find_element_by_css_selector('#draggable')  #元素的原位置
target = web.find_element_by_css_selector('#droppable')  #元素的目标位置
action = ActionChains(web)

action.drag_and_drop(source,target)

action.perform()