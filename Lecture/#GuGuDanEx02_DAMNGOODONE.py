for k in range(2,10):
	print("# %d단 #" %k, end='       ')
print("")
for i in range(1,10):
	for j in range(2,10):
		print("%d x %d =%2d" % (j,i,i*j), end='     ')
	print("")
