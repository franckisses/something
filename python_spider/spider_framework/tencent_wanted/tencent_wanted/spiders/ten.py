# -*- coding: utf-8 -*-
import scrapy

from tencent_wanted.items import TencentWantedItem


class TenSpider(scrapy.Spider):
    name = 'ten'
    allowed_domains = ['hr.tencent.com']  #设置域名范围
    base_url = "https://hr.tencent.com/position.php?&start="
    offset = 0
    start_urls = [base_url + str(offset)+"#a"]

    def parse(self, response):
        item = TencentWantedItem()
        node_list = response.xpath("//tr[@class='even'] | //tr[@class='odd']")
        for node in node_list:
            item["title"] = node.xpath(".//a/text()").get()
            item["positionLink"] = "https://hr.tencent.com/" + node.xpath(".//a/@href").get()
            item["positionType"]  = node.xpath("./td[2]/text()").get()
            item["positionNum"] = node.xpath("./td[3]/text()").get()
            item["positionLocation"] = node.xpath("./td[4]/text()").get()
            item["pubTime"] = node.xpath("./td[5]/text()").get()
            yield item

        if self.offset < 2801:
            self.offset+=10
            new_url = self.base_url + str(self.offset) + "#a"
            yield scrapy.Request(new_url, callback=self.parse) #对新的网页请求你，以及设置回调函数解析网页
        else:
            return




