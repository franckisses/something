# -*- coding: utf-8 -*-
import scrapy
from qsbk.items import QsbkItem
from scrapy.http.response.html import HtmlResponse
from scrapy.selector.unified import SelectorList



class QsbkDetailSpider(scrapy.Spider):
    name = 'qsbk_detail'
    allowed_domains = ['qiushibaike.com']
    base_domian = ["http://www.qiushibaike.com/"]
    start_urls = ['http://www.qiushibaike.com/text/page/1/']


    def parse(self, response):
        duanzidivs = response.xpath("//div[@id='content-left']/div")
        for duanzi in duanzidivs:
            author = duanzi.xpath(".//h2/text()").get().strip()
            content = duanzi.xpath(".//div[@class ='content']//text()").getall()
            content = "".join(content).strip()
            print(author)
            print(content)
            # item = QsbkItem(author=author,content=content)
            # print(tiem)

            # joker = {
            #     "auther":author,
            #     "content":content
            # }
        # yield item
        # next_url = response.xpath("//ul[@class= 'pagination']/li[last()]/a/@hred").get()
        # if not next_url:
        #     return
        # else:
        #     yield scrapy.Request(self.base_domian+next_url,callback=self.parse)