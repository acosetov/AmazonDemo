# -*- coding: utf-8 -*-
import re
import scrapy
from ..items import AmazoncleaningItem


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    page_number = 2
    start_urls = ['https://www.amazon.com/s?i=specialty-aps&bbn=16225011011&rh=n%3A%2116225011011%2Cn%3A10802561&ref=nav_em_T1_0_4_NaN_15__nav_desktop_sa_intl_cleaning_supplies']

    def parse(self, response):

        items = AmazoncleaningItem()

        product_name = response.xpath('//span[@class="a-size-medium a-color-base a-text-normal"]/text()').extract()
        product_url = response.xpath('//a[@class="a-link-normal a-text-normal"]/@href').extract()
        product_image = response.xpath('//img[@class="s-image"]/@src').extract()

        product_price_all = response.xpath('//span[@class="a-offscreen"]/text()').extract()
        product_price_one = response.xpath('//span[@class="a-color-base"]/text()').extract()
        if product_price_one:
            product_price_all = product_price_one + product_price_all
        

        
        row_data=zip(product_name,product_url,product_image,product_price_all)

        for item in row_data:
            product_name = item[0]
            product_url = 'https://amazon.com'+re.search(r'(.*)/(ref.*)',item[1]).group(1)
            product_image = item[2]
            product_price = item[3].replace("$", "")

            items['product_name'] = product_name
            items['product_url'] = product_url
            items['product_image'] = product_image
            items['product_price'] = float(product_price)

            yield items

            
        
        next_page = 'https://www.amazon.com/s?i=kitchen-intl-ship&bbn=16225011011&rh=n%3A16225011011%2Cn%3A10802561&page=' + str(AmazonSpider.page_number) + '&qid=1582894252&ref=sr_pg_2'

        if AmazonSpider.page_number <= 3:
            AmazonSpider.page_number += 1
            yield response.follow(next_page, callback = self.parse)
