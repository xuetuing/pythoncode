#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib
import urllib2
import re

class QSBK:
	"""docstring for QSBK"""
	def __init__(self):
		self.pageindex = 1
		self.user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0'
		self.enable = False   # hava a test / True 
		self.stories = []

	def getpagecode(self,pageindex):
		url = 'https://www.qiushibaike.com/hot/page/'+str(pageindex)
		req = urllib2.Request(url)
		req.add_header('User-Agent',self.user_agent)
		res = urllib2.urlopen(req)
		pagecode = res.read().decode('utf-8')
		return pagecode

	def getpagestory(self,pageindex):
		pagecode = self.getpagecode(self.pageindex)  #here should have a judge for empty pagecode
		pagestories = []
		reg = re.compile('<h2>(.*?)</h2>.*?<span>(.*?)</span>(.*?)<div class="stats.*?'+
	    'class="number">(.*?)</i>.*?"single-clear"></div>(.*?)</div>',re.S)
		items = re.findall(reg, pagecode)
		for item in items:
			if not re.search('img', item[2]):
				replaceBR = re.compile('<br/>')
				text = re.sub(replaceBR, '\n', item[1])
				pagestories.append([item[0].strip(),text.strip(),item[3].strip(),item[4].strip()])				
		return pagestories

	def loadpage(self):
		if self.enable:
			if len(self.stories)<2:
				pagestories = self.getpagestory(self.pageindex) # need a judge
				if pagestories:
					self.stories.append(pagestories)
					self.pageindex += 1

	def getonestory(self,pagestories,page):
		reg_mtext = re.compile('main-text">(.*?)<div',re.S)
		for story in pagestories:
			input = raw_input()
			self.loadpage()
			if input == 'q':
				self.enable = False
				return
			print 'the %d page of qiushibaike: ' % page
			print 'the author is: %s' % story[0]
			print 'the content is : %s' % story[1]
			print 'the comment num is : %d' % int(story[2])
			main_text = re.search(reg_mtext, story[3])
			if main_text: 
				print 'the pref comment is : %s' % main_text.group(1)
			else:
				print 'the pref comment is : none'

	def start(self):
		print 'please input "enter" for new info or "q" for exist:'
		self.enable = True
		self.loadpage()
		newpage = 0
		while self.enable:
			if len(self.stories)>0:
				pagestories = self.stories[0]
				newpage += 1
				del self.stories[0]
				self.getonestory(pagestories,newpage)
spider = QSBK()
spider.start()


