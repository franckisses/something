# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DongqiudiItem(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()
    title = scrapy.Field()
    discription = scrapy.Field()
    user_id = scrapy.Field()
    type = scrapy.Field()
    display_time = scrapy.Field()
    thumb = scrapy.Field()
    comments_total = scrapy.Field()
    web_url = scrapy.Field()
    official_account = scrapy.Field()
