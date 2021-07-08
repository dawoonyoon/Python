#foodOrderV01.py

foodOrder = ['pizza','pork','potato','coke zero']
foodPrice = [12000, 15000, 7000, 1000]
total = 0
i = 0

for i in foodPrice:
	total = i + total
discount = total*0.85

print(">>> Menu <<<")
print("="*18)
for i in range(len(foodOrder)):
	print("%-10s:"%foodOrder[i], "%5s"%foodPrice[i])
print("="*18)
print("total order price: %5d" % total)
print("15%% discount card: %5d" % discount)
