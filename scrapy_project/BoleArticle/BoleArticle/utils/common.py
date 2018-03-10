#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-08 05:17:38
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import hashlib

def get_md5(url):
	if isinstance(url, str):
		url = url.encode('utf-8')
	m = hashlib.md5()
	m.update(url)
	return m.hexdigest()

# if __name__ == '__main__':
# 	a = get_md5("http://www.baidu.com")
# 	print(a)