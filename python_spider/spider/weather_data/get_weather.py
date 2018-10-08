# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     get_weather
   Description :
   Author :       gongyan
   date：          2018/10/8
   Change Activity:2018/10/8 9:58:
-------------------------------------------------
"""

from urllib.request import urlopen
import json

def get_weather(city_code):
    url = 'http://www.weather.com.cn/data/sk/%s.html' % city_code
    html = urlopen(url)
    data = json.loads(html.read())
    print(data)




if __name__ == '__main__':
    city_code = {
        '0':'101010100',
        '1':'101121404'
    }
    for key,value in city_code.items():
        # print(key,value)
        get_weather(value)
