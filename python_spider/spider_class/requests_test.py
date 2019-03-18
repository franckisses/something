# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 14:46:20 2018

@author: gongyan
"""

import requests
from lxml import etree


headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
result = requests.get('https://hr.tencent.com/position.php',headers=headers)
html=result.text
html = etree.HTML(html)
print(html)
trs = html.xpath('//tr[@class="even"]/td/a/text() |//tr[@class="odd"]//td/a/text()')
print(trs)