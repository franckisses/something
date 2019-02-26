# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     urllib_test
   Description :
   Author :       gongyan
   date：          2019/2/25
   Change Activity:2019/2/25 11:03:
-------------------------------------------------
"""
import urllib

print(urllib.request.urlopen("http://www.baidu.com").read())