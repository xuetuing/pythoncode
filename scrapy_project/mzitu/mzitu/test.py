#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-02 11:39:27
# @Author  : xuetu


import requests
import base64
from selenium  import webdriver
header = {
			"User-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
			"Accept-Ranges": "bytes",
			"X-Frame-Options": "SAMEORIGIN" ,
			"Content-Type": "image/jpeg",
		}
url = "http://i.meizitu.net/2018/04/15a10.jpg"
browser = webdriver.Firefox(executable_path="/home/hacker/geckodriver")
res = browser.get(url)

# url = "http://i.meizitu.net/2018/04/15a08.jpg"
# res = requests.get(url,headers=header)
# data = base64.b64encode(res.content)
# fi = open("im.jpg","wb")
# fi.write(data)
# fi.close()