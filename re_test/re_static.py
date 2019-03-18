# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      re_static
   Description :     
   Author :         gongyan
   Date：           2019/2/27
   Change Activity: 2019/2/27 8:16
-------------------------------------------------
"""
import io
import sys
import re

from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup


sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

def getpage(url):
    headers = {
        'User-Agent': UserAgent().firefox,
        'Referer': 'http://www.stats.gov.cn/tjfw/gwyzl/zlgg/'
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    text = response.text
    pattern = re.compile(''
    )

def main():
    url = 'http://www.stats.gov.cn/tjfw/gwyzl/zlgg/201902/t20190212_1648667.html'
    getpage(url)

if __name__ == '__main__':
    main()
