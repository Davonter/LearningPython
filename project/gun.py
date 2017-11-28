#!/usr/bin/python3

class Person(object):
	'''人的类'''
	def __init__(self, name):
		super(Person, self).__init__()
		self.name = name
		self.gun = None	#用来保存枪对象的引用
		self.hp = 100
	
	def anzhuang_zidan(self, dan_jia_temp, bullet_temp):
		'''把子弹装到弹夹中'''
		# dan_jia.保存子弹
		dan_jia_temp.baocun_zidan(bullet_temp)
		
	def anzhuang_danjia(self, gun_tmp, dan_jia_temp):
		'''把弹夹安装到枪中'''
		gun_tmp.baocun_danjia(dan_jia_temp)
		
	def naqiang(self, gun_tmp):
		'''拿起一把枪'''
		self.gun = gun_tmp
		
	def koubanji(self, diren):
		'''让枪发射子弹去打敌人'''
		self.gun.fire(diren)
	def diaoxue(self, ssl):
		'''根据杀伤力，让敌人掉血'''
		self.hp -= ssl
	
	def __str__(self):
		if self.gun:
			return "%s的血量为:%d, 他的枪为%s" % (self.name, self.hp, self.gun)
		else:
			if self.hp > 0:
				return "%s的血量为:%d, 他没有枪" % (self.name, self.hp)
			else:
				return "%s 已挂" % self.name
class Gun(object):
	'''枪类'''
	def __init__(self, name):
		super(Gun, self).__init__()
		self.name = name
		self.danjia = None	# 用来记录弹夹对象的引用
		
	def baocun_danjia(self, dan_jia_temp):
		self.danjia = dan_jia_temp
	
	def fire(self, diren):
		'''枪从弹夹中获取一发子弹，然后让这发子弹去击中敌人'''
		'''先从弹夹中取子弹，然后让子弹去伤害敌人'''
		zidan_tanchu = self.danjia.tanchu()
		
		if zidan_tanchu:
			zidan_tanchu.dazhong(diren)
		else:
			print("弹夹中没有子弹了")
	
	def __str__(self):
		if self.danjia:
			return "枪的信息为%s, %s" % (self.name, self.danjia)
		else:
			return "枪的信息为%s, 这把枪没有弹夹" % (self.name)
			
class Danjia(object):
	'''弹夹类'''
	def __init__(self, max_num):
		super(Danjia, self).__init__()
		self.max_num = max_num
		self.bullet_list = []	# 记录所有子弹的引用
		
	def baocun_zidan(self, bullet_temp):
		'''将这颗子弹保存'''
		self.bullet_list.append(bullet_temp)
	
	def tanchu(self):
		'''弹出最上面的子弹'''
		if self.bullet_list:
			return self.bullet_list.pop()
		else:
			return None
	
	def __str__(self):
		return "弹夹信息为%d/%d" % (len(self.bullet_list), self.max_num)

class Bullet(object):
	'''子弹类'''
	def __init__(self, ssl):
		super(Bullet, self).__init__()
		self.ssl = ssl
		
	def dazhong(self, diren):
		'''让敌人掉血'''
		diren.diaoxue(self.ssl)
		
def main():
	'''主流程'''
	
	#1. 创建老王对象
	laowang = Person("Laowang")
	#2.	创建一个枪对象
	ak47 = Gun("ak47")
	#3. 创建一个弹夹对象
	dan_jia = Danjia(20)
	#4.	创建一些子弹
	for i in range(15):
		bullet = Bullet(10)
		#5.	创建一个敌人
		#Laowang.安装子弹到弹夹中
		laowang.anzhuang_zidan(dan_jia, bullet)
	
	#6.	老王把子弹安装到弹夹
	laowang.anzhuang_danjia(ak47, dan_jia)
	
	#test:测试弹夹信息
	print(dan_jia)
	#test:测试枪的信息
	print(ak47)
	
	#7. 老王把弹夹装到枪上
	laowang.naqiang(ak47)
	print(laowang)
	#8. 老王拿枪
	gebi_laosong = Person("Laosong")
	print(gebi_laosong)
	
	#9. 老王打敌人
	laowang.koubanji(gebi_laosong)
	print(gebi_laosong)
	print(laowang)

if __name__ == '__main__':
	main()
	