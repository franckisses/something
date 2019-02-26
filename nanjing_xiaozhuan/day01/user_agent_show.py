# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      user_agent_show
   Description :    这个代码用来演示服务器如何来识别爬虫的。
   Author :         gongyan
   Date：           2019/2/25
   Change Activity: 2019/2/25 13:54
-------------------------------------------------
"""
import requests
from fake_useragent import UserAgent

#验证http请求的网站域名
url = "http://www.httpbin.org/get"
#请求头
headers = {
    'User-Agent': UserAgent().chrome
}
#构造请求
response = requests.get(url,headers=headers)
print(response.text)