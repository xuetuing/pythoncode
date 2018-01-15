#!/usr/bin/python
# -*- coding: utf-8 -*-
from scrapy import Request
from scrapy.spider import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from mzitu.items import MzituItem

class MMspider(CrawlSpider):
	"""docstring for MMspider"""
	name = 'mzitu'
	allowed_domains = ['mzitu.com']
	start_urls = ['http://www.mzitu.com/']
	img_urls = []
	rules = (Rule(LinkExtractor(allow=(r'http://www.mzitu.com/\d{1,5}',),deny=(r'http://www.mzitu.com/\d{1,6}/\d{1,6}')),callback='parse_item',follow=True),)
 
	def parse_item(self,response):
		item = MzituItem()
		max_num = response.xpath("/html/body/div[2]/div[1]/div[4]/a[5]/span/text()").extract()
		item['name'] = response.xpath("/html/body/div[2]/div[1]/h2/text()").extract()
		item['url'] = response.url
		for num in range(1,3):
			page_url = response.url + '/' + str(num)
			yield Request(page_url,callback=self.img_url)
		item['image_urls'] = self.img_urls
		yield item

	def img_url(self,response):
		imge_urls = response.xpath("/html/body/div[2]/div[1]/div[3]/p/a/img/@src").extract()
		for img_url in imge_urls:
			self.img_urls.append(img_url)