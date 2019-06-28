# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     zhihu
   Description :
   Author :       gongyan
   date：          2019/1/21
   Change Activity:2019/1/21 15:28:
-------------------------------------------------
"""

from lxml import etree
import re
import os



# url = 'https://item.jd.com/1686632.html?extension_id=eyJhZCI6IjE0NzYiLCJjaCI6IjIiLCJza3UiOiIxNjg2NjMyIiwidHMiOiIxNTUzMjM3MjIwIiwidW5pcWlkIjoie1wiY2xpY2tfaWRcIjpcImJlY2Q2ZmQ5LTk0ZTktNDQ4Ny1iYzFjLTIxMzUwMDMxZjFjNFwiLFwibWF0ZXJpYWxfaWRcIjpcIjIzMDE0ODU2OFwiLFwicG9zX2lkXCI6XCIxNDc2XCIsXCJzaWRcIjpcImVlMjZmZTJjLWMyNjYtNGRhZi04ODI4LTZkMjBiNTQ5MjUwOFwifSJ9&jd_pop=becd6fd9-94e9-4487-bc1c-21350031f1c4&abt=0'

# result = url.split('.html')[0]
# result1 = result.split("com/")[1]
# print(result1)

if os.path.exists('test.py'):
	print('heheh')