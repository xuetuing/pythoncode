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
		for i in range(1,3):
			url = self.base_url + str(i) + '_1' + self.extenurl
			yield Request(url,self.parse)
		    #yield Request('http://www.23wx.com/quanben/1')

	def parse(self,response):    # the word "class_" must be took care of
		max_num = BeautifulSoup(response.text,'lxml').find('div',class_="pagelink").find_all('a')[-1].get_text()
		#max_num = BeautifulSoup(page,"lxml").find('dd',class_="pages").find_all('a')[-1].get_text()
		baseurl = str(response.url)[:-7]
		#for num in range(1,int(max_num)+1):
		for num in range(1,3):
			url = baseurl + '_' + str(num) + self.extenurl
			yield Request(url,callback=self.get_name)

	def get_name(self,response):
		tds = BeautifulSoup(response.text,'lxml').find_all('tr',bgcolor="#FFFFFF")
		for td in tds:
			novelname = td.find_all('a')[1].get_text()
			novelurl = td.find('a')['href']
			yield Request(novelurl,callback=self.get_chapterurl,meta={'name':novelname,'url':novelurl})
			# there is a 'meta' dict, not 'mate'
	def get_chapterurl(self,response):   
		item = DingdianItem()     # ??????
		#item['name'] = str(response.meta['name']).replace('\xa0', '')
		item['name'] = response.meta['name']
		item['novelurl'] = response.meta['url']
		category = BeautifulSoup(response.text,'lxml').find('table').find('a').get_text()
		author = BeautifulSoup(response.text,'lxml').find('table').find_all('td')[1].get_text()
		#baseurl = BeautifulSoup(response.text,'lxml').find('p',class_='btlinks').find('a',class_='read')['href']
		#name_id = str(baseurl)[-6:-1].replace('/','')
		name_id = str(response.meta['url'])[-5:].replace('/','')
		item['category'] = category
		item['author'] = author
		item['name_id'] = name_id
		
		return item
