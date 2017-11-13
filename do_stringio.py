#!/usr/bin/python3

from io import StringIO

# write to StringIO
f = StringIO()
f.write('Hello')
f.write(' ')
f.write('Python')

print(f.getvalue())


# read from StringIO
f = StringIO('窗前明月光,\n疑是地上霜.\n举头望明月,\n低头思故乡.')
while True:
	s = f.readline()
	if s == '':
		break
	print(s.strip())		#strip 按换行符切断字符串
