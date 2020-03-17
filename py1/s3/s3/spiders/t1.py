# -*- coding: utf-8 -*-
import scrapy


class T1Spider(scrapy.Spider):
    name = 't1'
    allowed_domains = ['itnews.com']
    start_urls = ['http://itnews.com/']

    def parse(self, response):
        pass
