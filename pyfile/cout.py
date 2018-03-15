#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
fi = open("/home/hacker/py_test/te.txt")
count = 0
for s in fi.readlines():
	i = re.findall('hello',s)
	count += len(i)
print "have %d 'hello'" % count
