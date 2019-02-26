# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     alicloud_test
   Description :   this file is for the test ali ip_pool
    the web site url is :
    https://market.aliyun.com/products/57000002/cmapi032027.html?spm=5176.2020520132.101.3.7b49721846NJxU#sku=yuncode2602700001
   Author :       gongyan
   date：          2019/2/14
   Change Activity:2019/2/14 11:14:
-------------------------------------------------
"""

import urllib, sys
import ssl


host = 'https://iphighproxyv2.haoservice.com'
path = '/devtoolservice/ipagency'
method = 'GET'
appcode = '3bbb8e934062439e8b4f6c7faad5b8ac'
querys = 'foreigntype=1'
bodys = {}
url = host + path + '?' + querys

request = urllib.request.Request(url)
request.add_header('Authorization', 'APPCODE ' + appcode)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
response = urllib.request.urlopen(request, context=ctx)
content = response.read()
if (content):
    print(content)

