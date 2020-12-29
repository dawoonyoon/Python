my_list=[75,65,100,80,90,55,95,30,20,50]
for i in range(len(my_list)):
	for j in range(i+1,len(my_list)):
		if my_list[i]>my_list[j]:
			temp=my_list[i]
			my_list[i]=my_list[j]
			my_list[j]=temp
print(my_list)
