# -*- coding: utf-8 -*-
import scrapy


class T3Spider(scrapy.Spider):
    name = 't3'
    allowed_domains = ['blog.scrapinghub.com', 'naver.com', 'daum.net']
    # start_urls = ['http://blog.scrapinghub.com/']

    def start_requests(self):
        yield scrapy.Request('https://blog.scrapinghub.com/',self.p1)
        yield scrapy.Request('https://comic.naver.com/webtoon/list.nhn?titleId=183559&weekday=mon',self.p2)
        yield scrapy.Request('https://www.daum.net/',self.p3)

    def p1(self, response):
        for url in response.css('div.post-header > h2 > a::attr("href")').getall():
            print(url)

    # content > table > tbody > tr:nth-child(3) > td.title > a
    def p2(self, response):
        for url in response.css('td.title > a::text').getall():
            print(url)
        # print('p2')


    def p3(self, response):
        print('p3')

    def parse(self, response):
        pass
