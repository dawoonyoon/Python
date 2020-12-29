#for와 range를 이용한 구구단

for i in range(2,10):
	for j in range(1, 10):
		print(i*j, end=" ")
	print('')

# print(i*j, end=" ") end를 넣어 준 이유는 해당 결과값을 출력할 때 다음줄로 넘기지 않고 그 줄에 계속해서 출력하기 위해서
# print(' ')는 2단, 3단 등을 구분하기 위해 두 번째 for문이 끝나면 결과값을 다음 줄부터 출력하게 해주는 문장
