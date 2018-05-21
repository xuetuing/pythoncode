#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-21 10:55:01
# @Author  : xuetu

import os,time,random
from  multiprocessing import Process,Pool,Queue,Pipe

def process_run(name):
	print("child process %s (%s) is running......" % (name,os.getpid()))

def run_task(name):
	print("process %s (pid = %s) is runnng ...." % (name,os.getpid()))
	time.sleep(random.random()*2)
	print("process %s end." % name)

def proc_write(q,urls):
	print("process %s is writing ." % os.getpid())
	for url in urls:
		q.put(url)
		print('%s was writen to Queue.' % url)
		time.sleep(random.random())

def proc_read(q):
	print("process %s is reading from Queue." % os.getgid())
	while True:
		url = q.get(True)
		print("%s was getten from Queue." % url)

def proc_send(pipe,urls):
	for url in urls:
		pipe.send(url)
		print('process %s send %s  to pipe.' % (os.getppid(),url))
		time.sleep(random.random())

def proc_recv(pipe):
	while True:
		print('process %s recv %s from  pipe.' % (os.getppid(),pipe.recv()))
		time.sleep(random.random())
		
if __name__ == '__main__':

	# print("parent process is : %s" % os.getppid())
	# for i in range(5):
	# 	p = Process(target=process_run,args=(str(i),))
	# 	print('process %d will start.' % i)
	# 	p.start()
	# p.join()
	# print("Process end.")

	# print("Current process is : %s" % os.getppid())
	# pool = Pool(processes=6) #Processes = 3
	# for i in range(6):	
	# 	pool.apply_async(run_task,args=(i,))
	# print('waitting all subprocesses done.')
	# pool.close()
	# pool.join()
	# print("all processes end.")

	# q = Queue()
	# proc_writer1 = Process(target=proc_write,args=(q,['url_1','url_2','url_3']))
	# proc_writer2= Process(target=proc_write,args=(q,['url_4','url_5','url_6']))
	# proc_reader = Process(target=proc_read,args=(q,))

	# proc_writer1.start()
	# proc_writer2.start()
	# proc_reader.start()

	# proc_writer1.join()
	# proc_writer2.join()
	# proc_reader.terminate()
	pipe = Pipe()
	p1 = Process(target=proc_send,args=(pipe[0],['url_'+str(i) for i in range(10)]))
	p2 = Process(target=proc_recv,args=(pipe[1],))

	p1.start()
	p2.start()

	p1.join()
	p2.terminate()
