
money = int(input("현금 잔액을 입력하세요:"))
card = input("card 소지 여부 True or False:")

if int(money) >= 3000 or card == "True":
	print("택시 타고 가라")
else:
	print("걸어 가라")
