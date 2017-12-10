#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from dingdian.items import DingdianItem

class Myspider(scrapy.Spider):
	name = 'dingdian'
	allowed_domains = ['x23us.com']
	base_url = 'http://www.x23us.com/class/'
	extenurl = '.html'

	def start_requests(self):
		for i in range(1,11):
			url = self.base_url + str(i) + '_1' + self.extenurl
			yield Request(url,self.parse)
		    #yield Request('http://www.23wx.com/quanben/1')

	def parse(self,response):
		max_num = BeautifulSoup(response.text,'lxml').find('div',calss_='pagelink').find_all('a')[-1].get_text()
		baseurl = str(response.url)[:-7]
		for num in range(1,int(max_num)+1):
			url = baseurl + '_' + str(num) + self.extenurl
			yield Request(url,callback=self.get_name)

	def get_name(self,response):
		tds = BeautifulSoup(response.text,'lxml').find_all(tr,bgcolor="#FFFFFF")
		for td in tds:
			novelname = td.find('a').get_text()
			novelurl = td.find('a')['href']
			yield Request(novelurl,callback=self.get_chapterurl,mate={'name':novelname,'url':novelurl})

	def get_chapterurl(self,response):
		item = DingdianItem()
		print str(response.mate['name'])
		item['name'] = str(response.mate['name']).replace('\xa0', '')
		item['novelurl'] = response.mate['url']
		category = BeautifulSoup(response.text,'lxml').find('table').find('a').get_text()
		author = BeautifulSoup(response.text,'lxml').find('table').find_all('td')[1].get_text()
		baseurl = BeautifulSoup(response.text,'lxml').find('p',class_='btlinks').find('a',class_='read')['href']
		name_id = str(baseurl)[-6:-1].replace('/','')
		item['category'] = str(category).replace('/','')
		print str(category)
		item['author'] = str(author).replace('/','')
		item['name_id'] = name_id
		return item

