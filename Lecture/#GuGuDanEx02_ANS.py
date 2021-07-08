for i in range(2,10):
	print("#",i,"단", end='')
print('\n')

print("="*48)

for a in range(2,10):
	for b in range(2,10):
		print("%d*%d=%2d" %(a,b,a*b), end=' ')
	print('\n')
print("="*48)
