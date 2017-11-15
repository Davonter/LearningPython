#!/usr/bin/python3

from multiprocessing import Process
import os

# 子進程要運行的代碼
def run_proc(name):
	print('Run child process %s (%s)' % (name, os.getpid()))
	
if __name__ == '__main__':
	print('Parent process is %s' % os.getpid())
	p = Process(target=run_proc, args=('test',))
	print('Child will start...')
	p.start()
	p.join()
	print('Child process end')
