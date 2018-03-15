#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

html = """
<ul class="cat-list">
    <li><a href="" title="">女装</a></li>
    <ul class="txt-list-brand clear none">
        <li><a target="_blank" href="http://xxxx.com/" title="xxx">xxx</a></li>
        <li><a target="_blank" href="http://xxxx.com/" title="xxx">xxx</a></li>
        <li><a target="_blank" href="http://xxxx.com/" title="xxx">xxx</a></li>
     </ul>
     
    <li><a href="" title="">男装</a></li>
    <ul class="txt-list-brand clear none">
        <li><a target="_blank" href="http://xxxx.com/" title="xxx">xxx</a></li>
        <li><a target="_blank" href="http://xxxx.com/" title="xxx">xxx</a></li>
        <li><a target="_blank" href="http://xxxx.com/" title="xxx">xxx</a></li>
     </ul>
     
     <li><a href="" title="">女鞋</a></li>
    <ul class="txt-list-brand clear none">
        <li><a target="_blank" href="http://xxxx.com/" title="xxx">xxx</a></li>
        <li><a target="_blank" href="http://xxxx.com/" title="xxx">xxx</a></li>
        <li><a target="_blank" href="http://xxxx.com/" title="xxx">xxx</a></li>
     </ul>
     
</ul>
"""
soup = BeautifulSoup(html,'lxml')
for i in soup.find_all('ul',class_='cat-list'):
	for j in i.find_all('li'):
		print(j.get_text())
