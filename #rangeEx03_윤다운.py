marks = [90,25,67,45,80]
print(len(marks)) #5
print(marks[0]) #90
print(marks)

for number in range(len(marks)):	# number = 0 ~ 4
	if marks[number] < 60:
		continue
	print("%d번 학생 축하합니다. 합격입니다." % (number+1))
