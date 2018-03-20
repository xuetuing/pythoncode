#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-20 09:57:37
# @Author  : xuetu


import requests
import re

def get_xsrf():

	agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE'
	header = {
		'HOST' : "www.zhihu.com",
		'Referer' : "https://www.zhihu.com",
		'User-agent' : agent,
	}
	response = session.get('https://www.zhihu.com', headers=header)
	fi = open("/home/hacker/a.txt","w")
	fi.write(response.text)
	fi.close
	match_obj = re.match('[\s\S]*name="_xsrf" value="(.*?)"', response.text)
	if match_obj:
		return match_obj.group(1)
	else:
		return ''

session = requests.session()
a = get_xsrf()
print(a)