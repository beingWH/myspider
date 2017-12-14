# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.item import Item
import pymongo


class CenelecPipeline(object):
    def process_item(self, item, spider):
        return item

class MongoDBPipeline(object):

    Host='localhost'
    Port=27017
    DB_Name='ScrapyDB'

    def open_spider(self,spider):
        self.client=pymongo.MongoClient(self.Host,self.Port)
        self.db=self.client[self.DB_Name]

    def close_spider(self,spider):
        self.client.close()

    def process_item(self,item,spider):
        collection=self.db[spider.name]
        post=dict(item) if isinstance(item,Item) else item
        collection.insert_one(post)
        return item
