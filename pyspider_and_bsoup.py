#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-10-25 22:32:10
# Project: crawljs

from pyspider.libs.base_handler import *
from bs4 import BeautifulSoup

class Handler(BaseHandler):
    crawl_config = {
    }
    @every(minutes=24 * 60)
    def on_start(self):
        url = 'https://mm.taobao.com/self/model_info.htm?user_id=687471686&is_coment=false'
        self.crawl(url, callback=self.index_page,fetch_type = 'js')

    @config(age=10 * 24 * 60 * 60)
    def index_page(self,response):
        soup = BeautifulSoup(response.content,'lxml')
        for i in soup.find_all('ul',class_='mm-p-info-cell clearfix'):
            for j in i.find_all('li'):
                print(j.get_text())