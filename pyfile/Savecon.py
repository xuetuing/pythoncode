#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
 
class Deal:
	def __init__(self):
		self.path = DIR_PATH
		if not self.path.endswith('/'):
			self.path = self.path + '/'
		if not os.path.exists(self.path):
			os.makedirs(self.path)

	def mkDir(self, path):
		path = path.strip()
		dir_path = self.path + path
		exists = os.path.exists(dir_path)
		if not exists:
		os.makedirs(dir_path)
		return dir_path
		else:
		return dir_path

	def saveImg(self, content, path):
		f = open(path, 'wb')
		f.write(content)
		f.close()

	def saveBrief(self, content, dir_path, name):
		file_name = dir_path + "/" + name + ".txt"
		f = open(file_name, "w+")
		f.write(content.encode('utf-8'))

	def getExtension(self, url):
		extension = url.split('.')[-1]
		return extension