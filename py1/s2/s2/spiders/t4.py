# -*- coding: utf-8 -*-
import scrapy


class T4Spider(scrapy.Spider):
    name = 't4'
    allowed_domains = ['w3schools.com']
    start_urls = ['http://w3schools.com/']

    def parse(self, response):
        for url in response.css('#mySidenav > div > a::text').getall():
            yield {'url':url}


