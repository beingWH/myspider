import scrapy
from scrapy import Request
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from ..items import IecchItem



class IECCHSpider(scrapy.Spider):
    name = "iecchspider"

    BASE_URL="https://webstore.iec.ch%s"
    iec_names=['IEC 50','CISPR 16','IEC 61000','IEC 801','CISPR 14','CISPR 11','CISPR 17','CISPR 18','CISPR 22','CISPR 24','CISPR 13','CISPR 20'
        ,'IEC 728','CISPR 12','CISPR 15','CISPR 19','IEC 1008','IEC 1009']

    BASE_START_URL="https://webstore.iec.ch/searchkey&RefNbr=&tag=&key=%s&RefNbr=&RefHeader=&ComNumber=&ICSNumber=&typepub=&vap=&From=&To=&start=1&MAX=10&FUZZY=0?_=1512128841725#"

    start_urls=[BASE_START_URL % 'IEC 60601']

    def parse(self, response):
        next_urls=response.xpath('//ul[@class="search-results lined-list"]//li/a/@href').re('^/\w+/\d+$')
        for next_url in next_urls:
            yield Request(self.BASE_URL % next_url.strip(),callback=self.parse_iecch)

        for iec_name in self.iec_names:
            yield Request(self.BASE_START_URL % iec_name,callback=self.parse)


    def parse_iecch(self,response):
        item=IecchItem()
        details=response.xpath('//div[@id="details"]//td/span/text()').extract()
        item['Standard']=response.xpath('//h1/span[@itemprop="productID"]/text()').extract_first()
        item['Name']=response.xpath('//h2[@itemprop="name"]/text()').extract_first()
        item['Abstract']=response.xpath('//span[@itemprop="description"]/text()').extract_first()
        if len(details)==7:
            item['PubType'] = details[0]
            item['PubDate'] = details[1]
            item['Edition'] = details[2]
            item['Languages'] = details[3]
            item['StabilityDate'] = details[4]
            item['Pages'] = details[5]
            item['Size'] = details[6] + 'KB'
        else:
            item['PubType'] = details[0]
            item['PubDate'] = details[1]
            item['Edition'] = details[2]
            item['Languages'] = details[3]
            # item['StabilityDate'] = details[4]
            item['Pages'] = details[4]
            item['Size'] = details[5] + 'KB'

        item['TCSC']=response.xpath('//*[@id="details"]/table/tbody/tr[5]/td/a/text()').extract()
        item['ICS']=response.xpath('//*[@id="details"]/table/tbody/tr[6]/td/a/text()').extract()
        yield item




