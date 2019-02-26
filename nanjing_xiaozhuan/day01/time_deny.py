# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      time_deny
   Description :     
   Author :         gongyan
   Date：           2019/2/25
   Change Activity: 2019/2/25 14:13
-------------------------------------------------
"""


def getPage ():
    pass



if __name__ == '__main__':
    for i in range(100):
        url = "http://www.baidu.com/page=1"
        getPage(url)
        time.sleep(2)