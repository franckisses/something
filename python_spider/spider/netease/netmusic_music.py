# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     netmusic_music
   Description : this code just for save the singer message.include singername singerid
   Author :       gongyan
   date：          2018/10/8
-------------------------------------------------
   Change Activity:
                   2018/10/8 8:38:
-------------------------------------------------
"""

from bs4 import BeautifulSoup
import re,sys,io
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import csv
import time


sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

browser  = webdriver.Chrome() #创建谷歌浏览器对象
wait = WebDriverWait(browser,5) #设置等待的时间，以免被封ip

def getSingerId(url):
    browser.get(url)
    browser.switch_to.frame('g_iframe')
    html = browser.page_source
    soup =BeautifulSoup(html,"lxml")
    info = soup.select(".nm.nm-icn.f-thide.s-fc0")
    singername =[]
    singerid = []
    for i in info:
        singername.append(i.getText())
        singerid.append(re.findall("\d+",str(re.findall('href="(.*?)"', str(i))))[0])
    return zip(singername,singerid)


def getDate(url):
    data = []
    for singernames, singerids in getSingerId(url):
        info = {}
        info['歌手名字'] = singernames
        info['歌手ID'] = singerids
        data.append(info)
    return data

def save2csv(url):
    print("saving...")
    with open('热门歌手信息.csv', 'a', newline='', encoding='utf-8-sig') as f:
        # CSV 基本写入用 w，追加改模式 w 为 a
        fieldnames = ['歌手名字', '歌手ID']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        data = getDate(url)
        print(data)
        writer.writerows(data)
        print('保存成功')


if __name__ == '__main__':
    id  =['1001','1002',,'1003','2001','2002','2003','7001','7002','7003','4001','4002','4003','6001','6002','6003']
    params = [str(i) for i in range(65,91)]
    for i in id:
        for j in params:
            url = "https://music.163.com/discover/artist/cat?id={}&initial={}".format(i,j)
            save2csv(url)
            time.sleep(4)

