#!/usr/bin/python
# -*- coding: utf-8 -*-

#this code is for the pics of the website(http://www.rosmm.com)
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

def mkurllist(firsturl,page):   #for the last one
	reg_tail = re.compile(r'href="\d{3,4}_?(\d{0,2}).htm">βҳ')
	reg_current = re.compile(r'class="current">(\d{1,2})')

	tailpage = re.search(reg_tail, page)

	if not tailpage:
		current = re.search(reg_current, page).group(1)
		urllist = [f_url+mdir+'_%d.htm' %i for i in range(2,int(current)+1)]
		urllist.append(f_url+mdir+'.htm')
	else:
		tailpage = tailpage.group(1)
		urllist = [f_url+mdir+'_%d.htm' %i for i in range(2,int(tailpage)+1)]
		urllist.append(f_url+mdir+'.htm')
	return urllist

def getimg(page,dirpath):
	global x
	res_img = re.compile(r'<img\ssrc="(.+?\.jpg)"\s/>')
	imglist = re.findall(res_img, page)
	for imgurl in imglist:
		urllib.urlretrieve(imgurl,dirpath+'/%d.jpg' % x)
		x+=1

firsturl = input('please enter the first url(str):')

while (firsturl != 'q'):
	reg_dir = re.compile(r'.*/(\d{3,4})_{0,1}')
	mdir = re.search(reg_dir, firsturl).group(1)                   
	f_url = firsturl[0:39]
	dirpath = '/home/hacker/pythonts/'+mdir
	if not os.path.exists(dirpath):
		os.mkdir(dirpath)
		print 'please wait......'
		page = getpage(firsturl)
		urllist = mkurllist(firsturl, page)
		for imlist in urllist:
			page1 = getpage(imlist)
			getimg(page1,dirpath)
		x = 0
		urllist = []
		firsturl = input('please enter the first url(str):')
	else:
		print 'the file is exist,please input another firsturl!\n'
		firsturl = input('please enter the first url(str):')
