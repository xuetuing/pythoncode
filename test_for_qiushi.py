#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib
import urllib2
import re

url = 'https://www.qiushibaike.com/hot/'
user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0'

req = urllib2.Request(url)
req.add_header("User-Agent", user_agent)
res = urllib2.urlopen(req)
page = res.read().decode('utf-8')
reg = re.compile('<h2>(.*?)</h2>.*?<span>(.*?)</span>(.*?)<div class="stats.*?'+
	'class="number">(.*?)</i>.*?"single-clear"></div>(.*?)</div>',re.S)
#reg = re.compile('<h2>(.*?)</h2>.*?<span>(.*?)</span>(.*?)<div class="stats.*?class="number">(.*?)</i>?',re.S)
reg_mtext = re.compile('main-text">(.*?)<div',re.S)
items = re.findall(reg, page)
pagestory = []
for item in items:
	if not re.search('img', item[2]):
		replaceBR = re.compile('<br/>')
		text = re.sub(replaceBR, '\n', item[1])
		pagestory.append([item[0].strip(),text.strip(),item[3].strip(),item[4].strip()])				
if pagestory:
	for story in pagestory:
		print 'the author is: %s' % story[0]
		print 'the content is : %s' % story[1]
		print 'the comment num is : %d' % int(story[2])
		main_text = re.search(reg_mtext, story[3])
		if main_text: 
			print 'the pref comment is : %s' % main_text.group(1)
		else:
			print 'the pref comment is : none'
else:
	print 'none'
