# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field


class IecchItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Standard=Field()
    Name=Field()
    PubType=Field()
    PubDate=Field()
    Edition=Field()
    Languages=Field()
    TCSC=Field()
    ICS=Field()
    StabilityDate=Field()
    Abstract=Field()
    Pages=Field()
    Size=Field()