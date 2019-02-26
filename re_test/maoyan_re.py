# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      maoyan_re
   Description :     
   Author :         gongyan
   Date：           2019/2/26
   Change Activity: 2019/2/26 20:56
-------------------------------------------------
"""

import re

import requests
from fake_useragent import UserAgent


def getpage(url):
    headers = {
        'User-Agent': UserAgent().firefox
    }
    response = requests.get(url,headers)
    if response.status_code == 200:
        return response.text
    else:
        return None


def parse_one_page(text):
    pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>'
                         '(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">'
                         '(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    result = re.findall(pattern, text)
    for i in result:
        print(i)

def main():
    url = 'https://maoyan.com/board/4?offset=0'
    text = getpage(url)
    if text:
        parse_one_page(text)


if __name__ == '__main__':
    main()