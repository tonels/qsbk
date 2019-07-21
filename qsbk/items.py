# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QsbkItem(scrapy.Item):
    # define the fields for your item here like:
    author = scrapy.Field() # 固定写法
    content = scrapy.Field() # 固定写法,就可以把这个数据模型引入到piplines中，优化代码
