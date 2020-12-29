# 1번 orange 1000원, 2번 strawberry 2500원, 3번 peach 1500원, 4번 mango 2000원, 5번 grape 2000원

fruitName = ["Orange","Strawberry","Peach","Mango","Grape"]
fruitPrice = [1000,2500,1500,2000,2000]
i = 0
print("*"*5,"영우대학교 과일 판매 머신 v01","*"*5)
print("="*42)
for i in range(len(fruitName)):
	print('[ {} {}] : {}원' .format(i+1,fruitName[i], fruitPrice[i]))
while True:
	print("="*42)
	purchase_number = int(input("구매번호를 입력하세요 (1-5)"))
	if purchase_number==1:
		print('[ {} {}] : {}원'.format(1,fruitName[0],fruitPrice[0]))
	elif purchase_number==2:
		print('[ {} {}] : {}원'.format(2,fruitName[1],fruitPrice[1]))
	elif purchase_number==3:
		print('[ {} {}] : {}원'.format(3,fruitName[2],fruitPrice[2]))
	elif purchase_number==4:
		print('[ {} {}] : {}원'.format(4,fruitName[3],fruitPrice[3]))
	elif purchase_number==5:
		print('[ {} {}] : {}원'.format(5,fruitName[4],fruitPrice[4]))
	else:
		print("? 번호를 확인하세요.")
