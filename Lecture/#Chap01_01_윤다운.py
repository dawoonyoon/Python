#Q2_166833
sum=0
i=1
while i<=1000:
	if i % 3 == 0:
		sum+=i
	i=i+1
print(sum)

#Q3
i=0
while True:
	i+=1
	if i <= 5:
		print('*' * i)
	else:
		break

#Q4
for i in range(1,101):
	print('{} ' .format(i), end='')
print('')