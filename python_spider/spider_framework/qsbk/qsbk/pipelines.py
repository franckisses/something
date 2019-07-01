# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
from scrapy.exporters import JsonItemExporter,JsonLinesItemExporter

class QsbkPipeline(object):
    def __init__(self):
        self.fp = open("duanzi.json","w",encoding="utf-8")

    def open_spider(self,spider):
        print("爬虫开始")

    def process_item(self, item,spider):
        item_json = json.dumps(item)
        print(item_json)
        self.fp.write(item_json+"\n")
        return item

    def close_spider(self,spider):
        self.close()
        print("爬虫结束")


# 第二方法
# import json
from scrapy.exporters import JsonItemExporter
# class QsbkPipeline(object):
    # def __init__(self):
    #     self.fp = open("duanzi.json","wb")
    #     self.exporter = JsonItemExporter(self.fp,ensure_ascii = False,encoding = "utf-8")
    #     self.exporter.start_exporting()
    #
    # def open_spider(self):
    #     print("爬虫开始")
    #     pass

    # def process_item(self, item, spider):
        # item_json = json.dumps(item)
        # self.fp.write(dict(item_json)+"\n")
        # return item
        # pass

    # def close_spider(self):
    #     self.exporter.finish_exporting()
    #     self.fp.close()
    #     print("爬虫结束")

# import json
# from scrapy.exporters import JsonLinesItemExporter
# class QsbkPipeline(object):
#     def __init__(self):
#         self.fp = open("duanzi.json","wb")
#         self.exporter = JsonLinesItemExporter(self.fp,ensure_ascii = False,encoding = "utf-8")
#
#     def open_spider(self):
#         print("爬虫开始")
#         pass
#
#     def process_item(self, item, spider):
#         item_json = json.dumps(item)
#         self.fp.write(dict(item_json)+"\n")
#         return item
#
#     def close_spider(self):
#         self.fp.close()
#         print("爬虫结束")