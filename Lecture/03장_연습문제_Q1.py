#Q1_shirt
a = "Life is too short, you need python"
if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")

#Q2_166833
result=0
i=1
while i<=1000:
	if i % 3 == 0:
		result+=i
	i+=1
print(result)

#Q3
i=0
while True:
	i+=1
	if i <= 5:
		print('*' * i)
	else:
		break

#Q4
for i in range(1,101):
	print('{} ' .format(i), end='')
print('')

#Q5_79.0
aList=[70,60,55,75,95,90,80,80,85,100]
print(sum(aList)/len(aList))

sum = 0
for i in aList:
	sum = sum + i
print(sum / len(aList))

#Q6_[2,6,10]
numbers=[1,2,3,4,5]
result=[]
for n in numbers:
	if n%2==1:
		result.append(n*2)
print(result)

numbers=[1,2,3,4,5]
result=[n*2 for n in numbers if n%2==1]
print(result)