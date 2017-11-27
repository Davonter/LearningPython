#!/usr/bin/python3

# 用来存储名片
card_infos = []

def print_menu():
	'''完成打印功能菜单'''
	print("="*50)
	print("		名片管理系统 v0.1")
	print(" 1. 添加一个新的名片")
	print(" 2. 删除一个名片")
	print(" 3. 修改一个名片")
	print(" 4. 查询一个名片")
	print(" 5. 显示所有的名片")
	print(" 6. 保存信息")
	print(" 7. 退出系统")
	
def add_new_card_info():
	'''添加一个新名片'''
	new_name = input("请输入新的名字:")
	new_qq = input("请输入新的QQ:")
	new_weixin = input("请输入新的微信:")
	new_addr = input("请输入新的地址:")
	
	# 定义一个新的字典，用来存储一个新的名片
	new_info = {}
	new_info['name'] = new_name
	new_info['qq'] = new_qq
	new_info['weixin'] = new_weixin
	new_info['addr'] = new_addr
	
	# 将一个字典，添加到列表中
	global card_infos
	card_infos.append(new_info)
	
def find_car_info():
	'''用来查询一个名片'''
	global card_infos
	
	find_name = input("请输入你要查询的名字")
	find_flag = 0
	
	for temp in card_infos:
		if find_name == temp['name']:
			print("%s\t%s\t%s\t%s" % (temp['name'], temp['qq'], temp['weixin'], temp['addr']))
			find_flag = 1
			break
			
	if find_flag == 0:
		print("查无此人")
		
		
def show_all_info():
	'''显示所有的名片'''
	global card_infos
	
	print("姓名\tQQ\t微信\t地址")
	for temp in card_infos:
		print("%s\t%s\t%s\t%s" % (temp['name'], temp['qq'], temp['weixin'], temp['addr']))
		

def save_2_file():
	'''把已经添加的信息保存到文件'''
	f = open("backup.data", 'w')
	
	f.write(str(card_infos))
	f.close()
	
def load_info():
	global card_infos
	
	try:
		f = open("backup.data")
		
		card_infos = eval(f.read())
		f.close()
	except Exception:
		pass
		
def main():
	'''完成对整个程序的控制'''
	# 灰度(加载)之前的数据到程序中
	load_info()
	
	# 1. 打印功能提示
	print_menu()
	
	while True:
		# 获取用户的输入
		num = int(input("请输入操作序号："))
		
		# 根据用户的数据执行响应的功能
		if num == 1:
			add_new_card_info()
		elif num == 2:
			pass
		elif num == 3:
			pass
		elif num == 4:
			find_car_info()
		elif num == 5:
			show_all_info()
		elif num == 6:
			save_2_file()
		elif num == 7:
			break
		else:
			print("输入有误，请重新输入")
		
		print("")
		
if __name__ == '__main__':
	main()
	
	
	
	
	
	
	
	
	
	
	
	
	