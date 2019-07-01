# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      bing_re
   Description :     
   Author :         gongyan
   Date：           2019/2/27
   Change Activity: 2019/2/27 8:32
-------------------------------------------------
"""
import re

import requests
from fake_useragent import UserAgent


def getpage(url):
    headers = {
        'User-Agent':UserAgent().chrome
    }
    response = requests.get(url,headers)
    if response.status_code == 200:
        return response.text
    else:
        return None



def parse_one_page(text):
    print(text)
    pattern = re.compile('<a.*?_blank.*?src="(.*?)".*?></div><p>.*?</p>(.*?)</p></a>', re.S)
    result = re.findall(pattern,text)
    print(result)




def main():
    url = 'http://bing.plmeizi.com/?page=2'
    text = getpage(url)
    if text:
        parse_one_page(text)
    else:
        print('请求异常')



if __name__ == '__main__':
    main()