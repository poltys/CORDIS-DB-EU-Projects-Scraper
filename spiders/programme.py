# -*- coding: utf-8 -*-
import scrapy


class ProgrammeSpider(scrapy.Spider):
    name = 'programme'
    allowed_domains = ['cordis.europa.eu']
    start_urls = ['http://cordis.europa.eu/projects/result_en?q=(relatedProgramme/programme/code%3D%27H2020-EU.1.1.*%27%20OR%20relatedSubProgramme/programme/code%3D%27H2020-EU.1.1.*%27)%20AND%20contenttype%3D%27project%27']

    def parse(self, response):
        pass
