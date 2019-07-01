# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     lagou_jobdetail
   Description :
   Author :       gongyan
   date：          2019/2/13
   Change Activity:2019/2/13 11:32:
-------------------------------------------------
"""
import requests


# ssl._create_default_https_context = ssl._create_unverified_context
# ssl._create_default_https_context =ssl._create_unverified_context


def getInfo(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36',
        'Referer': 'https://www.lagou.com/jobs/list_%E4%BA%91%E8%AE%A1%E7%AE%97?labelWords=&fromSearch=true&suginput=',
        'X-Requested-With': 'XMLHttpRequest'
    }
    for i in range(1,31):
        if i == 1:
            first = 'true'
        else:
            first = 'flase'
        data = {
            'first': first,
            'pn': i,
            'kd': '云计算'
        }
        print(data)
        print(headers)
        response = requests.post(url,data=data,headers=headers,verify=False)
        print(response.status_code)
        print("#"*40)
        print(response.text)
        break


if __name__ == '__main__':
    url = "https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false"
    getInfo(url)
