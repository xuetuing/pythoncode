#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division  # for float

def jia(x,y):
	return x+y

def jian(x,y):
	return x-y

def cheng(x,y):
	return x*y

def chu(x,y):
	return x/y

operator = {'+':jia,'-':jian,'*':cheng,'/':chu}

#operator['+'](2,4)
def f(x,o,y):
	print operator.get(o)(x,y)

f(2,'+',4)