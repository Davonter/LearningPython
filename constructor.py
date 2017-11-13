#!/usr/bin/python3

'''
重写类的构造方法
'''

class Bird(object):
	def __init__(self):
		self.hungry = True
		
	def eat(self):
		if self.hungry:
			print('Yummy...')
			self.hungry = False
		else:
			self.hungry = True
			

			
class SongBird(Bird):
	def __init__(self):
		#Bird.__init__(self)  # 调用未绑定的超类构造方法
		super(SongBird, self).__init__()  # 使用super方法
		self.sound = 'Style'
		
	def sing(self):
		print(self.sound)
		#pass
		
sb = SongBird()

#test = sb.sing()
test = sb.eat()
test2 = sb.eat()
test
test2
#print(test)
#print(test2)