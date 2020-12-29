#1-10 합
add = 0
for i in range(1, 11):
	add = add + i
print(add)

#1-10 짝수의 합
add = 0
for i in range(1, 11):
	if i % 2 == 0:
		add = add + i
print(add)

# 1-10 홀수의 합
add = 0
for i in range(1, 11):
	if i % 2 == 1:
		add = add + i
print(add)
