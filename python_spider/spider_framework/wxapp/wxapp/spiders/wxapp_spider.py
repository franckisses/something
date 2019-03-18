# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from wxapp.items import WxappItem



class WxappSpiderSpider(CrawlSpider):
    name = 'wxapp_spider'
    allowed_domains = ['wxapp-union.com']
    # 开始爬去的网页链接
    start_urls = ['http://www.wxapp-union.com/portal.php?mod=list&catid=2&page=1']

    # 允许爬取的url 第一个url是爬取的网页规则 第二个的是爬取的具体的内容
    rules = (
        Rule(LinkExtractor(allow=r'.+mod=list&catid=2&page=\d+'),follow=True),
        Rule(LinkExtractor(allow=r".+article-.+\.html"),callback="parse_detail",follow=False)
    )

    def parse_detail(self, response):
        # print(response.text)
        title = response.xpath('//*[@id="ct"]/div[1]/div/div[1]/div/div[2]/div[1]/h1/text()').get()
        auther_info = response.xpath('///p[@class="authors"]')
        author = auther_info.xpath('.//a/text()').get()
        pub_time = auther_info.xpath('.//span/text()').get()
        # 爬取内容中所有的文字 并且将其转化为字符串 而且去掉左右的空格
        article_content = response.xpath("//div[@class='content_middle cl']//text()").getall()
        content = "".join(article_content).strip()
        item = WxappItem(title=title,author=author,pub_time=pub_time,content=content)
        yield item




