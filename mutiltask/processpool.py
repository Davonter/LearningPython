#!/usr/bin/python3

'''
进程池: 创建大量的进程
'''

from multiprocessing import Pool
import os, time, random

def long_time_task(name):
	print('Run task %s(%s)...' % (name, os.getpid()))
	start = time.time()
	time.sleep(random.random() * 3)
	end = time.time()
	print('Task %s run %0.2f seconf.' % (name, (end - start)))
	
if __name__ == '__main__':
	print('Parent process %s.' % os.getpid())
	p = Pool(4)		# 创建四个线程
	for i in range(6):
		p.apply_async(long_time_task, args=(i,))
	time.sleep(1)
	print('Wait for all subprocess done...')
	p.close()
	p.join()
	print('All subprocess done.')

