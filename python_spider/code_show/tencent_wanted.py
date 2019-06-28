# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     tencent_wanted
   Description :
   Author :       gongyan
   date：          2018/11/26
   Change Activity:2018/11/26 17:20:
-------------------------------------------------
"""
import time
from bs4 import BeautifulSoup
import requests


def get_page(url,headers):
    response = requests.get(url,headers)
    html = response.text #将返回的数据转化成str类型
    print(html)
    # soup = BeautifulSoup(html,'lxml') #创建soup对象
    #网站的标题
    # title = soup.title.text
    # print(title)
    # position = soup.select('.even')
    # position1 = soup.select('.odd')



if __name__ == '__main__':
    url = 'http://dongqiudi.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Cookie': 'dqduid=ChOLeFxICPqAjHTYA3dHAg==; Hm_lvt_662abe3e1ab2558f09503989c9076934=1548596813,1548637719,1548682738,1548727909; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216797fd8b75363-03e5ed2eb617ae-3a3a5d0c-1049088-16797fd8b76351%22%2C%22%24device_id%22%3A%2216797fd8b75363-03e5ed2eb617ae-3a3a5d0c-1049088-16797fd8b76351%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%7D%7D; laravel_session=eyJpdiI6IlRIRG54c2JMelRzQUdEUGppa1JaXC9hMll6VDJuUDdXVHY0V3RwXC9qSmoxTT0iLCJ2YWx1ZSI6IjBCUHBmR1ZCb1U4d1pGbXdqXC9BQnNVbmVyd1ltdkZFRnRRczArOU1XTVVkNHJtRTNRMWEreCtaSWwxcVFDVUZjeHhhWGV4cldqeVwvWno4clMxb1BvTkE9PSIsIm1hYyI6ImNlZWVkNmQ3NTJiNTJjNDdlMTY5MjM1NDUxYjRjYTZjY2NmYTdmZTk4ODg1MTA5MDFlYzhmN2NkZjU3ZDk3OGYifQ%3D%3D; Hm_lpvt_662abe3e1ab2558f09503989c9076934=1548730988',
        'Host': 'dongqiudi.com',
        'Upgrade-Insecure-Requests': 1
    }
    get_page(url,headers)