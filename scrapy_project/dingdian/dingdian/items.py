# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DingdianItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	name = scrapy.Field()
	#the name of novel
	author = scrapy.Field()
	#the author of novel
	novelurl = scrapy.Field()
	#the url of novel
	serialstatus = scrapy.Field()
	#the status of novel
	serialnumber = scrapy.Field()
	#the num of novel
	category = scrapy.Field()
	#the type of novel
	name_id = scrapy.Field()
	#the id of novel

