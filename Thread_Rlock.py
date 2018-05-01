#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-19 09:29:37
# @Author  : xuetu


import threading

mylock = threading.RLock()     #RLock
num = 0

class MyThread(threading.Thread):
	"""docstring for MyThread"""
	def __init__(self, name):
		#super(MyThread, self).__init__()
		threading.Thread.__init__(self,name=name)

	def run(self):
		global num
		while  True:
	    		mylock.acquire()
	    		print("%s locked,number: %d" % (threading.current_thread().name,num))
	    		if num >= 4:
	    			mylock.release()
	    			print("%s released,number: %d" % (threading.current_thread().name,num))
	    			break
	    		num += 1
	    		print("%s released,number: %d" % (threading.current_thread().name,num))
	    		mylock.release()

if __name__ == '__main__':
	thread1 = MyThread("thread_1")
	thread2 = MyThread("thread_2")

	thread1.start()
	thread2.start()