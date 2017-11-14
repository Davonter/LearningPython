#!/usr/bin/python3
'''
我们把变量从内存中变成可存储或传输的过程称之为序列化；
相反，把变量内容从序列化的对象重新读到内存称之为反序列化
'''

import pickle

d = dict(name='bob', age=20, score=90)

data = pickle.dumps(d)
print(data)		# 序列化

reborn = pickle.loads(data)		# 反序列化
print(reborn)