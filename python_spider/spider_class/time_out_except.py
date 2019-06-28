# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 14:33:28 2018

@author: gongyan
"""

import socket
import urllib.request
import urllib.error

try:
    response = urllib.request.urlopen('http://httpbin.org',timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print('TIME OUT')
        
