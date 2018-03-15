#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib
import urllib2
import re
import os

class Tool:
	"""docstring for Tool"""
	#去除img标签,7位长空格
	removeImg = re.compile('<img.*?>| {7}|')
	#删除超链接标签
	removeAddr = re.compile('<a.*?>|</a>')
	#把换行的标签换为\n
	replaceLine = re.compile('<tr>|<div>|</div>|</p>')
	#将表格制表<td>替换为\t
	replaceTD= re.compile('<td>')
	#把段落开头换为\n加空两格
	replacePara = re.compile('<p.*?>')
	#将换行符或双换行符替换为\n
	replaceBR = re.compile('<br><br>|<br>')
	#将其余标签剔除
	removeExtraTag = re.compile('<.*?>')
	def replace(self,x):
		x = re.sub(self.removeImg,"",x)
		x = re.sub(self.removeAddr,"",x)
		x = re.sub(self.replaceLine,"\n",x)
		x = re.sub(self.replaceTD,"\t",x)
		x = re.sub(self.replacePara,"\n    ",x)
		x = re.sub(self.replaceBR,"\n",x)
		x = re.sub(self.removeExtraTag,"",x)
		#strip()将前后多余内容删除
		return x.strip()

class BDTB:
	"""docstring for BDTB"""
	def __init__(self,baseurl,seelz):
		self.baseURL = baseurl
		self.seeLZ = '?see_lz='+seelz
		self.fi = None
		self.tool = Tool()
	def getpage(self,pagenum):
		url = self.baseURL+self.seeLZ+'&pn='+str(pagenum)
		req = urllib2.Request(url)
		res = urllib2.urlopen(req)
		pagecode = res.read().decode('utf-8')
		return pagecode

	def getitle(self,pagecode):
		reg_title = re.compile('<h3 class="core_title_txt.*?>(.*?)</h3',re.S)
		title = re.search(reg_title, pagecode)
		if title:
			return title.group(1)
		else:
			print 'have a some question'

	def getpgnum(self,pagecode):
		reg_num = re.compile('<span class="red">(.*?)</span>',re.S)
		pgnum = re.search(reg_num, pagecode)
		if pgnum:
			return pgnum.group(1)
		else:
			print 'have a some question'

	def getcontent(self,pagecode):
		reg_con = re.compile('<div id="post_content.*?>(.*?)</div>',re.S)
		items = re.findall(reg_con, pagecode)
		contents = []
		for item in items:
			content = self.tool.replace(item)
			contents.append(content.encode('utf-8'))
		return contents
	
	def touchfile(self):
		filename = raw_input('please enter a filename(str):')
		path = '/home/hacker/pythonts/'+filename
		if not os.path.exists(path):
			self.fi = open(path,'a+')
		else:
			print 'the file is exist'

	def writedata(self,contents):
		for item in contents:
			self.fi.write(item)
		self.fi.close()

	def start(self):
		pagenum = input('which page should be collected?(enter a num):')
		print "getting the pagecode of the %d page." % pagenum
		pagecode = self.getpage(pagenum)
		#print pagecode
		title = self.getitle(pagecode)
		#print title
		pgnum = self.getpgnum(pagecode)
		#print pgnum
		contents = self.getcontent(pagecode)
		if pgnum == None:
			print 'the url is outdated,please try again.'
			return
		self.touchfile()
		self.writedata(contents)

baseurl = 'https://tieba.baidu.com/p/'+str (raw_input('please enter the pageid:'))
seelz = raw_input('please enter 1 for see LZ only,or 0\n')
bdtb = BDTB(baseurl, seelz)
bdtb.start()