# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentWantedItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 职位名称
    title = scrapy.Field()
    # 职位链接
    positionLink = scrapy.Field()
    # 职位类型
    positionType = scrapy.Field()
    # 职位人数
    positionNum = scrapy.Field()
    # 工作地点
    positionLocation = scrapy.Field()
    # 发布时间
    pubTime = scrapy.Field()

