#!/usr/bin/python

'''
运用正则表达式匹配任意一个邮箱
'''

import re

text = input("Please input an email address: ")

m = re.compile(r'^([a-zA-Z0-9]+)@([a-zA-Z0-9]+)\.([a-z]{2,3})$')

if re.match(m, text):
	print("%s is a valid email." % text)
else:
	print("%s is not a valid email." % text)