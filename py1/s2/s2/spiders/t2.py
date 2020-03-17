# -*- coding: utf-8 -*-
import scrapy


class T2Spider(scrapy.Spider):
    name = 't2'
    allowed_domains = ['blog.scrapinghub.com', 'naver.com', 'daum.net']
    start_urls = ['https://blog.scrapinghub.com/',
                  'https://comic.naver.com/webtoon/list.nhn?titleId=183559&weekday=mon','https://daum.net']

    def parse(self, response):
        if response.url.find('scrapinghub'):
            for url in response.css('div.post-header > h2 > a::attr("href")').getall():
                print(url)
        elif response.url.find('naver'):
            for url in response.css('td.title > a::text').getall():
                print(url)
        else:
            print('다음')
        # print(response.url)
