# -*- coding: utf-8 -*-

import scrapy
from ..items import *
from lxml import etree



class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    # start_urls = ['http://hr.tencent.com/']
    start_urls = ["https://hr.tencent.com/position.php?&start=0#a"]

    # for i in range(0,510,10):
    #     start_urls.append("https://hr.tencent.com/position.php?&start={}#a".format(i))

    # 提取数据的逻辑 这里接收的是HTTP Response
    def parse(self, response):
        # 把真实的要保存的数据上传,
        for each in response.xpath("//tr[@class = 'even']|//tr[@class = 'odd']|"):
            item = TencentSpider()
            item["positionName"] = each.xpath("./td[1]/a/text()").extract()[0]
            item["positionLink"] = "http://hr.tencent.com/"+each.xpath("//td[1]/a/@href").extract()[0]
            item["positionType"] = each.xpath("//td[2]/text()").extract()[0]
            yield item



