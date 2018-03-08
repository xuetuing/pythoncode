#!/usr/bin/python
# -*- coding: utf-8 -*-
fo = open('/home/hacker/py_test/te_b.txt','a')
fi = open('/home/hacker/py_test/te.txt')
# the first wey
#for x in fi.readlines(): #readlines() return a list
#	fo.write(x.replace('hello','csv'))
#fi.close()
#fo.close()

#the second way
s = fi.read()  #read() return a string 
fo.write(s.replace('hello','csv'))
fi.close()
fo.close()
