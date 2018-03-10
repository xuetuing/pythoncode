# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import json
import pymysql

from scrapy.pipelines.images import ImagesPipeline
from scrapy.exporters import JsonItemExporter
from twisted.enterprise import adbapi

class BolearticlePipeline(object):
	def process_item(self, item, spider):
		return item

'''
class JsonWithEncodingPipeline:
    # 自定义Json文件的导出
    def __init__(self):
        self.file = codecs.open('article.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        lines = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(lines)
        return item

    def spider_closed(self, spider):
        self.file.close()


class JsonExporterPipeline(object):
    # 调用scripy提供的JsonExporter导出Json文件
    def __init__(self):
        self.file = open('articleExporter.json', 'wb')
        self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
'''

class MysqlPipeline(object):
# 采用同步的机制写入MySQL

	def __init__(self):     
		self.conn = pymysql.connect('127.0.0.1', 'xuetu', '888', 'BoleArticle', charset='utf8', use_unicode=True)
		self.cursor = self.conn.cursor()

	def process_item(self, item, spider):
		insert_sql = """
		insert into Article(url_id, title, create_date,origin_url)
		Values ("%s", "%s", "%s", "%s")
		"""
		self.cursor.execute(insert_sql % (item['url_id'], item['title'], item['create_date'], item['origin_url']))
		self.conn.commit()
		return item


class MysqlTwistedPipeline(object):
	def __init__(self, dbpool):
		self.dbpool = dbpool

	@classmethod
	def from_settings(cls, settings):
		dbparms = dict(
			host=settings['MYSQL_HOST'],
			db=settings['MYSQL_DBNAME'],
			user=settings['MYSQL_USER'],
			passwd=settings['MYSQL_PASSWORD'],
			charset='utf8',
			cursorclass=pymysql.cursors.DictCursor,
			use_unicode=True
		)

		dbpool = adbapi.ConnectionPool('pymysql', **dbparms)
		return cls(dbpool)

	def process_item(self, item, spider):
		# 使用Twisted将MySQL插入变成异步执行
		query = self.dbpool.runInteraction(self.do_insert, item)
		query.addErrback(self.handle_error)
		return item

	def handle_error(self, failure):
		# 处理异步插入的异常
		print(failure)

	def do_insert(self, cursor, item):
		# 执行具体的插入
		insert_sql = """
			insert into Article(url_id, title, create_date, origin_url)
			Values ("%s", "%s", "%s", "%s")
			"""
		cursor.execute(insert_sql % (item['url_id'], item['title'], item['create_date'],item['origin_url']))

'''
class ArticleImagePipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        if 'front_image_url' in item:
            for ok, value in results:
                image_file_path = value['path']
            item['front_image_path'] = image_file_path
        return item
'''