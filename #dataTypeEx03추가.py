a=[1,2,3]
b=a
print('a, b 변경 전 =',a,'/',b)
a[1]=4
print('a[1] 변경 후=',a,'/',b)

a=[1,2,3]
b=a[:]
print('a, b 변경 전 =',a,'/',b)
a[1]=4
print('a[1] 변경 후=',a,'/',b)

from copy import copy
a=[1,2,3]
b=copy(a)
print('a, b 변경 전 =',a,'/',b)
a[1]=4
print('a[1] 변경 후=',a,'/',b)

print('동일객체유무확인=',b is a)