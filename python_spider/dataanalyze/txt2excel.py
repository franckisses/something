# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     txt2excel
   Description :
   Author :       gongyan
   date：          2018/12/17
   Change Activity:2018/12/17 9:31:
-------------------------------------------------
"""

# this file is exchange txt to excel!

import csv
import xlsxwriter

with open('new.txt','r',encoding="utf-8") as f:
    linelist = f.readlines()
    for line in linelist:

        with open('data.xlsx','a',newline="") as csvfile:  #如果在这不加newline=“” 会出现内容之间有空行
            writer = csv.writer(csvfile)
            line =line.split(" ")
            newlist=line.pop().strip()
            line.append(newlist)
            writer.writerow(line)

