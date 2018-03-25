#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-24 09:10:44
# @Author  : xuetu


import hashlib

def get_md5(url):
	if isinstance(url, str):
		url = url.encode('utf-8')
	m = hashlib.md5()
	m.update(url)
	return m.hexdigest()