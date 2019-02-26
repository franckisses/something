# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      user_agent_test
   Description :     
   Author :         gongyan
   Date：           2019/2/25
   Change Activity: 2019/2/25 13:47
-------------------------------------------------
"""
#安装库名： fake-useragent

from fake_useragent import UserAgent

#创建ua对象
ua = UserAgent()
for i in range(10):
    #输出chrome浏览器的请求头
    print(ua.chrome)
    print("#"*30)
    print(ua.firefox)
    print("---------"*15)