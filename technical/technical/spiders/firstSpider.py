#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 18:56:33 2019

@author: brendanhowell
"""
#import pymongo
import scrapy
from ..items import AmazonItem

class FirstSpider(scrapy.Spider):
    name = "firstSpider"
    pageNumber = 2
    start_urls = [
        'https://www.amazon.com/GoPro-Fusion-Waterproof-Digital-Spherical/product-reviews/B0792MJLNM/ref=cm_cr_getr_d_paging_btm_next_8?ie=UTF8&reviewerType=all_reviews&pageNumber=1'
    ]
    
    def parse(self, response):
        
        items = AmazonItem()
        
        all_reviews = response.css('#cm_cr-review_list')
                          
        for review in all_reviews:
            #review_id = review.css('#cm_cr-review_list .a-profile-name').css('::text').extract()
            #review_title = review.css('.a-text-bold span').css('::text').extract()
            #review_date = review.css('.review-date::text').extract()
            #review_stars = review.css('.a-icon-alt::text').extract()
            review_stars = all_reviews.css('.review-rating').extract()
            #review_text = review.css('.a-spacing-small.review-data , .review-text-content spann').css('::text').extract()
            review_text = all_reviews.css('.review-text').extract()
            
            #items['review_id'] = review_id
            #items['review_title'] = review_title
            #items['review_date'] = review_date
            items['review_stars'] = review_stars
            items['review_text'] = review_text
            
            yield items
        '''
        items = AmazonItem()
        
        review_id = response.css('#cm_cr-review_list .a-profile-name').css('::text').extract()
        review_title = response.css('.a-text-bold span').css('::text').extract()
        review_date = response.css('.review-date::text').extract()
        review_stars = response.css('.a-icon-alt::text').extract()
        review_text = response.css('.a-spacing-small.review-data , .review-text-content spann').css('::text').extract()
        
                                   
        items['review_id'] = review_id
        items['review_title'] = review_title
        items['review_date'] = review_date
        items['review_stars'] = review_stars
        items['review_text'] = review_text
        
        yield items
    '''
        next_page = 'https://www.amazon.com/GoPro-Fusion-Waterproof-Digital-Spherical/product-reviews/B0792MJLNM/ref=cm_cr_getr_d_paging_btm_next_8?ie=UTF8&reviewerType=all_reviews&pageNumber=' + str(FirstSpider.pageNumber)
        if FirstSpider.pageNumber <= 8:
            FirstSpider.pageNumber += 1
            yield response.follow(next_page, callback = self.parse)
  