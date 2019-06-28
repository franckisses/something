# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class TencentWantedPipeline(object):
    """
    定义爬取数据的存储方式
    """
    def process_item(self, item, spider):
        with open("tencent.json","a") as f:
            f.write(json.dumps(dict(item),ensure_ascii=False)+"\n")
            return item