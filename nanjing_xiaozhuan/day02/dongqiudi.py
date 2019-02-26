# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      dongqiudi
   Description :    bs4_exercise
   Author :         gongyan
   Date：           2019/2/26
   Change Activity: 2019/2/26 14:44
-------------------------------------------------
"""
from fake_useragent import UserAgent
import requests


def getpage(url):
    headers = {
        'User-Agent': UserAgent().firefox,
        'Referer': 'http://www.dongqiudi.com/'
    }
    response = requests.get(url, headers=headers)
    print(response.text)

def main():
    for i in range(1,5):
        baseurl = 'http://www.dongqiudi.com/archives/1?page={}'
        url = baseurl.format(i)
        getpage(url)
        break

if __name__ == '__main__':
    main()
