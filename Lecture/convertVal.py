#10진수 32
convertVal = 56

cvB = bin(convertVal) #2진수로 변환
cvO = oct(convertVal) #8진수로 변환
cvH = hex(convertVal) #16진수로 변환

print(cvB)
print(cvO)
print(cvH)

#format(number,[notation]함수로 진수 출력)
print("### format ###")
print('{:#o}'.format(10))
print('{:#x}'.format(10))
print('{:#b}'.format(10))

print("### format, notation ###")
print(format(10, 'b')) #2진수 변환
print(format(10, 'o')) #8진수 변환
print(format(10, 'x')) #16진수 변환

#진번 변환 함수
def convertBase(number, base):
	T="0123456789ABCDEF"
	i,j=divmod(number,base)

	if i==0:
		return T[j]
	else:
		return convertBase(i,base)+T[j]

inputNumber = 50

print('{} to bin => {}'.format(inputNumber, convertBase(inputNumber,2)))
print('{} to oct => {}'.format(inputNumber, convertBase(inputNumber,8)))
print('{} to hex => {}'.format(inputNumber, convertBase(inputNumber,16)))