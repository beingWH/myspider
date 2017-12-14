# -*- coding: utf-8 -*-
from urllib import parse
from urllib.parse import urljoin

import scrapy
from scrapy import Spider
from scrapy_splash import SplashRequest
from scrapy import Request
from scrapy.selector import  Selector
from ..items import CenelecItem


script="""
    function main(splash, args)
      splash.images_enabled=false
      assert(splash:go(args.url))
      assert(splash:wait(args.wait))
      js = string.format("document.querySelector('#KEYWORDS_AND').value=%s;document.querySelector('#tformsub1').click()", args.searchtxt)
      splash:evaljs(js)
      assert(splash:wait(args.wait))
      return {
        html = splash:html()
      }
    end
"""


class CenelecspiderSpider(scrapy.Spider):
    name = 'cenelecspider'
    allowed_domains = ['www.cenelec.eu']
    base_url = 'http://www.cenelec.eu/dyn/www/f?p=104:105:1321922947089454::::FSP_LANG_ID:25'
    data_url='https://www.cenelec.eu/dyn/www/'

    def start_requests(self):
        searchtxt="'EN 61000-4-5'"
        yield SplashRequest(self.base_url,callback=self.parse,endpoint='execute',args={'lua_source':script,'searchtxt':searchtxt,'wait':10})

    def parse(self, response):
        for sel in  response.css('#DASHBOARD_LISTTCPUBS > table > tbody >tr'):
            data_url=urljoin(self.data_url,sel.xpath('.//td[2]//a/@href')[0].extract())
            yield Request(data_url,callback=self.parse_data)

    def parse_data(self,response):
        slectorlist=response.css('#DASHBOARD_LISTPROJECT>table>tr')
        item=CenelecItem()
        item['Reference']=slectorlist[0].xpath('.//td/text()').extract_first()
        item['Title']=slectorlist[1].xpath('.//td/text()').extract_first()
        item['Abstract']=slectorlist[3].xpath('.//td/text()').extract_first()
        item['Status']=slectorlist[4].xpath('.//div/text()').extract_first()
        yield item

