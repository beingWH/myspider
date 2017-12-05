import scrapy
from scrapy import Request
from ..items import Gb688Item
import re
from scrapy.linkextractors import LinkExtractor
from  scrapy.selector import Selector

class GB688Spider(scrapy.Spider):
    name = "gb688spider"
    BASE_URL='http://www.gb688.cn/bzgk/gb/newGbInfo?hcno=%s'
    BASE_START_URL='http://www.gb688.cn/bzgk/gb/std_list?p.p1=0&p.p90=circulation_date&p.p91=desc&p.p2=%s'

    start_urls=[BASE_START_URL % 'GB/T 14886' ]
    gb_names=['GB/T 2423.1','GB/T 2423.2','GB/T 2423.5','GB/T 2423.6','GB/T 2423.10','GB/T 2423.17','GB/T 2423.22','GB/T 2423.34','GB/T 2423.50','GB 4824','GB/T 5095.2','GB 9254','GB/T 10125'
             ,'GB 14048.4','GB 14048.5','GB/T 17618','GB 17625.1','GB 17625.2','GB/T 17625.7','GB/T 17626.2','GB/T 17626.3','GB/T 17626.4','GB/T 17626.5','GB/T 17626.6','GB/T 17626.8','GB/T 17626.11'
             ,'GB/T 17626.16','GB/T 17626.29','GB/T 17627.1','GB/T 17627.2','GB 19212.1','GB/T 24807','GB/T 24808','GB/T 25000.51']

    def parse(self, response):
        next_urls=response.xpath('//td[@class="mytxt"]/a/@onclick').extract()
        for next_url in next_urls:
            re_url=re.split(r'\'',next_url)
            yield Request(self.BASE_URL % re_url[1],callback=self.parse_gb688)

        for gb_name in self.gb_names:
            yield Request(self.BASE_START_URL % gb_name,callback=self.parse)


    def parse_gb688(self,response):
        for sel in response.xpath('//div[@class="bor2"]'):
            gb=Gb688Item()
            gb['Stardard']=sel.xpath('.//h1/text()').extract_first().strip()
            gb['CNname']=sel.xpath('.//table[@class="tdlist"]//tr')[0].css('b::text').extract_first().strip()
            gb['ENname']=sel.xpath('.//table[@class="tdlist"]//tr')[1].css('td::text').extract_first().strip()
            gb['State']=sel.xpath('.//table[@class="tdlist"]//tr')[2].css('span::text').extract_first().strip()
            gb['CSS']=sel.xpath('.//div[@clsss="row detail"]//div')[1].css('div::text').extract_first().strip()
            gb['ICS']=sel.xpath('.//div[@clsss="row detail"]//div')[3].css('div::text').extract_first().strip()
            gb['Issuedate']=sel.xpath('.//div[@clsss="row"]//div')[1].css('div::text').extract_first().strip()
            gb['Enforcedate']=sel.xpath('.//div[@clsss="row"]//div')[3].css('div::text').extract_first().strip()
            gb['ResponseDept']=sel.xpath('.//div[@clsss="row"]//div')[5].css('div::text').extract_first().strip()
            gb['RelevateDept']=sel.xpath('.//div[@clsss="row"]//div')[7].css('div::text').extract_first().strip()
            gb['IssueOrganization']=sel.xpath('.//div[@clsss="row"]//div')[9].css('div::text').extract_first().strip()
            gb['Remarks']=sel.xpath('.//div[@clsss="row"]//div')[12].css('div::text').extract_first().strip()

            yield gb


