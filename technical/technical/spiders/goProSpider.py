# -*- coding: utf-8 -*-



import scrapy
from ..items import goProItem

class GoProSpider(scrapy.Spider):
    name = 'goProSpider'
    start_urls = [
            'https://www.amazon.com/GoPro-Fusion-Waterproof-Digital-Spherical/dp/B0792MJLNM/ref=sr_1_3?crid=D3C7EDM435E7&keywords=gopro+fusion&qid=1550442454&s=electronics&sprefix=GoPro+Fu%2Celectronics%2C1332&sr=1-3'
    ]
    
    def parse(self, response):
    
        items = goProItem()
        amazon = ['Amazon']
        goProPage = response.css('#dp-container')
       
        for info in goProPage:
            productName = info.css('#productTitle::text').extract()
            brand = info.css('#bylineInfo::text').extract()
            source = amazon
            if info.css('#priceblock_ourprice::text'):
                msrp = info.css('#priceblock_ourprice::text').extract()
            else:
                msrp = ['Only available from third party sellers']
            #sale = info.css('').extract()
            description = info.css('#productDescription p').css('::text').extract()
            rating = info.css('#productDetails_detailBullets_sections1 .a-icon-alt').css('::text').extract()
            reviewNumber = info.css('#dp-summary-see-all-reviews h2').css('::text').extract()
    
            items['productName'] = productName
            items['brand'] = brand
            items['source'] = source
            items['msrp'] = msrp
            #items['sale'] = sale
            items['description'] = description
            items['rating'] = rating
            items['reviewNumber'] = reviewNumber
            
            yield items
        