number=int(input("Enter a number:"))

if number < 20:
	print("WTF? Check your number")
else:
	print("1 is not a prime number")
	for i in range(2,number+1):
		isPrime = True
		for j in range(2, i):
			if (i % j) == 0:
				isPrime = False
				break
		if isPrime:
			print(i, "is a prime number")
		else:
			print(i,"is not a prime number")
			print(j,"times",i//j,"is",i)
