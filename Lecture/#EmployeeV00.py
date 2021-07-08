TName = ["구분","사원명","입사일","급여"]
empInfo = [
	['T160501',"캔디","2016-05-10"],
	['R160510',"장미","2016-05-10"],
	['t160811',"튤립","2016-08-15"],
	['T160821',"포도","2016-08-22"],
	['r160850',"사과","2016-08-30"]]
empPayTable = [
	[250,10],
	[200,12],
	[300,9],
	[230,11],
	[150,12]]

for t in range(len(TName)):
	print("%15s" % (TName[t]), end=' ')
print('')
print('-'*80)
for i in range(len(empInfo)):
	if 'T' in empInfo[i][0].capitalize():
		empInfo[i][0] = "계약직"
	else:
		empInfo[i][0] = "정규직"

for info_idx in range(len(empInfo)):
	for tag_idx in range(len(TName)):
		if tag_idx == len(TName) - 1:
			print("%15d" %(empPayTable[info_idx][0]*empPayTable[info_idx][1]))
		else:
			print("%15s"% empInfo[info_idx][tag_idx], end=' ')
	print("")

#print(empInfo)

print('')