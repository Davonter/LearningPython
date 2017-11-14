#!/usr/bin/python3

'''
将字典序列化为json对象
'''

import json

d = dict(name='Bob', age=20, score=90)
data = json.dumps(d)	# 序列化
print('JSON data is a str:', data)
rebore = json.loads(data)	# 反序列化
print(rebore)


# 用类表示
class Student(object):
	def __init__(self, name, age, score):
		self.name = name
		self.age = age
		self.score = score
	
	def __str__(self):
		return 'Student object(%s, %s, %s)' % (self.name, self.age, self.score)
		
s = Student('Bob', 20, 88)
std_data = json.dumps(s, default=lambda obj: obj.__dict__)
print('Dump Student:', std_data)

rebuild = json.loads(std_data, object_hook=lambda d: Student(d['name'], d['age'], d['score']))
print(rebuild)