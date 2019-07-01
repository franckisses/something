# -*- coding: utf-8 -*-

# Define your item pipelines here
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import JsonLinesItemExporter

#JsonLinesItemExporter 这个方法每次生成一个就会存储在硬盘中,不会放在内存中

class WxappPipeline(object):
    def __init__(self):
        self.fp = open("Weixin.json","wb")
        self.exporter = JsonLinesItemExporter(self.fp,ensure_ascii=False,encoding="utf-8")

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self):
        self.fp.close()
