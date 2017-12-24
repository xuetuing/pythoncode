#!/usr/bin/python
# -*- coding: utf-8 -*-
from pyspider.libs.base_handler import *
import os
from bs4 import BeautifulSoup

DIR_PATH = '/home/hacker/pythonts'

class Handler(BaseHandler):
	crawl_config = {
	}
	def __init__(self):
		self.base_url = 'https://mm.taobao.com/json/request_top_list.htm?page='
		self.page_num = 1
		self.total_num = None
		self.deal = Deal()
		self.brief = []

	@every(minutes=24 * 60)
	def on_start(self):
		url = self.base_url+str(self.page_num)
		print url
		self.crawl(url, callback=self.index_page)
		self.page_num +=1

	@config(age=10 * 24 * 60 * 60)
	def index_page(self, response):
		for each in response.doc('.lady-name').items():    
			self.crawl(each.attr.href, callback=self.detail_page,fetch_type='js')  #phantomjs for js webpage

	@config(priority=2)
	def detail_page(self, response):
		domain = 'http:'+response.doc('.mm-p-domain-info > span').text()
		print domain
	 	brief = self.deal.getinfo(response)    
		self.crawl(domain,callback=self.domain_page)

	def domain_page(self,response):
		name = response.doc('.mm-p-model-info-left-top dd > a').text()
		dir_path = self.deal.mkDir(name)
		if dir_path:
			self.deal.saveBrief(self.brief,dir_path, name)
			count = 1
			imgs = response.doc('.mm-aixiu-content img').items()
			for img in imgs:
				url = 'http:'+img.attr.src
				print url
				if url:
					extension = self.deal.getExtension(url)
					file_name = name+str(count)+'.'+extension
					count +=1
					self.crawl(url, callback=self.save_img,
						save={'dir_path': dir_path, 'file_name': file_name})  # send dir_path and file_name to save_img with sava param
	def save_img(self,response):
		content = response.content        #response.content, get all of the page content
		dir_path = response.save['dir_path']
		file_name = response.save['file_name']
		file_path = dir_path+'/'+file_name
		self.deal.saveImg(content,file_path)

class Deal:
	def __init__(self):
		self.path = DIR_PATH
		if not self.path.endswith('/'):
			self.path = self.path + '/'
		if not os.path.exists(self.path):
			os.makedirs(self.path)

	def mkDir(self, path):
		path = path.strip()
		dir_path = self.path + path
		exists = os.path.exists(dir_path)
		if not exists:
			os.makedirs(dir_path)
			return dir_path
		else:
			return dir_path

	def saveImg(self, content, path):
		f = open(path, 'wb')
		f.write(content)
		f.close()

	def saveBrief(self, brief, dir_path, name):
		file_name = dir_path + "/" + name + ".txt"
		f = open(file_name, "a+")
		for item in brief:
			f.write(item)
			f.write('\n')
		
	def getExtension(self, url):
		extension = url.split('.')[-1]
		return extension

	def getinfo(self,response):		
		brief = []
		soup = BeautifulSoup(response.content,'lxml')
		for i in soup.find_all('ul',class_='mm-p-info-cell clearfix'):
			for j in i.find_all('li'):
				brief.append(j.get_text().encode('utf-8'))
		return brief