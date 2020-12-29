a=[1,2,3]
b=[1,2,3]
print(a is b)	#False
print(a == b)	#True

a=[1,2,3]
b=a
print(a is b)	#True
print(a == b)	#True

a=3
b=3
print(a is b)	#True
print(a == b)	#True

b=3
b=a
print(a is b)	#True
print(a == b)	#True

# is와 ==dml 차이
#	is는 변수가 같은 object를 가리키면 True
#	==는 변수가 같은 value를 가지면 True