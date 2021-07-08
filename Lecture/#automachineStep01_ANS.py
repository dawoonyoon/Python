fruitName = ["Orange","Strawberry","Peach","Mango","Grape"]
fruitPrice = [1000,2500,1500,2000,2000]

print("*"*7,"영우대학교 과일 판매 머신 V01","*"*7)
for i in range(len(fruitName)):
	print("[ %d %s ] : %d 원" %(i+1,fruitName[i],fruitPrice[i]))
print("="*45)

while True:
	number=int(input("구매번호를 입력하세요(1-5):"))
	if number in range(1,6):
		print("%d번 %s %d원" %(number,fruitName[number-1],fruitPrice[number-1]))
	else:
		print("번호 확인 바람")
