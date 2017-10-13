#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import urllib

def gethtml(url):
	page = urllib.urlopen(url)
	html = page.read()
	return html

def getimg(html):
	res = re.compile(r'src="(.+?\.jpg)" size=')
	imglist = re.findall(res, html)
#	return imglist
	x = 0
	for imgurl in imglist:
		urllib.urlretrieve(imgurl,'1.jpg')
		x+=1

html = gethtml("http://tieba.baidu.com/p/5318940314") 
getimg(html)