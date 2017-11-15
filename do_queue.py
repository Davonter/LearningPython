#!/usr/bin/python3

'''
在父进程中创建两个子进程，一个往Queue里面写数据，一个从Queue里面读数据
'''

from multiprocessing import Process, Queue
import os, time, random

# 写进程
def write(q):
	print('Process to write: %s' % os.getpid())
	for value in ['A', 'B', 'C']:
		print('Put %s to queue...' % value)
		q.put(value)
		time.sleep(random.random())

# 读进程		
def read(q):
	print('Process to read: %s' % os.getpid())
	while True:
		value = q.get(True)
		print('Get %s from queue' % value)

if __name__ == '__main__':
	# 父进程创建Queue，并传给各个子进程
	q = Queue()
	pw = Process(target=write, args=(q,))
	pr = Process(target=read, args=(q,))
	
	# 启动写子进程
	pw.start()
	# 启动读子进程
	pr.start()
	
	# 等待写结束
	pw.join()
	
	# 读是死循环  只能强制终止
	pr.terminate()
	
