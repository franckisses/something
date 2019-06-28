"""
# -*- coding: utf-8 -*-
# @Time    : 2018/8/17 20:02
# @Author  : franck
# @Email   : franck_gxu@outlook.com
"""

from lxml import etree

with open("test.html","",decode = "gbk") as f:
    a = f.read()
print(type(a))
