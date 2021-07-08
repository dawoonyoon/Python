numbers_given=[1,1,2,3,3,2,1,1,2,3,3]
'''
for i in range(len(numbers_given)-2):
	for j in range(i+1,len(numbers_given)-1):
		if numbers_given[i]==numbers_given[j]:
            #numbers_given.remove(numbers_given[i])
			del numbers_given[i]
print(numbers_given)
'''
for i in range(len(numbers_given) - 1, 0, -1):
	if numbers_given[i] == numbers_given[i-1]:
		del numbers_given[i]
print(numbers_given)