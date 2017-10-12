#!/usr/bin/python
# coding: gb2312
import re
import urllib
import urllib2
import os

def getpage(url):
	req = urllib2.Request(url)
	res = urllib2.urlopen(req)
	page = res.read()
	return page

def mkurllist(page):   #for the last one
	res_url = re.compile(r'href="(\d{4}_?\d{0,2}.htm)">\d{0,2}')
#	res_tail = re.compile(r'href="(\d{4}_?\d{0,2}.htm)">\u5c3e\u9875')
#   no way to handle the question about messy code
	ilist = re.findall(res_url, page)
	N_ilist = list(set(ilist))   #Duplicate removal
	N_ilist.sort(key=ilist.index)
	while :
		page = getpage(f_url+N_ilist[-1])
		ilist = re.findall(res_url, page)
		N_ilist1 = list(set(ilist))
		N_ilist1.sort(key=ilist.index)
		N_ilist = list(set(N_ilist).union(set(N_ilist1)))
# find the max flag and the nin flag

	urllist = [f_url+s for s in N_ilist]
	return urllist

firsturl = input('please enter the first url(str):')
f_url = f_url = firsturl[0:39]
page = getpage(firsturl)
mkurllist(page)

#print urllist


	
	
	


