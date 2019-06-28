# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     weibo_test
   Description :
   Author :       gongyan
   date：          2018/11/15
   Change Activity:2018/11/15 17:46:
-------------------------------------------------
"""
from urllib.parse import unquote

url = "https://m.weibo.cn/api/container/getIndex?uid=2830678474&luicode=10000011&lfid=100103type%3D3%26q%3D%E5%B4%94%E5%BA%86%E6%89%8D%26t%3D0&containerid=1076032830678474&since_id=4284293049763841"

print(unquote(url))