#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import urllib
import urllib2
import os
x = 0

def getpage(url):
	request = urllib2.Request(url)
	response = urllib2.urlopen(request)
	page = response.read()
	return page

def mkurllist(page):   #for the last one
	res_url = re.compile(r'href="(\d{4}_?\d{0,2}.htm)">\d{0,2}')
	ilist = re.findall(res_url, page)
	N_ilist = list(set(ilist))   #Duplicate removal
	N_ilist.sort(key=ilist.index)
	urllist = [f_url+s for s in N_ilist]
	return urllist

def getimg(page,dirpath):
	global x
	res_img = re.compile(r'<img\ssrc="(.+?\.jpg)"\s/>')
	imglist = re.findall(res_img, page)
	for imgurl in imglist:
		urllib.urlretrieve(imgurl,dirpath+'/%d.jpg' % x)
		x+=1


# this code(Fenyeweb.py) can not get all the page!
firsturl = input('please enter the first url(str):')
while (firsturl != 'q'):
	dirpath = '/home/hacker/pythonts/'+firsturl[39:43]
	os.mkdir(dirpath)
	f_url = firsturl[0:39]
	print 'please wait......'
	page = getpage(firsturl)
	urllist = mkurllist(page)
	getimg(page,dirpath)
	for imlist in urllist:
		page1 = getpage(imlist)
		getimg(page1,dirpath)
	x = 0
	urllist = []
	firsturl = input('please enter the first url(str):')

