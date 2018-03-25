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