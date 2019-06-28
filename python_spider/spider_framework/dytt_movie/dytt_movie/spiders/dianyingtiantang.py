# -*- coding: utf-8 -*-
import scrapy

class DianyingtiantangSpider(scrapy.Spider):
    name = "dianyingtiantang"
    allowed_domains = ["https://www.dytt8.net/"]
    start_urls = ['http://www.dytt8.net/']

    def parse(self, response):
        pass
