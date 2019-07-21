#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 # 这里不能运行，不知道为什么？？？，教程里是可以的
 # 问题已解决，是 pip 和 conda 安装的scrapy,是不一样的，环境设为py3.6版本，用conda install scrapy 重新安装的
from scrapy import cmdline
cmdline.execute("scrapy crawl qsbk_splider".split())
# cmdline.execute(["scrapy",'crawl','qsbk_splider'])
