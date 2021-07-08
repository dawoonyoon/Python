fruitList=['Apple','Melon','Grape','Strawberry']
fruitChoice = int(input('반복할 숫자를 넣어주세요: '))
Apple_count=0
Melon_count=0
Grape_count=0
Strawberry_count=0
for i in range(1,fruitChoice+1):
	print(i,end='')

	if i%3==0:
		print(fruitList[0],end='')
		Apple_count=Apple_count+1
	if i%4==0:
		print(fruitList[1],end='')
		Melon_count=Melon_count+1
	if i%5==0:
		print(fruitList[2],end='')
		Grape_count=Grape_count+1
	if i%8==0:
		print(fruitList[3],end='')
		Strawberry_count=Strawberry_count+1
	
	print('')

print('\n==<<Fruit Count List>>>==\n')

print('1. Apple\t{}회'.format (Apple_count))
print('2. Melon\t{}회'.format (Melon_count))
print('3. Grape\t{}회'.format (Grape_count))
print('4. Strawberry\t{}회'.format (Strawberry_count))