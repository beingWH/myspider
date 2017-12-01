# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field


class Gb688Item(Item):
    Stardard=Field()
    CNname=Field()
    ENname=Field()
    State=Field()
    CSS=Field()
    ICS=Field()
    Issuedate=Field()
    Enforcedate=Field()
    ResponseDept=Field()
    RelevateDept=Field()
    IssueOrganization=Field()
    Remarks=Field()
