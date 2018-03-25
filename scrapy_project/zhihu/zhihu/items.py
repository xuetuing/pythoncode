# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# class ZhihuItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass

class LgjobItem(scrapy.Item):
	# define the fields for your item here like:
	# name = scrapy.Field()
	title = scrapy.Field()
	url_id = scrapy.Field()
	exper = scrapy.Field()
	address = scrapy.Field()
	company = scrapy.Field()
	salary = scrapy.Field()
	pub_time = scrapy.Field()