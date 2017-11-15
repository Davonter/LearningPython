#!/usr/bin/python3

import os

print('The process %s start...' % os.getpid())

pid = os.fork()

if pid == 0:
	print('I am the child process(%s), my parent process is (%s)' % (os.getpid(), os.getppid()))
else:
	print('I(%s) just create a child process(%s)' % (os.getpid(), pid))
	
	