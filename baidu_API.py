#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-15 06:52:19

from aip import AipOcr
import json
APP_ID = '10929016'
API_KEY = 'md4jjjdjwKC6OWN5iwdkTFKR'
SECRET_KEY = 'jsNPrC9cUhGKjGdeGKpuZ2VaAu0B4ztu'

aipocr = AipOcr(APP_ID,API_KEY,SECRET_KEY)

fpath = "/home/hacker/pythonts/im.png"
def get_content(fpath):
	with open(fpath,'rb') as fp:
		return fp.read()
 	
options = {
	'detect_direction':'true',
	'language_type':'eng',
} 
result = aipocr.basicGeneral(get_content(fpath),options)
print(json.dumps(result))
