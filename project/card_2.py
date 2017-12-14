#!/usr/bin/python3

card_info = []	# 定义一个全局列表，保存用户信息

def print_menu():
	print("="*50)
	print(" 	个人信息管理系统 v0.1")
	print(" 1. 添加一个新名片")
	print(" 2. 删除一个名片")
	print(" 3. 修改一个名片")
	print(" 4. 查询一个名片")
	print(" 5. 显示所有名片")
	print(" 6. 保存信息")
	print(" 7. 退出系统")
	print("="*50)
	print("\n")

def show_all_info():
	print("		信息统计")
	print(" 姓名	性别	年龄	手机号码")
	global card_info
	for item in card_info:
		print(" %s\t%s\t%s\t%s" % (item['name'], item['sex'], item['age'], item['number']))

def add_new_card():
	new_name = input(" 1. 请输入姓名: ")
	new_sex = input(" 2. 请输入性别: ")
	new_age = input(" 3. 请输入年龄: ")
	new_number = input(" 4. 请输入手机号码: ")

	# 定义一个字典，将新名片储存
	new_info = {}
	new_info['name'] = new_name
	new_info['sex'] = new_sex
	new_info['age'] = new_age
	new_info['number'] = new_number
	
	global card_info
	card_info.append(new_info)

def find_one_card():
	global card_info
	
	find_name = input("请输入你要查找的名字: ")
	find_flag = 0
	
	for temp in card_info:
		if find_name == temp['name']:
			print("%s\t%s\t%s\t%s" % (temp['name'], temp['sex'], temp['sex'], temp['number']))
			find_flag = 1
			break
	
	if find_flag == 0:
		print("查无此人")
		
def show_all_info():
	global card_info
	
	print("姓名\t性别\t年龄\t手机号码")
	
	for temp in card_info:
		print("%s\t%s\t%s\t%s" % (temp['name'], temp['sex'], temp['age'], temp['number']))
	
	print('\n')
	
def save_2_file():
	global card_info
	
	with open('bak.data', 'w') as f:
		f.write(str(card_info))
	f.close()
	
def load_info():
	global card_info
	
	try:
		with open("bak.data") as f:
			card_info = eval(f.read())
		f.close()
	except Exception:
		pass
		
def main():
	'''用户信息管理系统'''
	#show_all_info()	# 打印菜单
	load_info()
	
	print_menu()
	try:
		while True:
			num = int(input("请输入选项："))
			if num == 1:
				add_new_card()
			elif num == 2:
				del_one_card()
			elif num == 3:
				change_one_card()
			elif num == 4:
				find_one_card()
			elif num == 5:
				show_all_info()
			elif num == 6:
				save_2_file()
			elif num == 7:
				break
			else:
				print("输入有误，请重新输入")
	except:
		print("\n异常，退出系统")

if __name__ == '__main__':
	main()