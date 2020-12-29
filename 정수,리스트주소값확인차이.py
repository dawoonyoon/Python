a=[1,2,3]
b=a

print('a, b 변경 전 =', a, '/', b)
a[1]=4
print('a[1] 변경 후 =', a, '/', b)


a=3
b=3
print('a is b :', a is b)
print('a == b:', a==b)
print(id(a))
print(id(b))

a=[1,2,3]
b=[1,2,3]
print('a is b :', a is b)
print('a == b:', a==b)
print(id(a))
print(id(b))