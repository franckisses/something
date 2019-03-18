# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 15:32:42 2018

@author: gongyan
"""

from urllib import request,error

try:
    response = request.urlopen('http://www.dongqiudi.com/wosh')
except error.URLError as e:
    print(e.reason,e.code,e.headers)
    