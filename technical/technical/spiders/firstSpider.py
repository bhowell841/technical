#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 18:56:33 2019

@author: brendanhowell
"""

import scrapy
from ..items import AmazonItem

class FirstSpider(scrapy.Spider):
    name = "firstSpider"
   
    start_urls = [
        #'https://www.amazon.com/GoPro-Fusion-Waterproof-Digital-Spherical/product-reviews/B0792MJLNM/ref=cm_cr_getr_d_paging_btm_next_8?ie=UTF8&reviewerType=all_reviews&pageNumber=1'
        'https://www.amazon.com/s?bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&fst=as%3Aoff&qid=1562029045&rnid=1250225011&ref=lp_283155_nr_p_n_publication_date_0'
    ]
    
    def parse(self, response):
        items = AmazonItem()
        
        product_name = response.css('.a-color-base .a-text-normal').css('::text').extract()
        product_author = response.css('.a-color-secondary .a-size-base+ .a-size-base , .a-color-secondary .a-size-base.a-link-normal').css('::text').extract()
        product_price = response.css('.a-spacing-top-small .a-price:nth-child(1) span').css('::text').extract()
        product_imagelink = response.css('.s-image::attr(src)').extract()
        
        items['product_name'] = product_name
        items['product_author'] = product_author
        items['product_price'] = product_price
        items['product_imagelink'] = product_imagelink
        
        yield items
    
    
    