# -*- coding: utf-8 -*-
import scrapy

class DqdSpider(scrapy.Spider):
    name = "DQD"
    allowed_domains = ["dongqiudi.com"]
    start_urls = ['http://dongqiudi.com/archives/1?page=1']

    def parse(self, response):
        html = response.text
        text = json.loads(html)
        dataArray = text['data']
        for data in dataArray:
            yield data

        for i in range(2,50):
            new_url = "http://dongqiudi.com/archives/1?page={}".format(i)
            yield scrapy.Request(url=new_url,callback=self.parse)