# -*-coding:utf-8 -*-
"""
这是一个示例多线程爬取网站的方法！
"""
import time
import threading
from queue import Queue

import requests
from lxml import etree
from fake_useragent import UserAgent


class bsSpider:
	def __init__(self):
		self.baseurl = 'http://www.budejie.com/'
		self.headers = {
			'User-Agent':UserAgent().chrome
			}
		#url队列
		self.urlQueue = Queue()
		#响应队列
		self.resQueue = Queue()

	#生成url的队列
	def getUrl(self):
		for pNum in range(1,50):
			url = self.baseurl + str(pNum)
			self.urlQueue.put(url)

	#响应队列
	def getHtml(self):
		while True:
			url = self.urlQueue.get()
			res = requests.get(url,self.headers)
			res.encoding = 'utf-8'
			html = res.text
			# 放到响应队列中
			self.resQueue.put(html)
			# 清除此任务
			self.urlQueue.task_done()

	#解析页面
	def getContent(self):
		while True:
			# 从响应队列中依次获取html源码
			html = self.resQueue.get()
			parseHtml = etree.HTML(html)
			r_list = parseHtml.xpath('//div[@class="j-r-list-c-desc"]/a/text()')
			for s in r_list:
				print(s+'\n')
			# 清除任务
			self.resQueue.task_done()

	def run(self):
		# 把所有的线程都存放在列表中
		thread_list = []
		#获取url队列
		self.getUrl()
		#创建getpage线程
		for i in range(3):
			thradRes = threading.Thread(target=self.getHtml)
			thread_list.append(thradRes)

		#创建解析线程
		for i in range(2):
			threadParse = threading.Thread(target=self.getContent)
			thread_list.append(threadParse)

		#所有的线程开始干活
		for th in thread_list:
			th.setDaemon(True)
			th.start()

		#如果队列为空。则执行其他程序 此处用来回收进程，队列中为空的时候，进行回收。
		self.urlQueue.join()
		self.resQueue.join()
		print('运行结束')


if __name__ == '__main__':
	begin = time.time()
	spider = bsSpider()
	spider.run()
	end = time.time()
	print(end-begin)