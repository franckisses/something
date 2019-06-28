# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     beautiful_soup
   Description :
   Author :       gongyan
   date：          2018/11/13
   Change Activity:2018/11/13 9:43:
-------------------------------------------------
"""
import requests
import os
import datetime

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) ' \
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
    }

if not os.path.isdir('%s'%datetime.datetime.now().strftime('%Y-%m-%d')):
    os.makedirs('%s'%datetime.datetime.now().strftime('%Y-%m-%d'))
# fileName = 'images\\' + fileNum + fileFix

# url = 'http://bimgs.plmeizi.com/images/bing/2018/NorsteadLights_ZH-CN9558383357_1920x1080.jpg'
# response = requests.get(url,headers)
# print(response.text)