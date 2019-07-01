# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     wangyidict
   Description :
   Author :       gongyan
   date：          2019/1/3
   Change Activity:2019/1/3 20:56:
-------------------------------------------------
"""
import requests


url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

key={
    'type':"AUTO",
    'i':'hello',
    "doctype":"json",
    "version":"2.1",
    "keyfrom":"fanyi.web",
    "ue":"UTF-8",
    "action":"FY_BY_CLICKBUTTON",
    "typoResult":"true"
    }
response = requests.get(url,data=key)
text = response.content

print(text)