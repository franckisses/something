# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 16:16:45 2018

@author: gongyan
"""

from urllib.robotparser import RobotFileParser

rp = RobotFileParser()
rp.set_url("http://www.jianshu.com/robots.txt")
rp.read()
print(rp.can_fetch('*','http://www.jianshu.com/p/b67554025d7d'))
print(rp.can_fetch('*','http://www.jianshu.com/search?q=python&page=1&type=collections'))