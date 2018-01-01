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
		self.fileform = '.xls'
		self.Slist= []
		self.bsdict = {}
		self.collist = [u'L',u'Part-no.',u'S',u'unit',u'Unit weight   (kg)',u'Rmarks']    # need to set

	def bk_sheet_list(self,filepath):

		slist = []
		rmlist = [u'Summary sheet',u'Sprache',u'UnVisible',u'Shapes',u'add',u'标准预制件索引']
		for filename in glob.glob(filepath+'*'+self.fileform):
			bk = xlrd.open_workbook(filename)
			slist = slist + bk.sheet_names() 
			self.bsdict[filename] = bk.sheet_names()
		for value in slist:
			if rmlist[-1] in value:
				continue
			elif value in rmlist:
				continue
			else:
				self.Slist.append(value)
		return self.Slist

	def return_bkname(self,sheet):     
		# return the list of bkname(path+name) those has the same sheet
		# make a two-dimensional array
		# input a sheetname 
		# ergodic the list, if have the same value ,return the path of book
		bklst = []
		if self.Slist.count(sheet) > 1 :  	
			for key in self.bsdict.keys():
				if sheet in self.bsdict[key]:
					bklst.append(key)   
			return bklst
		else:
			for key in self.bsdict.keys():
				if sheet in self.bsdict[key]:
					bklst.append(key)
					break   
			return bklst
	def write_excel(self,book,sheet,New_sheet):   # find there Designated col ant write to new excel
		# read the firs row of the excel
		# ergodic the fist row list
		# if find the same value, write to new excel
		bk = xlrd.open_workbook(book)
		shet = bk.sheet_by_name(sheet)  ##
		first_row = shet.row_values(5)
		print first_row
		row_lst = []
		for index,colname in enumerate(self.collist):
			colname = filter(lambda x : x in first_row,[colname, colname.capitalize()])
			if colname:
				n = self.find_index(colname[0],first_row)
				col_data = shet.col_values(n)[0:30]
				while '' in col_data:
					col_data.remove('')
				row_lst.append(len(col_data))
				row = self.nrows + 1
				for i in range(1,len(col_data)):
					New_sheet.write(row,index+1,col_data[i])
					row = row + 1
			else:
				continue
		self.nrows = self.nrows + max(row_lst)-1
		for  i  in range(1,self.nrows+1):
			New_sheet.write(i,0,sheet)   #New_sheet.write(i,0,sheet+'/'+shet.cell(5,8))

		# need to judge the max len of the col_data of every sheet

	def find_index(self,value,lst):
		for index in range(len(lst)):
			if lst[index] == value:
				return index

filepath = "/home/hacker/pythonts/"
filedestination = "/home/hacker/pythonts/excel/"
mk_excel = Excel_handle()
slist = mk_excel.bk_sheet_list(filepath)
new_bk = xlwt.Workbook()

for sheet in set(slist):
	New_sheet = new_bk.add_sheet(sheet,cell_overwrite_ok=True)
	bklst = mk_excel.return_bkname(sheet)
	biaotou = [u'名称',u'规格',u'图纸编号（物料编号）',u'材料',u'单位',u'单重',u'备注']  ##
	for i in range(0,len(biaotou)):  # if possible,del
		New_sheet.write(0,i,biaotou[i])	
	for book in bklst:                                 ## not work
		mk_excel.write_excel(book,sheet,New_sheet)
	mk_excel.nrows = 0
new_bk.save(filedestination+"test.xls")