#!/usr/bin/python
# -*- coding: utf-8 -*-
import xlrd
import xlwt
import xlutils
import glob
from numpy import *

class Excel_handle(object):
	"""docstring for ClassName"""
	nrows = 0
	def __init__(self):      #can use global var
		self.fileform = '.xlsx'
		self.slist= []
		self.bsdict = {}
		self.collist = []    # need to set

	def bk_sheet_list(self,filepath):

		for filename in glob.glob(filepath+'*'+self.fileform):
			bk = xlrd.open_workbook(filename)
			self.slist = self.slist + bk.sheet_names() 
			self.bsdict[filename] = bk.sheet_names()
		return self.slist

	def return_bkname(self,sheet):     
		# return the list of bkname(path+name) those has the same sheet
		# make a two-dimensional array
		# input a sheetname 
		# ergodic the list, if have the same value ,return the path of book
		bklst = []
		if self.slist.count(sheet) > 1 :  	
			for key in self.bsdict.keys():
				if sheet in self.bsdict[key]:
					bklst.append(key)   
			return bklst
		else:
			for key in self.bsdict.keys():
				if sheet in self.bsdict[sheet]:
					bklst.append(key)
					break   
			return bklst
	def write_excel(self,book,nrows,new_sheet):   # find there Designated col ant write to new excel
		# read the firs row of the excel
		# ergodic the fist row list
		# if find the same value, write to new excel
		bk = xlrd.open_workbook(book)
		shet = bk.sheet_by_name(sheet)
		m = 0
		row_lst = []
		first_row = shet.row_values(0)
		for colname in self.collist:
			if colname in first_row:
				n = find_index(colname, first_row)
				col_data = shet.col_values(n)
				row = nrows + 1
				for i in range(1,len(col_data)):
					New_sheet.write(row,m,col_data[i])
					m = m+1
					row = row + 1
				row_lst.append(len(col_data))
			else:
				continue
		nrows = nrows + max(row_lst)-1

		# need to judge the max len of the col_data of every sheet

	def find_index(self,value,lst):
		for i in range(len(lst)):
			if lst[i] == value:
				return index

filepath = "/home/hacker/pythonts/"
filedestination = "/home/hacker/pythonts/excel/"
mk_excel = Excel_handle()
slist = mk_excel.bk_sheet_list(filepath)
new_bk = xlwt.Workbook()

for sheet in set(slist):
	New_sheet = new_bk.add_sheet(sheet)
	bklst = mk_excel.return_bkname(sheet)
	biaotou = []  ##
	for i in range(0,len(biaotou)):  # if possible,del
		New_sheet.write(0,i,biaotou[i])
	nrows = 0
	for book in bklst:
		mk_excel.write_excel(book,nrows,New_sheet)
filename.save(filedestination+file+".xls")