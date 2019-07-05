# -*- coding: utf-8 -*-


import scrapy
from ..items import AmazonItem

class SecondSpider(scrapy.Spider):
    name = "practiceSpider"
   
    custom_settings = {
        'COLLECTION_NAME' : 'reviews_tb'
    }
    
    start_urls = [
        'https://www.amazon.com/GoPro-Fusion-Waterproof-Digital-Spherical/product-reviews/B0792MJLNM/ref=cm_cr_getr_d_paging_btm_next_8?ie=UTF8&reviewerType=all_reviews&pageNumber=1'
    ]
    
    def parse(self, response):
        
        #all_reviews = response.css('#cm_cr-review_list')
        
        #for review in all_reviews:
        for review in response.css('#cm_cr-review_list'):
            
            items = AmazonItem()
            #items['review_id'] = review.css('[id^="customer_review-"]')
            items['review_reviewer'] = review.css('.a-profile-name::text').extract()
            items['review_title'] = review.css('.a-text-bold span').css('::text').extract()
            items['review_date'] = review.css('.review-date::text').extract()
            items['review_stars'] = review.css('.a-icon-alt::text').extract()
            items['review_text'] = review.css('.review-text').css('::text').extract()
             
            yield items
           
        '''    
        NEXT_PAGE_SELECTOR = '.a-last a ::attr(href)'
        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        if next_page:
            yield scrapy.Request(
                    response.urljoin(next_page),
                    callback=self.parse
            )
        ''' 
            