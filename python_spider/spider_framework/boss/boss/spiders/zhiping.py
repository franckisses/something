# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ZhipingSpider(CrawlSpider):
    name = 'zhiping'
    allowed_domains = ['zhiping.com']
    start_urls = ['https://www.zhipin.com/c101110100/h_101110100/?query=Python&page=1']

    rules = (
        # 匹配列表页的规则
        Rule(LinkExtractor(allow=r'.+\?query=Python&page=\d'),follow=True),
        # 匹配详情页的规则
        Rule(LinkExtractor(allow=r'/job_detail/[0-9a-zA-Z]{27}~\.html'),callback="parse_item",follow=False),

    )


    def parse_item(self, response):
        title = response.xpath("//*[@id='main']/div[1]/div/div/div[2]/div[2]/h1/text()").get()
        print(title)

        # i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i
