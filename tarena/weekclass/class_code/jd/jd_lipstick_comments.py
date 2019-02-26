# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     taobao_spider
   Description :   this spider for crawl taobao.
   Author :       gongyan
   date：          2019/1/18
   Change Activity:2019/1/18 10:31:
-------------------------------------------------
"""
import requests,time,json
import pymysql


def get_page(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6'
    }
    response = requests.get(url,headers=headers)
    text = response.text
    print(text)

    # new_text = text[27:-2]
    # result = json.loads(new_text)  #将json格式的文字转化成字符串
    # comments = result['comments']
    # for i in comments:
    #     items = []
    #     items.append(str(i['id']))
    #     items.append(i['content'])
    #     items.append(i['referenceName'])
    #     items.append(i['referenceTime'])
    #     items.append(i['nickname'])
    #     items.append(i['productColor'])
    #     items.append(i['userLevelName'])
    #     items.append(i['userLevelId'])
    #     items.append(i['userClientShow'])
    #     items.append(i['mobileVersion'])
    #     items.append(str(i['isMobile']))
    #     print(items)
        # saveSql(items)
        # print(items)


def saveSql(items):
    id = items[0]
    content = items[1]
    referenceName = items[2]
    referenceTime = items[3]
    userLevelId = items[4]
    nickname = items[5]
    productColor = items[6]
    userLevelName = items[7]
    userClientShow = items[8]
    mobileVersion = items[9]
    isMobile = items[10]
    # print(id,content,referenceName,referenceTime,userLevelId,nickname,productColor,userLevelName,userClientShow,mobileVersion,isMobile)
    conn = pymysql.connect(host='localhost',port=3306,user='root',password='123456',database='jdlipstick')
    cur = conn.cursor()
    sql = 'INSERT INTO contents(id,content,referenceName,referenceTime,userLevelId,nickname,productColor,userLevelName,userClientShow,mobileVersion,isMobile) VALUES ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")'%(
        id, content, referenceName, referenceTime, userLevelName, nickname, productColor, userLevelId, userClientShow,
        mobileVersion, isMobile)
    try:
        cur.execute(sql)
        conn.commit()
    except:
        print("error",sql)
    finally:
        print('sucessfully')
        cur.close()
        conn.close()


if __name__ == '__main__':
    for i in range(100,101):
        url = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv30097&productId=12259131996&score=0&sortType=5&page={}&pageSize=10&isShadowSku=0&rid=0&fold=1'.format(i)
        get_page(url)
        print("current page%s"%i)




