# _*_ coding: utf-8 _*_
"""
-------------------------------------------------
   File Name：     dongqiudi
   Description :
   Author :       gongyan
   date：          2019/1/7
   Change Activity:2019/1/7 19:54:
-------------------------------------------------
"""
import requests
from lxml import etree


def get_page(url):

    """
    get the page information！
    :param url:
    :return: nothing！
    """

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    response = requests.get(url,headers=headers)
    text = response.text
    html = etree.HTML(text)

    li = html.xpath('//div[@id="news_list"]/ol/li')
    print(len(li))


if __name__ == '__main__':
    for i in range(1,20):
        url = 'http://www.dongqiudi.com/archives/1?page={}'.format(i)
        get_page(url)

