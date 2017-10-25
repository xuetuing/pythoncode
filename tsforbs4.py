#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from Worm import *

url = 'https://mm.taobao.com/self/model_info.htm?user_id=687471686&is_coment=false'

page = getpage(url)



'''

soup = BeautifulSoup(html,'lxml')
for i in soup.find_all('ul',class_='cat-list'):
	for j in i.find_all('li'):
		print(j.get_text())
'''