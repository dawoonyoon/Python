#a 리스트의 각 항목에 3을 곱한 결과를 result 리스트에 담는 방법
a = [1, 2, 3, 4]
result = []
for num in a:
	result.append(num*3)

print(result)

#리스트 내포를 사용하는 방법
a=[1,2,3,4]
result = [num * 3 for num in a]
print(result)

#[1,2,3,4] 중에서 짝수에만 3을 곱하여 담고 싶을때, 리스트 내포 안에 if조건 사용
a=[1,2,3,4]
result = [num *3 for num in a if num % 2 == 0]
print(result)
