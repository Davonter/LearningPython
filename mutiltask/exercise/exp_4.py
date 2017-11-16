#!/usr/bin/python3

import multiprocessing
import time

def worker(interval):
	print("worker start %s" % time.ctime())
	time.sleep(interval)
	print("worker end %s" % time.ctime())

if __name__ == '__main__':
	p = multiprocessing.Process(target=worker, args=(3,))
	p.daemon = True
	p.start()
	print("End!")