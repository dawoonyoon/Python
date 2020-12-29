#Joconfirmv01

import sys

args=sys.argv[1:]
print(args)

if len(args) < 4:
	print('4인 이상의 이름을 입력하세요: ')
else:
	for i in args:
		print(i)
