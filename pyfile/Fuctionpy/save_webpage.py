#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
import urllib
import re

url = 'http://cuiqingcai.com/1052.html'

def getpage(url):
	req = urllib2.Request(url)
	res = urllib2.urlopen(req)
	pagecode = res.read()
	return pagecode

	

def save_page(filename,pagecode):
	path = '/home/hacker/pythonts/'+filename+'.html'
	fi = open(path,'a+')
	fi.write(pagecode)
	fi.close()

reg_page = re.compile('<a title="(.*?)" href="(.*?)".*?</a></p>',re.S)
pagecode = getpage(url)
items = re.findall(reg_page, pagecode)
del items[0]
items.pop()
for item in items:
	filename = item[0].decode('utf-8')  # decode for string
	pagecode = getpage(item[1])
	save_page(filename, pagecode)


