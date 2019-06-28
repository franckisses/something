# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      robots_test
   Description :     
   Author :         gongyan
   Date：           2019/2/27
   Change Activity: 2019/2/27 6:41
-------------------------------------------------
"""
from urllib import robotparser

rp = robotparser.RobotFileParser()
rp.set_url('http://www.dongqiudi.com')
rp.read()
print(rp.can_fetch("*",'https://www.dongqiudi.com/archive/918057.html'))