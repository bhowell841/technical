# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    review_id = scrapy.Field()
    review_title = scrapy.Field()
    review_date = scrapy.Field()
    review_stars = scrapy.Field()
    review_text = scrapy.Field()
    
    
    
class goProItem(scrapy.Item):
    productName = scrapy.Field()
    brand = scrapy.Field()
    source = scrapy.Field()
    msrp = scrapy.Field()
    sale = scrapy.Field()
    description = scrapy.Field()
    rating = scrapy.Field()
    reviewNumber = scrapy.Field()
    
    