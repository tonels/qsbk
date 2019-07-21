# -*- coding: utf-8 -*-
import scrapy
from qsbk.items import QsbkItem
from scrapy.http.response.html import HtmlResponse
from scrapy.selector.unified import SelectorList

class QsbkSpliderSpider(scrapy.Spider):
    name = 'qsbk_splider' #
    allowed_domains = ['qiushibaike.com'] #限制爬虫范围
    start_urls = ['https://www.qiushibaike.com/text/page/1/'] # 运行时，发送请求给调度器，再给引擎，再下载器，再引擎

    def parse(self, response):
        duanzidiv = response.xpath("//div[@id='content-left']/div")
        for dz in duanzidiv:
            author = dz.xpath(".//h2/text()").get().strip()
            content = dz.xpath(".//div[@class='content']//text()").getall()
            content = ''.join(content).strip()
            # print(author)
            # print(content)
            # duanzi2_ = {'author': author, 'content': content}
            item = QsbkItem(author=author, content=content) # 可以这样简化写
            yield item # 将数据移交给 piplines

