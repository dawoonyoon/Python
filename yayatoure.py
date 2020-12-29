#Q1
answers=[]
numbers_given=[1,2,3,1]
for i in range(len(numbers_given)):
    for j in range(i+1,len(numbers_given)):
        if numbers_given[i]+numbers_given[j] not in answers:
            n=numbers_given[i]+numbers_given[j]
            answers.append(n)
answers.sort() #오름차순으로 정렬
print(answers)
