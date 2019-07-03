# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 18:56:33 2019

@author: brendanhowell
"""

import scrapy
from ..items import AmazonItem

class SecondSpider(scrapy.Spider):
    name = "secondSpider"
    
    pageNumber = 2
    start_urls = [
        'https://www.amazon.com/GoPro-Fusion-Waterproof-Digital-Spherical/product-reviews/B0792MJLNM/ref=cm_cr_getr_d_paging_btm_next_8?ie=UTF8&reviewerType=all_reviews&pageNumber=1'
    ]
    
    def parse(self, response):
        
        items = AmazonItem()
        
        all_reviews = response.css('#cm_cr-review_list')
       
        for review in all_reviews:
            review_id = review.css('.a-profile-name').css('::text').extract()
            review_title = review.css('.a-text-bold span').css('::text').extract()
            #review_title = review.css('.review-title').extract()
            review_date = review.css('.review-date::text').extract()
            #review_date = review.css('.review-date::text').extract()
            review_stars = review.css('.a-icon-alt::text').extract()
            #review_stars = review.css('.review-rating').extract()
            #review_text = review.css('.a-spacing-small.review-data , .review-text-content spann').css('::text').extract()
            review_text = review.css('.review-text').extract()
            
            items['review_id'] = review_id
            items['review_title'] = review_title
            items['review_date'] = review_date
            items['review_stars'] = review_stars
            items['review_text'] = review_text
            
            yield items
            
            NEXT_PAGE_SELECTOR = '.a-last a ::attr(href)'
            next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
            if next_page:
                yield scrapy.Request(
                        response.urljoin(next_page),
                        callback=self.parse
                )
            
            '''
            next_page = 'https://www.amazon.com/GoPro-Fusion-Waterproof-Digital-Spherical/product-reviews/B0792MJLNM/ref=cm_cr_getr_d_paging_btm_next_8?ie=UTF8&reviewerType=all_reviews&pageNumber=' + str(SecondSpider.pageNumber)
            if SecondSpider.pageNumber <= 8:
                SecondSpider.pageNumber += 1
                yield response.follow(next_page, callback = self.parse)
            '''