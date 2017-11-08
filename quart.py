#!/usr/bin/python3.5

__author__ = 'wynter-wang'

'''
求一元二次方程的根:
a * x * x + b * x + c = 0
'''
import math

def quart(a, b, c):
	r = b * b - 4 * a * c
	
	if r < 0:
		print("该方程无解");
	elif a == 0:
		return -(c/b)
	elif r == 0:
		return -b/(2*a)
	else:
		x1 = (-b + math.sqrt(r))/(2*a)
		x2 = (-b - math.sqrt(r))/(2*a)
		return x1, x2
		

a = float(input("Please input a, a= "))
b = float(input("Please input b, b= "))
c = float(input("Please input c, c= "))

print(quart(a, b, c))
	