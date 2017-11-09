#!/usr/bin/python3

__author__ = 'wynter'

'''
TDD信号是有的，而且我用专业的软件查看当前环境的小区配置了，所以我根据现网配置把eNB 的频点设为band40最高优先级频点(中国移动)。现在有一个问题，我运行TDD模式，偶尔有一两次手机能看到当前eNB小区信息，而且手机还会去attach，但是其余大部分时间都是看不到的。网上有人说因为TDD是时分，所以除了要进行频率同步还要进行时间同步，也就是上下行时隙同步，为了eNB能正常工作，每次都要侦听当前现网TDD的时隙，和现网同步成功后才能正常工作，但现在我就是不知道怎么去侦听现网的配置信息并自动更新配置。还请有人能帮我解答一下！
'''


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