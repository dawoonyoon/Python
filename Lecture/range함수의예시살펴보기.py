add = 0
for i in range(1, 11):
	add = add + i

print(add)

grades = [90, 25, 67, 45, 80]
for number in range(len(grades)):
	if grades[number] < 60:
		continue
	print("%d번 학생 축하합니다. 합격입니다." % (number+1))
