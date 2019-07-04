# -*- coding: utf-8 -*-



import scrapy
from ..items import goProItem

class GoProSpider(scrapy.Spider):
    name = 'goProSpider'
    
    start_urls = [
            'https://www.amazon.com/GoPro-Fusion-Waterproof-Digital-Spherical/dp/B0792MJLNM/ref=sr_1_3?crid=D3C7EDM435E7&keywords=gopro+fusion&qid=1550442454&s=electronics&sprefix=GoPro+Fu%2Celectronics%2C1332&sr=1-3'
    ]
    '''
    #test link
    start_urls = [
            'https://www.amazon.com/GoPro-HERO7-Black-Waterproof-Streaming-Stabilization/dp/B07GDGZCCH/ref=sr_1_3?keywords=gopro&qid=1562169138&s=gateway&sr=8-3'
    ]
    #test link
    start_urls = [
            'https://www.amazon.com/dp/B0785T83KG/ref=sspa_dk_detail_1?psc=1&pd_rd_i=B0785T83KG&pd_rd_w=eQGPN&pf_rd_p=8a8f3917-7900-4ce8-ad90-adf0d53c0985&pd_rd_wg=TqeYY&pf_rd_r=YFVRYQWAQJS9G42JFR3T&pd_rd_r=0b32f18e-9db5-11e9-b8f1-8196756ce61d'
    ]
    '''
    
    def parse(self, response):
    
        items = goProItem()
        amazon = ['Amazon']
        goProPage = response.css('#dp-container')
       
        for info in goProPage:
            productName = info.css('#productTitle::text').extract()
            brand = info.css('#bylineInfo::text').extract()
            source = amazon
            #msrp
            if info.css('.a-text-strike::text'):
                msrp = info.css('.a-text-strike::text').extract()
            elif info.css('#priceblock_ourprice::text'):
                msrp = info.css('#priceblock_ourprice::text').extract()
            else:
                msrp = ['Only available from third party sellers']
            #sale
            if info.css('.a-text-strike::text'):
                sale = info.css('#priceblock_ourprice::text').extract()
            else:
                sale = ['This item is not currently on sale']
            description = info.css('#productDescription p').css('::text').extract()
            rating = info.css('#productDetails_detailBullets_sections1 .a-icon-alt').css('::text').extract()
            reviewNumber = info.css('#dp-summary-see-all-reviews h2').css('::text').extract()
    
            items['productName'] = productName
            items['brand'] = brand
            items['source'] = source
            items['msrp'] = msrp
            items['sale'] = sale
            items['description'] = description
            items['rating'] = rating
            items['reviewNumber'] = reviewNumber
            
            yield items
        