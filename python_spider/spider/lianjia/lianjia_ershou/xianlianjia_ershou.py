"""
# -*- coding: utf-8 -*-
# @Time    : 2018/8/16 18:57
# @Author  : franck
# @Email   : franck_gxu@outlook.com
"""
import random
import re
import time
import requests
from MysqlHelper import DbHelper
from UserAgentPool import UserAgent
from lxml import etree



# 请求网页
def request_page(url):
    # 设置请求头
    headers = {
        "User-Agent": UserAgent().user_agent(),
        "Cookie": 'lianjia_ssid=ee1a20cd-2237-42ee-a22f-18cbb1190fc6; expires=Fri, 17-Aug-18 08:23:49 GMT; Max-Age=1800; domain=.lianjia.com; path=/'
    }
    response = requests.get(url, headers=headers)
    text = response.text
    html = etree.HTML(text)
    # 标题
    title = html.xpath('//div[4]/div[1]/ul/li/div[1]/div[1]/a/text()')
    # 小区
    department = html.xpath('//div[4]/div[1]/ul/li/div[1]/div[2]/div/a/text()')
    # 行政区域
    district = html.xpath('//div[4]/div[1]/ul/li/div[1]/div[3]/div/a/text()')
    # 风格
    style = []
    # 建筑面积
    area = []
    # 走向
    towards = []
    # 装修
    decorate = []
    # 关注人数
    focus = []
    # 带看次数
    show_time = []
    # 发布时间
    release_time = []
    # 具体描述
    specialty = []
    # 是否为高楼层 一共多少层 楼层类型
    build_type = html.xpath('//div[4]/div[1]/ul/li/div[1]/div[3]/div/text()')
    some_info1 = html.xpath('//div[4]/div[1]/ul/li/div[1]/div[2]/div/text()[2]')
    # 关注度 带看  发布时间
    some_info3 = html.xpath("//div[4]/div[1]/ul/li/div[1]/div[4]/text()")
    # print(type(some_info1))
    for x in some_info1:
        style.append(x.split("|")[1])
        area.append(x.split("|")[2])
        towards.append(x.split("|")[3])
        decorate.append(x.split("|")[4])
    for info_str1 in some_info3:
        focus.append(info_str1.split("/")[0])
        show_time.append(info_str1.split("/")[1])
        release_time.append(info_str1.split("/")[2])
    # 特点
    specialties = html.xpath("//div[4]/div[1]/ul/li/div[1]/div[5]")
    #将所有的div标签都匹配出来然后在匹配里边的span
    for x in specialties:
        x_detail = x.xpath("./span[1]/text()")
        if x.xpath("./span[2]/text()"):
            x_detail += x.xpath("./span[2]/text()")
        else:
            pass
        if x.xpath("./span[2]/text()"):
            x_detail += x.xpath("./span[3]/text()")
        else:
            pass
        specialty.append(x_detail)
    # 总价d
    total_price = html.xpath("//div[4]/div[1]/ul/li/div[1]/div[6]/div[1]/span/text()")
    # 单价d
    average_price = html.xpath("//div[4]/div[1]/ul/li/div[1]/div[6]/div[2]/span/text()")
    item = []
    for x in range(0,30):
        info = {
            "title" : title[x],
            "department" : department[x],
            "style" :style[x],
            "area" : area[x],
            "towards" : towards[x],
            "district" : district[x],
            "build_type": build_type[x].split()[0],
            "total_price":total_price[x],
            "average_price":re.findall("\d{4,6}",average_price[x]),
            "release_time":release_time[x],
            "show_time": re.findall("\d{1,3}",show_time[x]),
            "focus":focus[x],
            "decorate":decorate[x],
            "specialty":"".join(specialty[x])
        }
        item.append(info)
    return write2sql(item)


# 将所有的数据写入数据库
def write2sql(item):
    dbhelper = DbHelper()
    for x in item:
        title = x["title"]
        department = x["department"]
        style = x["style"]
        area = x["area"]
        towards = x["towards"]
        district = x["district"]
        specialty = x["specialty"]
        build_type = x["build_type"]
        total_price = x["total_price"]
        average_price = x["average_price"][0]
        release_time = x["release_time"]
        show_time = x["show_time"][0]
        focus = x["focus"]
        decorate = x["decorate"]

        sql = "INSERT INTO newdatabase.lianjia_ershou(title, department,style, area, towards, district,specialty, build_type,total_price,show_time,decorate,focus,average_price,release_time) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        params = (title, department,style, area, towards, district,specialty, build_type,total_price,show_time,decorate,focus,average_price,release_time)
        result = dbhelper.execute(sql, params)
        if result == True:
            print("插入成功")
        else:
            print("插入失败", params)

def main():
    for x in range(1, 101):
        url = "https://xa.lianjia.com/ershoufang/pg{}/".format(x)
        request_page(url)
        time.sleep(random.randint(10, 20))

if __name__ == "__main__":
    main()
