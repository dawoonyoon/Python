'''a=[1,2,3]
b=[1,2,3]
a=(1,2,3)
b=(1,2,3)'''
a={"kk":3}
b={"kk":3}

print(id(a))
print(id(b))
print('a is b:', a is b)
print('a == b:', a == b)
