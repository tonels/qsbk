# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# 将爬虫文件传的数据，处理
import json


class QsbkPipeline(object):

    def __init__(self):
        self.fp = open('duanzi.json','w',encoding='utf-8')
        super().__init__()

    def process_item(self, item, spider):
        item_json = json.dumps(dict(item),ensure_ascii=False) # 直接传item,不会直接解析成json,先转化为词典dict
        self.fp.write(item_json + '\n')
        return item

    def open_splider(self,splider):
        print('爬虫开始')

    def close_splider(self, splider):
        self.fp.closed()
        print('爬虫结束了')

