import scrapy
from scrapy import Request
from ..items import Gb688Item
import re
from scrapy.linkextractors import LinkExtractor
from  scrapy.selector import Selector

class GB688Spider(scrapy.Spider):
    name = "gb688spider"
    BASE_URL='http://www.gb688.cn/bzgk/gb/newGbInfo?hcno=%s'

    start_urls=['http://www.gb688.cn/bzgk/gb/std_list?p.p1=0&p.p90=circulation_date&p.p91=desc&p.p2=GB%20500']

    def parse(self, response):
        next_urls=response.xpath('//td[@class="mytxt"]/a/@onclick').extract()
        for next_url in next_urls:
            re_url=re.split(r'\'',next_url)
            yield Request(self.BASE_URL % re_url[1],callback=self.parse_gb688)

    def parse_gb688(self,response):
        for sel in response.xpath('//div[@class="bor2"]'):
            gb=Gb688Item()
            gb['Stardard']=sel.xpath('.//h1/text()').extract_first().strip()
            gb['CNname']=sel.xpath('.//table[@class="tdlist"]//td')[0].css('b::text').extract_first().strip()
            gb['ENname']=sel.xpath('.//table[@class="tdlist"]//td')[2].css('td::text').extract_first().strip()
            gb['State']=sel.xpath('.//table[@class="tdlist"]//td')[3].css('span::text').extract_first().strip()
            gb['CSS']=sel.xpath('.//div[@clsss="row detail"]//div')[1].css('div::text').extract_first().strip()
            gb['ICS']=sel.xpath('.//div[@clsss="row detail"]//div')[3].css('div::text').extract_first().strip()
            gb['Issuedate']=sel.xpath('.//div[@clsss="row"]//div')[1].css('div::text').extract_first().strip()
            gb['Enforcedate']=sel.xpath('.//div[@clsss="row"]//div')[3].css('div::text').extract_first().strip()
            gb['ResponseDept']=sel.xpath('.//div[@clsss="row"]//div')[5].css('div::text').extract_first().strip()
            gb['RelevateDept']=sel.xpath('.//div[@clsss="row"]//div')[7].css('div::text').extract_first().strip()
            gb['IssueOrganization']=sel.xpath('.//div[@clsss="row"]//div')[9].css('div::text').extract_first().strip()
            gb['Remarks']=sel.xpath('.//div[@clsss="row"]//div')[12].css('div::text').extract_first().strip()

            yield gb