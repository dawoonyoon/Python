#Q1
홍길동_점수=[80, 75, 55]
print(sum(홍길동_점수)/len(홍길동_점수))
print('')
#Q2
number=13
if number%2==0:
	print('13은 짝수가 맞습니다')
else:
	print('13은 홀수 입니다.')
print('')
#Q3
HGD_SSN='881120-1068234'
HGD_yymmdd=HGD_SSN[:6]
HGD_idnum=HGD_SSN[7:]
print('HGD_yymmdd:',HGD_yymmdd)
print('HGD_idnum:',HGD_idnum)
print('')
#Q4
pin='881120-1068234'
yaya=pin.split('-')
print(yaya[1][0])
print('')
#Q5
a='a:b:c:d'
b=a.replace(':','#')
print(b)
print('')