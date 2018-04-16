#!/usr/bin/python
# -*- coding: utf-8 -*-
from scrapy import Request
from scrapy.spider import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from mzitu.items import MzituItem
import time
import random

class MMspider(CrawlSpider):
	"""docstring for MMspider"""
	name = 'mzitu'
	allowed_domains = ['www.mzitu.com']
	start_urls = ['http://www.mzitu.com/']
	rules = (
		Rule(LinkExtractor(allow=(r'/xinggan/page/\d+')),follow=True),
		Rule(LinkExtractor(allow=(r'/\d{1,6}',),deny=(r'/\d{1,6}/\d{1,6}')),callback='parse_item',follow=True),
		)
 
	def parse_item(self,response):
		header = {
			"User-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
		}
		item = MzituItem()
		item["name"] = response.css(".main-title::text").extract()	
		item["url"] = response.url
		item['image_urls'] = response.css(".main-image img::attr(src)").extract()
		time.sleep(random.randint(3,6))		
		yield Request(response.url,headers=header)
		yield item
