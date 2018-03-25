#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-20 09:57:37
# @Author  : xuetu


import os
import sys


print '***获取当前目录***'
print os.getcwd()
print os.path.abspath(os.path.dirname(__file__))

print '***获取上级目录***'
print os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
print os.path.abspath(os.path.dirname(os.getcwd()))
print os.path.abspath(os.path.join(os.getcwd(), ".."))

print '***获取上上级目录***'
print os.path.abspath(os.path.join(os.getcwd(), "../.."))

	