def automation(i):
	print('입력하신 구매번호는 {}입니다.'.format(purchase_number))
	coin = int(input('코인을 투입하세요: '))
	print('\n')
	print('투입된 금액은 {}원 입니다.' .format(coin))
	print('거스름돈은 {}원 입니다.' .format(coin - fruitPrice[i-1]))
	
fruitName = ["Orange","Strawberry","Peach","Mango","Grape"]
fruitPrice = [1000,2500,1500,2000,2000]

print("*"*5,"영우대학교 과일 판매 머신 v01","*"*5)
print("="*42)

for i in range(len(fruitName)):
	print('[ {} {}] : {}원' .format(i+1,fruitName[i], fruitPrice[i]))

while True:
	print("="*42)
	purchase_number = int(input("구매번호를 입력하세요 (1~5): "))
	if purchase_number==1:
		automation(purchase_number)
	elif purchase_number==2:
		automation(purchase_number)
	elif purchase_number==3:
		automation(purchase_number)
	elif purchase_number==4:
		automation(purchase_number)
	elif purchase_number==5:
		automation(purchase_number)
	else:
		print("? 번호를 확인하세요.")
