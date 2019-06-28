# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class DyttSpiderSpider(CrawlSpider):
    name = 'dytt_spider'
    allowed_domains = ['dytt8.net']
    start_urls = ['http://www.dytt8.net/html/gndy/dyzz/index.html']

    rules = (
        Rule(LinkExtractor(allow=r'list_23_\d+.html'), follow=True),
        Rule(LinkExtractor(allow=r'html/gndy/dyzz/\d{8}/\d+.html'), callback='parse', follow=False),
    )

    def parse(self, response):
        print(response.text)

        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
