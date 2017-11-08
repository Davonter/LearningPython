#!/usr/bin/python3

__author__ = 'wynter-wang'

'''
关于函数的一些定义
'''

import math

def my_abs(x):	# 求绝对值
	if not isinstance(x, (int, float)):
		raise TypeError('Bad type')		# 非整数或浮点数，抛出异常
	if x >= 0:
		return x
	else:
		return -x
		
def move(x, y, step, angle=0):
	nx = x + step * math.cos(angle)
	ny = y + step * math.sin(angle)
	return nx, ny
	

n = abs(-20)
print(n)

x, y = move(100, 100, 5, math.pi / 6)
print(x, y)


#my_abs('123')	#type error