#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

f_path = []
g = os.walk('/home/hacker/py_test')
for path,con_name,filelist in g:
	for filename in filelist:
		fpath = os.path.join(path,filename)
		f_path.append(fpath)
print f_path