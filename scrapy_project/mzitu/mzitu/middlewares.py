# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

class Mzitu(object):
    """docstring for Mzitu"""
    def process_request(self,request,spider):
        referer = request.meta.get('referer',None)
        if referer:
            request.headers['referer'] = referer
        
        
