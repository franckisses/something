# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      jd_comments
   Description :     
   Author :         gongyan
   Date：           2019/2/26
   Change Activity: 2019/2/26 9:55
-------------------------------------------------
"""
import json
import requests

from fake_useragent import UserAgent


def getjson(url):
    headers = {
        'User-Agent':UserAgent().chrome,
        'Referer': 'https://item.jd.com/100000822981.html'
    }
    response = requests.get(url,headers=headers)
    text = response.text
    #进行数据的清洗
    jsonobject = text[27:-2]
    result = json.loads(jsonobject)
    comments = result['comments']
    for i in comments:
        #评论的内容
        content = i['content']
        #用户的等级状况
        userLevelName = i['userLevelName']
        #用户使用的终端设备
        userClientShow = i['userClientShow']
        #用户购买的型号
        productSales = i['productSales'][0]['saleValue']
        with open('jdcomments.txt','a+') as f:
            f.write(content+" "+userLevelName+" "+userClientShow+" "+productSales+"\n")
            f.write('-'*30+"\n")


if __name__ == '__main__':
    baseurl = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv14250&\
productId=100000822981&score=0&sortType=5&page={}&pageSize=10&isShadowSku=0&rid=0&fold=1'
    for i in range(11):
        url = baseurl.format(i)
        getjson(url)
        break

