#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib
import urllib2
import re
import os
		
'''
	def getitle(pagecode):
		reg_title = re.compile('<h3 class="core_title_txt.*?>(.*?)</h3',re.S)
		title = re.search(reg_title, pagecode)
		if title:
			return title.group(1)
		else:
			print 'have a some question'

	def getpgnum(pagecode):
		reg_num = re.compile('<span class="red">(.*?)</span>',re.S)
		pgnum = re.search(reg_num, pagecode)
		if pgnum:
			return pgnum.group(1)
		else:
			print 'have a some question'
	def getcontent(pagecode):
		reg_con = re.compile('<div id="post_content.*?>(.*?)</div>',re.S)
		content = re.findall(reg_con, pagecode)
		if content:
			return content
		else:
			print "have a question"
'''
baseurl = 'https://tieba.baidu.com/p/3138733512'
seelz = '?see_lz='+raw_input('please enter 1 for see LZ only,or 0\n')
'''
		pagenum = input('which page should be collected?(enter a num):')
		print "getting the pagecode of the %d page." % pagenum
		pagecode = self.getpage(pagenum)
		title = self.getitle(pagecode)
		pgnum = self.getpgnum(pagecode)
		content = self.getcontent(pagecode)
		print 'now write the content of the %d page to file.' % pagenum
		self.writedata(content)
'''
pagenum = 1
url = baseurl+seelz+'&pn='+str(pagenum)
req = urllib2.Request(url)
res = urllib2.urlopen(req)
pagecode = res.read().decode('utf-8')
reg_title = re.compile('<h3 class="core_title_txt.*?>(.*?)</h3',re.S)
title = re.search(reg_title, pagecode)
if title:
	print title.group(1)
else:
	print 'have a some question'

reg_num = re.compile('<span class="red">(.*?)</span>',re.S)
pgnum = re.search(reg_num, pagecode)
if pgnum:
	print pgnum.group(1)
else:
	print 'have a some question'
reg_con = re.compile('<div id="post_content.*?>(.*?)</div>',re.S)
content = re.findall(reg_con, pagecode)
if content:
	print content
else:
	print "have a question"