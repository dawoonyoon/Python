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

for t in TName:
    print('{:15}'.format(t),end='\t')
print('')
print('='*80)
for i in range(len(empInfo)):
    if 'T' in empInfo[i][0].upper():
        empInfo[i][0]='계약직'
    else:
        empInfo[i][0]='정규직'
print(empInfo,end=' ')
print('')
'''
for i in range(len(empInfo)):
    for j in range(len(TName)):
        if i==j
'''