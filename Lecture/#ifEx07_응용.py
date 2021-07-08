categorizing = input("현금입니까? 카드입니까?")
if categorizing == "현금":
	money = int(input("현금 잔액을 입력하세요:"))
	if int(money) >= 3000:
		print("택시 타고 가라")
	else:
		print("걸어 가라")
else:
	card = input("card 소지 여부 True or False:")
	if card == "True":
		print("택시 타고 가라")
	else:
		print("걸어 가라")
