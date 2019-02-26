# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      youdao_dict
   Description :    有道词典的爬虫
   Author :         gongyan
   Date：           2019/2/26
   Change Activity: 2019/2/26 8:58
-------------------------------------------------
"""
import json
import requests


def translate(url,data):
    datadict = {
        'type': "AUTO",
        'i': data,
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "ue": "UTF-8",
        "action": "FY_BY_CLICKBUTTON",
        "typoResult": "true"
    }
    response = requests.post(url,datadict)
    text = response.text
    info = json.loads(text)
    result = info['translateResult'][0][0]['tgt']   #[[{"src":"zhongguo","tgt":"中国"}]]
    print('翻译的结果是：',result)


def printinfo():
    print("您现在使用的是有道翻译的api接口")
    data = input("请输入您要翻译的内容:")
    return data

def main():
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule\
            &smartresult=ugc&sessionFrom=null'
    data = printinfo()
    translate(url,data)

if __name__ == '__main__':
    main()