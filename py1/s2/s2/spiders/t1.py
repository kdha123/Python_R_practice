# -*- coding: utf-8 -*-
import scrapy


class T1Spider(scrapy.Spider):
    name = 't1'
    allowed_domains = ['blog.scrapinghub.com']
    start_urls = ['https://blog.scrapinghub.com/']

    def parse(self, response):
        # print(response.css('div.post-header > h2 > a::attr("href")').getall())
        for url in response.css('div.post-header > h2 > a::attr("href")').getall():
            # print(url)
            yield scrapy.Request(url,self.detail_content)

    def detail_content(self, response):
        # print('-'*5)
        # print(response.body())
        content = response.css('div.post-body > span > p::text').get()
        yield {'content' : content}
        # print(content)
