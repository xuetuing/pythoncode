#!/usr/bin/python
# -*- coding: utf-8 -*-

# print string to file

fi = open('/home/hacker/py_test/print_f.txt','a')

print >> fi, "I am"
print >> fi, "a student."

print >> fi, "I am" , #the comma meaning no '\n'
print >> fi, "a student."

fi.close()