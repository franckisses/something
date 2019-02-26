# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      xpath_test
   Description :    xpath 语法练习
   Author :         gongyan
   Date：           2019/2/25
   Change Activity: 2019/2/25 15:26
-------------------------------------------------
"""
import requests
from fake_useragent import UserAgent
from lxml import etree
import io,sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
def downloadpage(url):
    headers = {
        'User-Agent':UserAgent().chrome
    }
    response = requests.get(url,headers=headers)
    text = response.text    #etree.HTML只能接收解析网页的字符串
    html = etree.HTML(text)
    divcontents = html.xpath('//div[@class="r_lbx"]')  #xpath语法的返回值是一个列表
    for singlediv in divcontents:
        imgurl = singlediv.xpath("a/img/@src")[0]  #房源的图片的链接
        title = singlediv.xpath("div[1]/div[1]/a/text()")[0]  #房源的名称
        tosubway = singlediv.xpath("div[1]/div[1]/div/text()")[1]  #与地铁站的距离
        #将所有的字符串匹配出来，然后进行去空格处理，再进行分割
        totalinfo = singlediv.xpath('div[1]/div[2]/text()')[1].strip().split("|")
        area = totalinfo[0]
        floor = totalinfo[1].strip()
        roomType = totalinfo[2].strip()
        location = totalinfo[3]
        istogether = singlediv.xpath('div[1]/div[2]/i/text()')[0]  #是不是合租
        firstmonthRent = singlediv.xpath('div[2]/div/span[2]/text()')[0].strip()  #首月的房租
        monthRent = singlediv.xpath('div[2]/div/div/em/text()')[0].replace("¥","")  #次月正常房租
        break





if __name__ == '__main__':
    url = "https://www.danke.com/room/nj?page=1"
    downloadpage(url)