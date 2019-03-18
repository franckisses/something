# -*- coding:utf-8 -*-
from selenium import webdriver
from fake_useragent import UserAgent

web = webdriver.Chrome()
headers = {
	"User-Agent": UserAgent().Chrome
}

web.get('http://www.jd.com')

web.save_screenshot('haha.png')   #用来截屏并进行保存！

web.close()