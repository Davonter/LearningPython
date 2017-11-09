#!/usr/bin/python3

__author__ = 'wynter'


# 运用递归求阶乘
def fact(n):
	if n == 1:
		return n
	return n * fact(n - 1)
	
print("fact(1) = %d" % fact(1))
print("fact(4) = %d" % fact(4))
print("fact(6) = %d" % fact(6))

# 运用递归求汉诺塔
def move(n, a, b, c):
	'''
	n表示第一个柱子上环的数量
	'''
	if n == 1:
		print('move', a, '-->', c)
	else:
		move(n-1, a, c, b)		#
		move(1, a, b, c)
		move(n-1, b, a, c)
		
move(4, 'A', 'B', 'C')