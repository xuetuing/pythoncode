#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

file_path = []

def showpath(path):
	content_name = os.listdir(path)
	for s in content_name:
#		file_path.append(path+'/'+s)
		fpath = os.path.join(path,s)
		if os.path.isdir(fpath):
			showpath(fpath)
		else:
			file_path.append(fpath)
	return file_path

print showpath('/home/hacker/py_test')
 
