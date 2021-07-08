bankInfo = [ ["BANK001", "서건호"],
							["BANK002", "김병태"],
							["BANK003", "신진영"],
							["BANK004", "이선규"],
							["BANK005", "김대은"],
							["BANK006", "양동혁"],
							["BANK007", "최창희"] ];
vBalance = [10000, 20000, 30000, 40000, 50000, 60000, 70000];
cusList = []

class BankV01:
	setBankBalance = 100000

print("*"*7,"은행 관리 프로그램 V01","*"*7)
for i in range(len(bankInfo)):
	print(" {} {}".format( bankInfo[i], vBalance[i]))
print("="*45)


