# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     jianshu_test
   Description :
   Author :       gongyan
   date：          2019/2/25
   Change Activity:2019/2/25 9:11:
-------------------------------------------------
"""
import requests

url = 'http://www.jianshu.com'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 \
         (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
}
response = requests.get(url,headers=headers)

#查看状态码
print(response.status_code)
#查看响应的内容
print(response.content)


# Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko