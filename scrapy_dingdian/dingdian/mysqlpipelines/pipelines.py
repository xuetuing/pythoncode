# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from .sql import *    # should use '*',not 'Sql'
from dingdian.items import DingdianItem

class DingdianPipeline(object):
	def process_item(self,item,spider):
		if isinstance(item, DingdianItem):
			name_id = item['name_id']
			ret = Sql.select_name(name_id)
			if ret[0] == 1:
				print('have exist.')
				pass
			else:
				xs_name = item['name']
				xs_author = item['author']
				category = item['category']
				Sql.insert_dd_name(xs_name, xs_author, xs_name, name_id)
				print('start save the title of novel.')

