#!/usr/bin/python
# -*- coding: utf-8 -*-

from pyquery import PyQuery as pq
'''
d= pq('<div><p>test1</p><p>test2</p></div>')

print d('p')
print d('p').html() #only return the first match
print d('p').eq(1).html() #.eq(0),.eq(1)-->test1 and test2
'''
d=pq("<p id='my_id'><a href='http://hello.com'>hello</a></p>")
print d('a').attr('href')
print d('p').attr('id')
print d('a').attr('href','http://baidu.com')

d = pq('<div></div>')
print d.add_class('my_class') #<div class="my_class"/>

filter(function or None, sequence)

find()

hasClass(name)

children(selector=None)

parents(selector=None)

clone()

empty()

nextAll()

not_(selector)