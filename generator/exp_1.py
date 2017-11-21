#!/usr/bin/python

def yield_test(n):
	for i in range(n):
		yield call(i)
		print("i=", i)
		
	print("Do sth")
	print("End")
	
def call(i):
	return i*2
	
for i in yield_test(5):
	print(i, ",")
	
