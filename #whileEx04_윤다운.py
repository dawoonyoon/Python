idx=5
while True:
	idx=idx-1
	print("남은 커피의 양은 '{}'개입니다." .format(idx))
	if idx==0:
		print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
		break
