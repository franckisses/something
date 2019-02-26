# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      coutry_statics
   Description :    国家统计局公务员面试名单
   Author :         gongyan
   Date：           2019/2/26
   Change Activity: 2019/2/26 14:53
-------------------------------------------------
"""
import io
import sys

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
    soup = BeautifulSoup(response.text, 'lxml')
    trs = soup.select('tbody tr')[2:]
    for i in trs:
        text = i.text
        print(text.split('   '))
        # '  '.strip() 去字符串两边的空格


def main():
    url = 'http://www.stats.gov.cn/tjfw/gwyzl/zlgg/201902/t20190212_1648667.html'
    getpage(url)

if __name__ == '__main__':
    main()
