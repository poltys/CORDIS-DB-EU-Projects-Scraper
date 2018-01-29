# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class CordisItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # EU Project
    Meta = Field()
    Project_ACR = Field()
    Project_Title = Field()
    Total_Cost = Field()
    EU_Contribution = Field()
    Coordinated_in = Field()
    Topic_s = Field()
    Call_for_Proposal = Field()
    Funding_scheme = Field()
    Project_ID = Field()
    To = Field()
    From = Field()
    Partners = Field()
    Country = Field()
    Activity = Field()
    Technology_Description = Field()

    # Housekeeping fields
    url = Field()
    project = Field()
    spider = Field()
    server = Field()
    date = Field()

    # pass
