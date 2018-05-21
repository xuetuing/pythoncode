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

class UserInfoItem(scrapy.Item):
	# define the fields for your item here like:
	# name = scrapy.Field()
	user_ider = scrapy.Field()
	name = scrapy.Field()
	address = scrapy.Field()
	user_image_url = scrapy.Field()
	profession = scrapy.Field()
	work_exper = scrapy.Field()
	education = scrapy.Field()
	resume = scrapy.Field()
	followees_num = scrapy.Field()
	followers_num = scrapy.Field()

class RelationItem(scrapy.Item):
	user_ider = scrapy.Field()
	relation_type = scrapy.Field()
	relation_id = scrapy.Field()

class YunQiBkListItem(scrapy.Item):
	novel_id = scrapy.Field()
	novel_name = scrapy.Field()
	novellink = scrapy.Field()
	novel_image_url = scrapy.Field()
	Author = scrapy.Field()
	classify = scrapy.Field()
	status = scrapy.Field()
	update_time = scrapy.Field()
	words = scrapy.Field()
	resume = scrapy.Field()

class YunQiBkDetailItem(scrapy.Item):
	novelallclick = scrapy.Field()
	novelallpopular = scrapy.Field()
	weekpopular = scrapy.Field()
	#novelcomments = scrapy.Field()