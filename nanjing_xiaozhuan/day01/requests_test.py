# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      requests_test
   Description :
   Author :         gongyan
   Date：           2019/2/25
   Change Activity: 2019/2/25 14:49
-------------------------------------------------
"""
import requests
from fake_useragent import UserAgent

#查看源代码 快捷键：ctrl +b 跳转到api接口。

# response = requests.request(method='get',url='',**kwargs)

# response1 = requests.get(url='',params="",kwargs)
# response2 = requests.post(url='',params="",kwargs)
# response2 = requests.head(url='',params="",kwargs)
# response2 = requests.options(url='',params="",kwargs)
# response2 = requests.delete(url='',params="",kwargs)
# response2 = requests.put(url='',params="",kwargs)
headers = {
    'User-Agent':UserAgent().chrome
}
response = requests.get('http://www.dongqiudi.com',headers=headers)

print(response.text)

