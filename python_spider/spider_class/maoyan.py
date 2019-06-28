# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 19:18:54 2018

@author: gongyan
"""

import requests
import re

def get_one_page(url):
    headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
            }
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        return response.text
    return None

def main():
    url = 'http://maoyan.com/board/4'
    html = get_one_page(url)
    print(type(html))
    #content = re.findall('<dd>.*? board-index.*?>(.*?)</i>',html,re.S)
    with open("maoyan.txt","a",encoding='utf-8') as f:
        f.write(html)
    
    
main()