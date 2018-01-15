# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
import re

class MzituPipeline(ImagesPipeline):
	def file_path(self,request,response=None,info=None):
		item = request.meta['item']
		folder = item['name']
		folder_strip = strip(folder)
		image_guid = request.url.split('/')[-1]
		filename = u'full/{0}/{1}'.format(folder.strip,image_guid)
		return filename
	def get_media_requests(self,item,info):
		for img_url in item['image_urls']:
			referer = item['url']
			yield Request(img_url,meta={'item':item,'referer':referer})
		
	def item_completed(self, results, item,info):
		image_paths = [x['path'] for ok,x in results if ok]
		if not image_paths:
			raise DropItem("Item contains no images")
		return item

def strip(path):
	path = re.sub(r'[?\\*|"<>:/]', '', str(path))
	return path

if __name__ == "__main":
	a = 'it is a ?\*|"<>:/ error str' 
	print(strip(a))
	