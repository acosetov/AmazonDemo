# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazoncleaningItem(scrapy.Item):
    
    product_name = scrapy.Field()
    product_url = scrapy.Field()
    product_image = scrapy.Field()
    product_price = scrapy.Field()
    pass
