vI01=10
vI02=20

print('변경전:vI01:',vI01)	
print('변경전:vI02:',vI02)

temp=vI01	#왼쪽에 있는 애한테 오른쪽에 있는 애의 값을 부여
vI01=vI02
vI02=temp

print('변경후:vI01:',vI01)
print('변경전:vI02:',vI02)
