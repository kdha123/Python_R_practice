# -*- coding: utf-8 -*-
import scrapy


class T2Spider(scrapy.Spider):
    name = 't2'
    allowed_domains = ['blog.scrapinghub.com']
    start_urls = ['https://blog.scrapinghub.com/']

    def parse(self, response):
        # print(response.css('div.post-header > h2 > a::text').getall())
        for t in response.css('div.post-header > h2 > a::text').getall():
            yield {
                'title': t
            }
