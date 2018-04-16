#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-25 10:55:08
# @Author  : xuetu

import requests
from scrapy.selector import Selector
import pymysql
import  random
import time

cnn = pymysql.connect(host='127.0.0.1',user='xuetu',passwd='123',db='CrawlDB',charset='utf8')
cursor = cnn.cursor()

def crawl_ips():
	base_url = 'https://www.kuaidaili.com/free/inha/'
	agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
	for i in  range(1,2222):
		url = base_url+'{0}'.format(i)
		response = requests.get(url,headers={'User-Agent':agent})
		time.sleep(random.randint(5,15))

		selector = Selector(text=response.text)
		#this is wrong   ->    selector = Selector(response.text)
		all_trs = selector.css('#list tr')
		print('ok0')

		ip_list = []
		for tr in all_trs[1:]:
			
			ip_text = tr.css("td::text").extract()
			ip = ip_text[0]
			port = ip_text[1]
			proxy_type = ip_text[3]
			ip_list.append((ip,port,proxy_type))
			print('ok1')

			for ip_info in ip_list:
				print('ok2')
				cursor.execute(
					"insert into proxy_ips (ip,port,proxy_type) VALUES('{0}','{1}','{2}')".format(
						ip_info[0],ip_info[1],ip_info[2])
					)
				cnn.commit()

class Getip(object):
	
	def get_ip(self):
		sql = '''
			select ip,port,proxy_type from proxy_ips 
			order by rand()
			limit 1
			'''
		cursor.execute(sql)
		cnn.commit()
		for ip_info in cursor.fetchall():
			ip = ip_info[0]
			port = ip_info[1]
			proxy_type = ip_info[2]

			self.judge_ip(ip,port,proxy_type)
		 

	def judge_ip(self,ip,port,proxy_type):

		url = 'http://www.baidu.com'
		proxy_url = '{0}://{1}:{2}'.format(ip[2],ip[0],ip[1])
		
		try:
			proxy_dict = {
				'http' : proxy_url                                  #how to make proxy_dict
			}
			response = requests.get(url,proxies=proxy_dict)
			return True
		except Exception as e:
			print("voild ip!")
			self.delete_ip(ip)
			return False
		else:
			code = response.statu_code
			if code >=200 and code <=300 :
				return True
			else:
				print('voild ip!')
				self.delete_ip(ip)
				return False
		tr
	def delete_ip(self,ip):
		cursor.execute(
			"delete ip from proxy_ips where ip='{0}'".format(ip)
		)
		cnn.commit()
		return True

crawl_ips()