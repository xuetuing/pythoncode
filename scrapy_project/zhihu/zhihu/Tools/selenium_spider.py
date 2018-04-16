#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-26 11:25:45
# @Author  : xuetu

from  selenium import webdriver
from scrapy.selector import Selector

browser = webdriver.chrome(executable_path="")
browser.get(url)

#browser.page_source

selector = Selector(text=browser.page_source)


