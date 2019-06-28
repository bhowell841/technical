#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 18:56:33 2019

@author: brendanhowell
"""

import scrapy

class FirstSpider(scrapy.Spider):
    name = "firstSpider"
    
    def start_requests(self):
        urls = [
                'https://www.amazon.com/GoPro-Fusion-Waterproof-Digital-Spherical/dp/B0792MJLNM/ref=sr_1_3?crid=D3C7EDM435E7&keywords=gopro+fusion&qid=1550442454&s=electronics&sprefix=GoPro+Fu%2Celectronics%2C1332&sr=1-3',
        ]
        for url in urls:
                    yield scrapy.Request(url=url, callback=self.parse)
                    
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'goPro-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename) 
        