# -*- coding: utf-8 -*-
import scrapy


class ProgrammeSpider(scrapy.Spider):
    name = 'programme'
    allowed_domains = ['cordis.europa.eu']
    start_urls = ['http://cordis.europa.eu/projects/home_en.html']

    # BASE_URL = 'http://cordis.europa.eu/projects/'

    def parse(self, response):
        links = response.xpath('//*[@id="cattree"]/div[2]/div[1]/dl/dd[1]/a').extract()
        for link in links:
            absolute_url = self.BASE_URL = link
            yield scrapy.Request(absolute_url, callback=self.parse_attr)

    def parse_attr(self, response):
        item = ProgrammeItem()
        item['link'] = response.url
        yield item
