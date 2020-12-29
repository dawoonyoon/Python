#coffee

coffee=5
while True:
	money=int(input("돈을 넣어 주세요: "))
	if money==300:
		print("커피를 제공합니다. 남은 커피의 양은 '{}'개 입니다." .format(coffee-1))
		coffee=coffee-1
	elif money>300:
		print("거스름돈 '{}'을 주고 커피를 줍니다. 남은 커피의 양은 '{}'개 입니다." .format(money-300,coffee-1))
		coffee=coffee-1
	else:
		print("커피값을 확인 해주세요.")
		print("남은 커피의 양은 '{}'개 입니다." .format(coffee))
	if coffee==0:
		print("SOLD OUT")
		break
