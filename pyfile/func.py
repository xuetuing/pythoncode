#!/usr/bin/python
#coding:utf8

def fun(x,y):
    if(x == y):
        print x,'=',y
    else:
        print x,'!=',y

def show(x,y):
    print "得到一个 %d 元,%s 味的食品！" % (x,y)

s1 = raw_input("input a num:")
s2 = raw_input("input a str:")
#fun(s1,s2)
show(int(s1),s2)
