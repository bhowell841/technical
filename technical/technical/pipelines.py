# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

class TechnicalPipeline(object):
    
    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['goproreviews']
        self.collection = db['reviews_tb']
        
        
    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item
