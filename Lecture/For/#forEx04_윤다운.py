grades = [90, 25, 67, 45, 80]

number = 0
for grade in grades:
	number = number +1
	if grade < 60:
		continue
	print("%d번 학생 축하합니다. 합격입니다." % number)
