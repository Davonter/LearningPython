#!/usr/bin/python3

import multiprocessing
import time

def worker(interval):
	print('Interval = ', interval)
	print('p.name is ', p.name)
	n = 5
	while n > 0:
		print('The time is %s ' % time.ctime())
		time.sleep(interval)
		n -= 1

if __name__ == '__main__':
	p = multiprocessing.Process(target=worker, args=(3,))
	p.start()
	print('p.pid = %s' % p.pid)
	print('p.name = %s' % p.name)
	print('p.is_alive',  p.is_alive)