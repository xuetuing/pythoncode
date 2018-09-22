# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class ZhihuPipeline(object):
	def process_item(self, item, spider):
		return item

class LgjobsqlPipeline(object):
# 采用同步的机制写入MySQL

	def __init__(self):     
		self.conn = pymysql.connect('127.0.0.1', 'xuetu', '123', 'CrawlDB', charset='utf8', use_unicode=True)
		self.cursor = self.conn.cursor()

	def process_item(self, item, spider):
		insert_sql = """
		insert into Article(url_id, title, exper, salary)
		VALUES ("%s", "%s", "%s", "%s")
		ON DUPLICATE KEY UPDATE url_id=VALUES(url_id)
		"""
		self.cursor.execute(insert_sql % (item['url_id'], item['title'], item['exper'], item['salary']))
		self.conn.commit()
		return item

class ZhihuCrawlPipeline(object):
	""" pipeline for mongodb"""
	def __init__(self, mongo_uri,mongo_db):
		self.mongo_uri = mongo_uri
		self.mongo_db = mongo_db

	@classmethod
	def from_crawler(self, crawler):
		return cls(
			mongo_uri = crawler.settings.get('MONGO_URI')
			mongo_db = crawler.settings.get('MONGO_DATABASE','zhihu')
		)

	def open_spider(self, spider):
		self.client = pymongo.MongoClient(self.mongo_uri)
		self.db = self.client[self.mongo_db]
	
	def close_spider(self, spider):
		self.client.close()

	def process_item(self, item,spider):
		if isinstance(item,UserInfoItem):
			self._process_user_item(item)
		else:
			self._process_relation_item(item)
		return item
	
	def _process_user_itme(self, item):
		slef.db.UserInfo.insert(dict(item))

	def _process_relation_itme(self, item):
		slef.db.Relation.insert(dict(item))

class YunQimgoPipeline(object):
	""" pipeline for mongodb"""
	def __init__(self, mongo_uri,mongo_db,replicaset):
		self.mongo_uri = mongo_uri
		self.mongo_db = mongo_db
		self.replicaset = replicaset

	@classmethod
	def from_crawler(self, crawler):
		return cls(
			mongo_uri = crawler.settings.get('MONGO_URI')
			mongo_db = crawler.settings.get('MONGO_DATABASE','zhihu')
			replicaset = crawler.settings.get('REPLICASET')
		)

	def open_spider(self, spider):
		self.client = pymongo.MongoClient(self.mongo_uri,replicaset=self.replicaset)
		self.db = self.client[self.mongo_db]
	
	def close_spider(self, spider):
		self.client.close()

	def process_item(self, item,spider):
		if isinstance(item,YunQiBkListItem):
			self._process_bklist_item(item)
		else:
			self._process_bkdetail_itme(item)
		return item
	
	def _process_bklist_item(self, item):
		self.db.bookInfo.insert(dict(item))

	def _process_bkdetail_itme(self, item):
		self.db.bookhot.insert(dict(item))