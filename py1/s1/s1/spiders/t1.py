# -*- coding: utf-8 -*-
import scrapy


class T1Spider(scrapy.Spider):
    name = 't1'
    allowed_domains = ['scrapinghub.com']
    start_urls = ['https://scrapinghub.com//']
    def parse(self, response):
        print(response.status)
        print(response.body)
